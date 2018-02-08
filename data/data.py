from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Enum, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pyodbc

import os

try:
    mysql_user = os.environ['sql_user']
    mysql_pass = os.environ['sql_pass']
    mysql_database = os.environ['db_name']
except KeyError as e:
    print("MODIFY setup FILE & RUN AGAIN")
    import sys
    sys.exit()


engine = create_engine('mysql://%s:%s@localhost/%s' % (mysql_user, mysql_pass, mysql_database))
Base = declarative_base()


class Risk(Base):
    __tablename__ = "risk"
    risk_id = Column(Integer, primary_key=True)
    risk_type = Column(String(10))


class Insurer(Base):
    __tablename__ = "insurer"
    insurer_id = Column(Integer, primary_key=True)
    insurer_name = Column(String(10))
    # risk_id = Column(Inte ger, ForeignKey('risk.risk_id'))
    # user = relationship("Risk", back_populates="insurer")


class InsurerRiskMap(Base):
    __tablename__ = "insurerRiskMap"
    insurer_id = Column(Integer, ForeignKey("insurer.insurer_id"), primary_key=True)
    risk_id = Column(Integer, ForeignKey("risk.risk_id"), primary_key=True)


class Form(Base):
    __tablename__ = "form"
    form_id = Column(Integer, primary_key=True)
    insurer_id = Column(Integer, ForeignKey("insurer.insurer_id"))
    risk_id = Column(Integer, ForeignKey("risk.risk_id"))


class FormField(Base):
    __tablename__ = "formField"
    field_id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey("form.form_id"), primary_key=True)
    field_type = Column(Enum("TEXT", "NUMBER", "DATE", "ENUM"))
    field_label = Column(String(20))
    mandatory = Column(Boolean, unique=False, default=True)


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey("form.form_id"), primary_key=True)


class FormFieldValue(Base):
    __tablename__ = "formFieldValue"
    field_id = Column(Integer, ForeignKey("formField.field_id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), primary_key=True)
    form_id = Column(Integer, ForeignKey("form.form_id"), primary_key=True)
    field_value = Column(String(300))


################################################################
# Part Below creates a database with dummy values
#################################################################

def createRiskTable(session):
    row1 = Risk(risk_id=1, risk_type="House")
    row2 = Risk(risk_id=2, risk_type="Automobile")
    row3 = Risk(risk_id=3, risk_type="Prize")
    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.commit()


def createInsurerTable(session):
    row1 = Insurer(insurer_id=1, insurer_name="Honda")
    row2 = Insurer(insurer_id=2, insurer_name="Bajaj")

    session.add(row1)
    session.add(row2)
    session.commit()


def createInsurerRiskMapTable(session):
    row1 = InsurerRiskMap(insurer_id=1, risk_id=1)
    row2 = InsurerRiskMap(insurer_id=1, risk_id=2)
    row3 = InsurerRiskMap(insurer_id=2, risk_id=1)
    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.commit()


def createFormTable(session):
    row1 = Form(insurer_id=1, risk_id=1, form_id=1)
    row2 = Form(insurer_id=1, risk_id=2, form_id=2)
    row3 = Form(insurer_id=2, risk_id=1, form_id=3)
    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.commit()


def createFormFieldTable(session):
    row1 = FormField(field_id=1, form_id=1, field_type="TEXT", field_label="Name", mandatory=True)
    row2 = FormField(field_id=2, form_id=1, field_type="TEXT", field_label="Country", mandatory=True)
    row3 = FormField(field_id=3, form_id=1, field_type="NUMBER", field_label="Age", mandatory=True)
    row4 = FormField(field_id=4, form_id=1, field_type="DATE", field_label="Date Of Birth", mandatory=True)

    row5 = FormField(field_id=1, form_id=2, field_type="TEXT", field_label="Name", mandatory=True)
    row6 = FormField(field_id=2, form_id=2, field_type="TEXT", field_label="Country", mandatory=True)
    row7 = FormField(field_id=3, form_id=2, field_type="NUMBER", field_label="Age", mandatory=True)
    row8 = FormField(field_id=4, form_id=2, field_type="DATE", field_label="Date Of Birth", mandatory=True)
    row9 = FormField(field_id=5, form_id=2, field_type="NUMBER", field_label="PHONE NUMBER", mandatory=True)
    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.add(row4)
    session.add(row5)
    session.add(row6)
    session.add(row7)
    session.add(row8)
    session.add(row9)
    session.commit()


def createUserTable(session):
    row1 = User(user_id=1, form_id=1)
    row2 = User(user_id=1, form_id=2)
    row3 = User(user_id=2, form_id=1)
    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.commit()


def createFormFieldValueTable(session):

    field_id = Column(Integer, ForeignKey("formField.field_id"))
    user_id = Column(Integer, ForeignKey("user.user_id"))
    form_id = Column(Integer, ForeignKey("form.form_id"))
    field_value = Column(String(300))

    row1 = FormFieldValue(field_id=1, user_id=1, form_id=1, field_value="Guido")
    row2 = FormFieldValue(field_id=2, user_id=1, form_id=1, field_value="Alaska")
    row3 = FormFieldValue(field_id=3, user_id=1, form_id=1, field_value=38)
    row4 = FormFieldValue(field_id=4, user_id=1, form_id=1, field_value="2017-01-01")

    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.add(row4)
    session.commit()


def createDB(session):
    createRiskTable(session)
    createInsurerTable(session)
    createInsurerRiskMapTable(session)
    createFormTable(session)
    createFormFieldTable(session)
    createUserTable(session)
    createFormFieldValueTable(session)
    session.commit()

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
s = session()
createDB(s)
s.close()
print "done...."

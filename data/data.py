from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Enum
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pyodbc


engine = create_engine('mysql://root:@localhost/foo')
Base = declarative_base()


class Risk(Base):
    __tablename__ = "risk"
    risk_id = Column(Integer, primary_key=True)
    risk_type = Column(String(10))


class Insurer(Base):
    __tablename__ = "insurer"
    insurer_id = Column(Integer, primary_key=True)
    insurer_name = Column(String(10))
    risk_id = Column(Integer, ForeignKey('risk.risk_id'))
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


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey("form.form_id"), primary_key=True)


class FieldType(Base):
    __tablename__ = "fieldType"
    type_id = Column(Integer, primary_key=True)
    type_name = Column(Enum("TEXT", "NUMBER", "DATE", "ENUM"))


class Field(Base):
    __tablename__ = "field"
    field_id = Column(Integer, primary_key=True)
    field_name = Column(String(20))
    type_id = Column(Integer, ForeignKey("fieldType.type_id"))


class FormFieldMap(Base):
    __tablename__ = "formField"
    form_id = Column(Integer, ForeignKey("form.form_id"), primary_key=True)
    field_id = Column(Integer, ForeignKey("field.field_id"), primary_key=True)


class FormData(Base):
    __tablename__ = "formData"
    id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey("form.form_id"))
    user_id = Column(Integer, ForeignKey("user.user_id"))
    field_id = Column(Integer, ForeignKey("field.field_id"))
    field_value = Column(String(30))

# class RiskData(Base):
#     __tablename__ = "riskData"
#     riskId = Column(Integer, ForeignKey("risk.risk_id"))
#     insurerId = Column(Integer, ForeignKey("insurer.id"))
#     # uid = Column(Integer, ForeignKey("insurer.id"), primary_key=True)
#     fields = Column(String(10), primary_key=True)
#     typeId = Column(Integer, ForeignKey("field.type_id"))
#     order = Column(Integer)


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
    row1 = Insurer(insurer_id=1, insurer_name="Honda", risk_id=1)
    row2 = Insurer(insurer_id=2, insurer_name="Bajaj", risk_id=2)

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


def createFieldTypeTable(session):
    row1 = FieldType(type_id=1, type_name="TEXT")
    row2 = FieldType(type_id=2, type_name="NUMBER")
    row3 = FieldType(type_id=3, type_name="DATE")
    row4 = FieldType(type_id=4, type_name="ENUM")
    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.add(row4)
    session.commit()


def createFieldTable(session):
    row1 = Field(field_id=1, field_name="Age", type_id=2)
    row2 = Field(field_id=2, field_name="Name", type_id=1)
    row3 = Field(field_id=3, field_name="Address", type_id=1)
    row4 = Field(field_id=4, field_name="Country", type_id=1)
    row5 = Field(field_id=5, field_name="DateOfBirth", type_id=3)

    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.add(row4)
    session.add(row5)
    session.commit()


def createFormFieldMap(session):
    row1 = FormFieldMap(form_id=1, field_id=2)
    row2 = FormFieldMap(form_id=1, field_id=1)
    row3 = FormFieldMap(form_id=1, field_id=3)
    row4 = FormFieldMap(form_id=2, field_id=2)

    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.add(row4)
    session.commit()


def createUserTable(session):
    row1 = User(user_id=1, form_id=1)
    row2 = User(user_id=1, form_id=2)
    row3 = User(user_id=2, form_id=1)
    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.commit()


def createFormDataTable(session):
    row1 = FormData(form_id=1, user_id=1, field_id=2, field_value="JEFF")
    row2 = FormData(form_id=1, user_id=1, field_id=1, field_value=23)
    row3 = FormData(form_id=2, user_id=2, field_id=2, field_value="ninja")
    session.add(row1)
    session.add(row2)
    session.add(row3)
    session.commit()


def createDB(session):
    createRiskTable(session)
    createInsurerTable(session)
    createInsurerRiskMapTable(session)
    createFormTable(session)
    createFieldTypeTable(session)
    createFieldTable(session)
    createFormFieldMap(session)
    createUserTable(session)
    createFormDataTable(session)
    session.commit()

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
s = session()

createDB(s)
s.commit()
print "done"

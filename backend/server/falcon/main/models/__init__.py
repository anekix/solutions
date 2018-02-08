from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Enum, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pyodbc

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

# engine = create_engine('mysql://root:Ranjesh9931248492@localhost/foo')
engine = create_engine('mysql://root:@localhost/foo')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

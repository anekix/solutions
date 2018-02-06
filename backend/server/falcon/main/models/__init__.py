from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Enum
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

engine = create_engine('mysql://root:@localhost/foo')

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

# r = Risk(risk_type="House")
S = session()
# s.add(r)


# r = Risk(risk_type="Car")
# s.add(r)

# i = Insurer(insurer_name="Honda", risk_id=6)
# s.add(i)

# f = Field(type="TEXT")
# s.add(f)
# s.commit()
# print s.query(Insurer).all()

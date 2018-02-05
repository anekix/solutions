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
    id = Column(Integer, primary_key=True)
    insurer_name = Column(String(10))
    risk_id = Column(Integer, ForeignKey('risk.risk_id'))
    # user = relationship("Risk", back_populates="insurer")


class Field(Base):
    __tablename__ = "field"
    type_id = Column(Integer, primary_key=True)
    type = Column(Enum("TEXT", "NUMBER", "DATE", "ENUM"))


class RiskData(Base):
    __tablename__ = "riskData"
    riskId = Column(Integer, ForeignKey("risk.risk_id"))
    insurerId = Column(Integer, ForeignKey("insurer.id"))
    # uid = Column(Integer, ForeignKey("insurer.id"), primary_key=True)
    fields = Column(String(10), primary_key=True)
    typeId = Column(Integer, ForeignKey("field.type_id"))
    order = Column(Integer)


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
	row1 = Insurer(id=1, insurer_name="Honda", risk_id=1)
	session.add(row1)
	session.commit()

def createFieldTable(session):
	row1 = Field(type_id=1, type="TEXT")
	row2 = Field(type_id=2, type="NUMBER")
	row3 = Field(type_id=3, type="DATE")
	row4 = Field(type_id=4, type="ENUM")
	session.add(row1)
	session.add(row2)
	session.add(row3)
	session.add(row4)
	session.commit()

def craeteRiskDataTable(session):
	row1 = RiskData(riskId=1,insurerId=1,fields="Name",typeId=1)
	row2 = RiskData(riskId=1,insurerId=1,fields="Age",typeId=2)
	row3 = RiskData(riskId=1,insurerId=1,fields="Adress",typeId=1)
	row4 = RiskData(riskId=2,insurerId=1,fields="Country",typeId=1)
	session.add(row1)
	session.add(row2)
	session.add(row3)
	session.add(row4)
	session.commit()


def createDB(session):
	createRiskTable(session)
	createInsurerTable(session)	
	createFieldTable(session)
	craeteRiskDataTable(session)
	session.commit()


# class RiskData(Base):
#     __tablename__ = "riskData"
#     uid = Column(Integer, ForeignKey("insurer.id"), primary_key=True)
#     fields = Column(String(10), primary_key=True)
#     typeId = Column(Integer, ForeignKey("field.type_id"))
#     order = Column(Integer)


session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
s = session()

createDB(s)
s.commit()
print "done"

# r = Risk(risk_type="House")
# s = session()
# s.add(r)


# r = Risk(risk_type="Car")
# s.add(r)

# #i = Insurer(insurer_name="Honda",risk_id=1)
# # s.add(i)

# f = Field(type="TEXT")
# s.add(f)
# s.commit()
# print s.query(Insurer).all()

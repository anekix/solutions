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

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Insurer(Base):
    __tablename__ = "insurer"
    id = Column(Integer, primary_key=True)
    insurer_name = Column(String(10))
    risk_id = Column(Integer, ForeignKey('risk.risk_id'))


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

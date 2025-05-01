# sqlalchemy

```python
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db", echo=True)
Base = declarative_base()

class Table00(Base):
    __tablename__ = 'table00'

    column00 = Column(Integer, primary_key=True)
    column01 = Column(String)
    column02 = Column(Integer)

class Table01(Base):
    __tablename__ = 'table01'

    column00 = Column(Integer, primary_key=True)
    column01 = Column(String)
    column02 = Column(Integer)

class Table02(Base):
    __tablename__ = 'table02'

    column00 = Column(Integer, primary_key=True)
    column01 = Column(String)
    column02 = Column(Integer)

# CREATE
Base.metadata.create_all(engine)

# DB Session
Session = sessionmaker(bind=engine)
session = Session()

# INSERT
session.add( Table00(column00 = 0, column01 = "Hello", column02 = 0) )
session.add( Table00(column00 = 1, column01 = "Sql", column02 = 1) )
session.add( Table00(column00 = 2, column01 = "Alchemy", column02 = 2) )
session.commit()

# UPDATE
row = session.query(Table00).filter_by(column01="Hello").first()
if row:
    row.column02 = 2
    session.commit()

# DELETE
row = session.query(Table00).filter_by(column01="Sql").first()
if row:
    session.delete(row)
    session.commit()

# SELECT
rows = session.query(Table00).all()
for row in rows:
    print(row.column00, row.column01, row.column02)
```


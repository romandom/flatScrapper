import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost/flats_db")
print(DATABASE_URL)

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()

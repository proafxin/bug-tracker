from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from tracker.config.settings import DBHOST, DBNAME, DBPASSWORD, DBPORT, DBUSER

url = f"mysql+pymysql://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBNAME}"
engine = create_engine(url=url)

Session = sessionmaker(bind=engine, autoflush=False)


BaseModel = declarative_base()


def get_db():
    db = Session()

    try:
        yield db
    finally:
        db.close()

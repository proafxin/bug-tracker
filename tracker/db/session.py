from tracker.config.settings import DBUSER, DBPASSWORD, DBHOST, DBPORT, DBNAME

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


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

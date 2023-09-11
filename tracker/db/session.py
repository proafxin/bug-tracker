from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from tracker.config.settings import DBHOST, DBNAME, DBPASSWORD, DBPORT, DBUSER

url = f"mysql+aiomysql://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBNAME}"
engine = create_async_engine(url=url)

Session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


BaseModel = declarative_base()


async def get_db():
    async with Session() as db:
        yield db

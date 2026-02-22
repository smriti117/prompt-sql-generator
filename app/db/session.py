from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from config.settings import env


DATABASE_URL = f"postgresql+asyncpg://{env.db_user}:{env.db_password}@{env.db_host}:{env.db_port}/{env.db_name}"

print(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

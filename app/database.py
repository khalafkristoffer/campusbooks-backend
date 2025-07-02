from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Validate DATABASE_URL exists
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create async SQLAlchemy engine
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)

# Create async session class
SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False
)

Base = declarative_base()

# Async db dependency
async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


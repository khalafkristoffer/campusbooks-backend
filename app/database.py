from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Validate DATABASE_URL exists
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create async SQLAlchemy engine
asyncengine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,  # Remove 'await' here
    echo=False,
    pool_pre_ping=True,
)

# Create async session class
SessionLocal = sessionmaker(
    asyncengine,  # Use 'asyncengine' not 'engine'
    class_=AsyncSession, 
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


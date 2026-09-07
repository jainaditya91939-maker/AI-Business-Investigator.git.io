from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://postgres:miniproject@localhost:5432/ai_business_investigator"

engine = create_engine(DATABASE_URL)
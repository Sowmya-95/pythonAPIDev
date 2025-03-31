from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# postgresql://<username>:password@<ip-address/hostname>/<database-name>
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg.connect(host='localhost', dbname='fastapi',
#                                user='postgres', password='password', row_factory=psycopg.rows.dict_row)
#         cursor = conn.cursor()
#         print('Connected to the database successfully')
#         break
#     except Exception as e:
#         print("Error connecting to the database: ", e)
#         time.sleep(2)

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from pydantic_settings import BaseSettings
# from dotenv import load_dotenv
# import os
#
#
# class Settings(BaseSettings):
#     database_url: str
#
#     class Config:
#         env_file = ".env"
#         env_file_encoding = 'utf-8'
#
# settings = Settings()
#
# engine = create_engine()
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
#
# def get_db():
#     db: Session = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn

# from .config import settings

# class Settings(BaseSettings):
#     DATABASE_URL: PostgresDsn
#
#     model_config = SettingsConfigDict(env_file='.env')
#
# settings = Settings(_env_file='.env')

# class Settings(BaseSettings):
#     DATABASE_URL: PostgresDsn
#
#     class Config:
#         env_file = ".env"
#
# settings = Settings()


# Используем строку подключения из настроек
# engine = create_engine(str('postgresql://postgres:123@213.109.204.3/test_apiv2'))
engine = create_engine(str('postgresql://postgres:123@db:5432/mytestdb'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()




def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

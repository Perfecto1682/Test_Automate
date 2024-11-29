import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Загружаем переменные из файла .env
load_dotenv()

# Получаем URL базы данных
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

# Создаем движок и сессию
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

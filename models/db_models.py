from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date
from data.config import BASE_DIR, DB_NAME
from .choices import Gender

engine = create_engine(f'sqlite:////{BASE_DIR}/{DB_NAME}', echo=True)
Session = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()


class Information(Base):
    __tablename__ = 'telegram_information'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), index=True)
    surname = Column(String(length=255))
    day = Column(Date, nullable=True)
    last_congrat = Column(Date, nullable=True, default=None)
    gender = Column(String, nullable=True, default=Gender.NONE)

    def get_full_name(self):
        return self.name + ' ' + self.surname

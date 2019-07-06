import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,  create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from telegram.ext import Updater, CommandHandler

token = os.getenv('TOKEN', '')
PROXY_URL = os.getenv('PROXY_URL', '')
PROXY_LOGIN = os.getenv('PROXY_LOGIN', '')
PROXY_PASSWORD = os.getenv('PROXY_PASSWORD', '')
PROXY = {'proxy_url': PROXY_URL, 'urllib3_proxy_kwargs': {'username': PROXY_LOGIN, 'password': PROXY_PASSWORD}}


Base = declarative_base()
DBSession = scoped_session(sessionmaker())

dbname = 'sqlite:///sqlalchemy.db'


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))


def init_sqlalchemy(dbname):
    global engine
    engine = create_engine(dbname, echo=False)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)


def registration_user(bot, update):
    username = update.message.from_user.username
    id_telegram = update.message.from_user.id
    new_user = User()
    new_user.name = username
    new_user.id = id_telegram
    DBSession.add(new_user)
    DBSession.commit()


if __name__ == '__main__':
    init_sqlalchemy(dbname)
    mybot = Updater(token, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", registration_user))
    mybot.start_polling()
    mybot.idle()

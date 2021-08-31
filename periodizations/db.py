
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from periodizations.settings import DB_HOST, DB_NAME, DB_PORT, DB_USER

engine = create_engine("postgresql://"
        f"{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
Session = sessionmaker(bind = engine)

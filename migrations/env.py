from logging.config import fileConfig
from alembic import context
from periodizations.models import Base
from periodizations.db import engine

config = context.config

fileConfig(config.config_file_name)
target_metadata = Base.metadata

with engine.connect() as connection:
    context.configure(
                connection = connection, target_metadata = target_metadata
            )
    with context.begin_transaction():
        context.run_migrations()

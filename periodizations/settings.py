
from environs import Env

env = Env()
env.read_env()

DB_HOST= env.str("DB_HOST")
DB_PORT = env.int("DB_PORT")
DB_USER = env.str("DB_USER")
DB_NAME = env.str("DB_NAME")

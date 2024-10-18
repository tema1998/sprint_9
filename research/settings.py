from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Settings(BaseSettings):

    mongo_host: str = Field("127.0.0.1")
    mongo_port: int = Field(27017)
    mongo_db: str = Field("ugc")

    pg_db_name: str = Field()
    pg_db_user: str = Field()
    pg_db_password: str = Field()
    pg_db_host: str = Field()
    pg_db_port: int = Field()

    number_of_entries: int = Field(1000000)

    def get_pg_dsn(self):
        return {
            'dbname': self.pg_db_name,
            'user': self.pg_db_user,
            'password': self.pg_db_password,
            'host': self.pg_db_host,
            'port': self.pg_db_port,
        }

settings = Settings()

from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Settings(BaseSettings):

    mongo_host: str = Field("127.0.0.1")
    mongo_port: int = Field(27017)
    mongo_db: str = Field("ugc")
    number_of_entries: int = Field(1000000)

settings = Settings()
from pydantic_settings import BaseSettings

class settings(BaseSettings):
    mongo_url: str = "mongodb://localhost:27017"
    mongo_database:str = "cinema_web"
    model_config: Settings.ConfigDict = {
        "env_file": ".env", extra
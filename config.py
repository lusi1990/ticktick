import os
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, validator
from pytz import timezone


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True

    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SERVER_NAME: str = ''
    SERVER_HOST: AnyHttpUrl = "http://127.0.0.1:8000"
    SERVER_PORT: int = 8000

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = 'TickTick'

    APP_LOGGER_FILE: str = os.path.join(BASE_DIR, 'log/ticktick.log')

    STATIC_DIR: str = '~/Pictures'
    STATIC_URL: str = '/static/'
    STATICFILES = os.path.join(STATIC_DIR, 'static')
    if not os.path.isdir(STATICFILES):
        os.makedirs(STATICFILES)

    TIMEZONE_LOCAL = timezone('Asia/Shanghai')

    class Config:
        case_sensitive = True


settings = Settings()

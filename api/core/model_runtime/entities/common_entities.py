from typing import Optional

from pydantic import BaseModel


class I18nObject(BaseModel):
    """
    Model class for i18n object.
    """

    en_US: str

    def __init__(self, **data):
        super().__init__(**data)

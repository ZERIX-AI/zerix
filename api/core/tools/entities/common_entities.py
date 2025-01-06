from typing import Optional

from pydantic import BaseModel


class I18nObject(BaseModel):
    """
    Model class for i18n object.
    """

    pt_BR: Optional[str] = None
    en_US: str

    def __init__(self, **data):
        super().__init__(**data)
        if not self.pt_BR:
            self.pt_BR = self.en_US

    def to_dict(self) -> dict:
        return {"en_US": self.en_US, "pt_BR": self.pt_BR}

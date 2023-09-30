from app.models.base import BaseProjectModel
from app.services.constants import MAX_STRING
from sqlalchemy import Column, String, Text


class CharityProject(BaseProjectModel):
    name = Column(String(MAX_STRING), nullable=False, unique=True)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f'< name={self.name}, '
            f'description={self.description} >'
            f'{super().__repr__()}'
        )

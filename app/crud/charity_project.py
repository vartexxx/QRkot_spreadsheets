from typing import Optional, List, Dict

from app.crud.base import CRUDBase
from app.models import CharityProject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDCharityProject(CRUDBase):

    @staticmethod
    async def get_charity_project_id_by_name(
        charity_project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        db_charity_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_project_name
            )
        )
        db_charity_project_id = db_charity_project_id.scalars().first()
        return db_charity_project_id

    @staticmethod
    async def get_projects_by_completion_rate(
        session: AsyncSession
    ) -> List[Dict[str, str]]:
        projects = await session.execute(
            select([CharityProject]).where(CharityProject.fully_invested == 1)
        )
        projects = projects.scalars().all()
        project_list = []
        for project in projects:
            project_list.append({
                'name': project.name,
                'duration': project.close_date - project.create_date,
                'description': project.description
            })
        project_list = sorted(project_list, key=lambda x: x['duration'])
        return project_list


charity_project_crud = CRUDCharityProject(CharityProject)

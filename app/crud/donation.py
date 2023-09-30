from app.crud.base import CRUDBase
from app.models import Donation, User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDDonation(CRUDBase):

    @staticmethod
    async def get_by_user(
            user: User,
            session: AsyncSession
    ):
        donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return donations.scalars().all()


donation_crud = CRUDDonation(Donation)

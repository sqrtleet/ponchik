from typing import Type, TypeVar, Generic, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import InstrumentedAttribute

T = TypeVar("T")


class CRUDService(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    async def get_by_id(self, db: AsyncSession, id_: str | int) -> Optional[T]:
        return await db.get(self.model, id_)

    async def get_by_field(self, db: AsyncSession, field: InstrumentedAttribute, value) -> Optional[T]:
        stmt = select(self.model).where(field == value)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, db: AsyncSession, obj_in: T, commit: bool = True) -> T:
        db.add(obj_in)
        if commit:
            await db.commit()
        else:
            await db.flush()
        return obj_in

    async def delete(self, db: AsyncSession, db_obj: T, commit: bool = True) -> None:
        await db.delete(db_obj)
        if commit:
            await db.commit()

    async def update(self, db: AsyncSession, db_obj: T, data: dict, commit: bool = True) -> T:
        for field, value in data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        if commit:
            await db.commit()
        return db_obj

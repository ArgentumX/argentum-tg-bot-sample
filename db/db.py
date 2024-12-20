import datetime
from typing import List

import sqlalchemy as sa
from aiogram import Dispatcher
from gino import Gino
from loguru import logger

from config import config

logger.info("Creating gino instance")
db = Gino()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True
    created_at = db.Column(db.DateTime(True), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=db.func.now(),
    )


async def create_tables():
    await db.gino.create_all()
    logger.info("Created all tables")


async def drop_all():
    await db.gino.drop_all()
    logger.info("Dropped all tables")


async def recreate_db():
    await drop_all()
    await create_tables()


async def on_startup(dispatcher: Dispatcher):
    logger.info("Setup PostgreSQL Connection")
    await db.set_bind(config.POSTGRES_URI)
    await create_tables()


async def on_shutdown(dispatcher: Dispatcher):
    bind = db.pop_bind()
    if bind:
        logger.info("Close PostgreSQL Connection")
        await bind.close()


def setup(dp: Dispatcher):
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

# type: ignore
"""Populate client_types table

Revision ID: 1275bab53041
Revises: 4f4c3bd0de96
Create Date: 2025-04-03 13:46:06.606648

"""

import warnings
from typing import TYPE_CHECKING

import sqlalchemy as sa
from alembic import op
from advanced_alchemy.types import EncryptedString, EncryptedText, GUID, ORA_JSONB, DateTimeUTC
from sqlalchemy import Text  # noqa: F401

from app.api.enums.client_type import ClientType
from app.core.db.models.sqlalchemy_models import ClientTypeModel

if TYPE_CHECKING:
    from collections.abc import Sequence

__all__ = ["downgrade", "upgrade", "schema_upgrades", "schema_downgrades", "data_upgrades", "data_downgrades"]

sa.GUID = GUID
sa.DateTimeUTC = DateTimeUTC
sa.ORA_JSONB = ORA_JSONB
sa.EncryptedString = EncryptedString
sa.EncryptedText = EncryptedText

# revision identifiers, used by Alembic.
revision = '1275bab53041'
down_revision = '4f4c3bd0de96'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        with op.get_context().autocommit_block():
            schema_upgrades()
            data_upgrades()


def downgrade() -> None:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        with op.get_context().autocommit_block():
            data_downgrades()
            schema_downgrades()


def schema_upgrades() -> None:
    """schema upgrade migrations go here."""
    pass


def schema_downgrades() -> None:
    """schema downgrade migrations go here."""
    pass


def data_upgrades() -> None:
    op.bulk_insert(
        ClientTypeModel.__table__,
        [
            {"type": ClientType.REGULAR},
            {"type": ClientType.STUDENT},
            {"type": ClientType.LARGE_FAMILY},
            {"type": ClientType.PENSIONER},
        ]
    )
    """Add any optional data upgrade migrations here!"""


def data_downgrades() -> None:
    """Add any optional data downgrade migrations here!"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.models.sqlalchemy_models import ClientModel, TrainerModel
from app.api.enums.client_type import ClientType
from app.api.schemas.client import Client
from app.api.schemas.trainer import Trainer
from app.api.services.client_service import ClientService
from app.api.services.trainer_service import TrainerService
from litestar.exceptions import HTTPException


@pytest.fixture
def fake_db():
    return AsyncMock(spec=AsyncSession)


@pytest.mark.asyncio
async def test_create_client_from_dto(fake_db):
    service = ClientService()
    dto = Client(
        last_name="Никифоров",
        first_name="Сергей",
        phone_number="+79142383220",
        client_type=ClientType.STUDENT,
        is_active=True,
    )
    fake_db.scalar.return_value = MagicMock()

    result = await service.create_from_dto(fake_db, dto)

    fake_db.add.assert_called_once()
    assert isinstance(result, ClientModel)


@pytest.mark.asyncio
async def test_get_client_success(fake_db):
    service = ClientService()
    mock_client = MagicMock(spec=ClientModel)
    fake_db.get.return_value = mock_client

    result = await service.get_client(fake_db, "uuid")
    assert result is mock_client


@pytest.mark.asyncio
async def test_get_client_not_found(fake_db):
    service = ClientService()
    fake_db.get.return_value = None

    with pytest.raises(HTTPException) as exc:
        await service.get_client(fake_db, "uuid")

    assert exc.value.status_code == 404


@pytest.mark.asyncio
async def test_update_client(fake_db):
    service = ClientService()
    mock_client = MagicMock(spec=ClientModel)
    fake_db.get.return_value = mock_client

    updated = await service.update_client(fake_db, "uuid", {"bonus": 100})
    assert updated is not None
    assert fake_db.commit.called


@pytest.mark.asyncio
async def test_delete_client(fake_db):
    service = ClientService()
    mock_client = MagicMock(spec=ClientModel)
    fake_db.get.return_value = mock_client

    await service.delete_client(fake_db, "uuid")
    fake_db.delete.assert_called_once()


@pytest.mark.asyncio
async def test_create_trainer_from_dto(fake_db):
    service = TrainerService()
    dto = Trainer(
        last_name="Захаров",
        first_name="Вячеслав",
        phone_number="+791422387654",
        is_active=True,
    )
    result = await service.create_from_dto(fake_db, dto)
    fake_db.add.assert_called_once()
    assert isinstance(result, TrainerModel)


@pytest.mark.asyncio
async def test_get_trainer_not_found(fake_db):
    service = TrainerService()
    fake_db.get.return_value = None

    with pytest.raises(HTTPException) as exc:
        await service.get_trainer(fake_db, 1)

    assert exc.value.status_code == 404


@pytest.mark.asyncio
async def test_update_trainer(fake_db):
    service = TrainerService()
    mock_trainer = MagicMock(spec=TrainerModel)
    fake_db.get.return_value = mock_trainer

    updated = await service.update_trainer(fake_db, 1, {"is_active": False})
    assert updated is not None
    assert fake_db.commit.called


@pytest.mark.asyncio
async def test_delete_trainer(fake_db):
    service = TrainerService()
    mock_trainer = MagicMock(spec=TrainerModel)
    fake_db.get.return_value = mock_trainer

    await service.delete_trainer(fake_db, 1)
    fake_db.delete.assert_called_once()

@pytest.mark.asyncio
async def test_update_client_not_found(fake_db):
    service = ClientService()
    fake_db.get.return_value = None

    with pytest.raises(HTTPException) as exc:
        await service.update_client(fake_db, "uuid", {"bonus": 100})

    assert exc.value.status_code == 404


@pytest.mark.asyncio
async def test_get_trainer_success(fake_db):
    service = TrainerService()
    mock_trainer = MagicMock(spec=TrainerModel)
    fake_db.get.return_value = mock_trainer

    result = await service.get_trainer(fake_db, 1)
    assert result is mock_trainer


@pytest.mark.asyncio
async def test_update_trainer_not_found(fake_db):
    service = TrainerService()
    fake_db.get.return_value = None

    with pytest.raises(HTTPException) as exc:
        await service.update_trainer(fake_db, 1, {"is_active": True})

    assert exc.value.status_code == 404


@pytest.mark.asyncio
async def test_create_client_duplicate_phone(fake_db):
    service = ClientService()
    dto = Client(
        last_name="Никифоров",
        first_name="Сергей",
        phone_number="+79142383220",
        client_type=ClientType.STUDENT,
        is_active=True,
    )
    fake_db.scalar.return_value = ClientModel()

    with pytest.raises(HTTPException) as exc:
        await service.create_from_dto(fake_db, dto)

    assert exc.value.status_code == 400
from litestar import post, get, Router

from litestar.status_codes import *

from litestar.dto import DTOData

from ..schemas.client import *

from app.core.db.models.sqlalchemy_models import ClientModel


class ClientController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO

    @post('')
    async def create_client(self, data: DTOData[Client], db_session) -> int:
        client = data.create_instance()
        db_session.add(client)
        await db_session.commit()
        return HTTP_201_CREATED

    @get('/{client_id:int}')
    def get_client(self, client_id: int, db_session) -> Client:
        client_model = db_session.query(ClientModel).get(client_id)
        if not client_model:
            from litestar.exceptions import NotFoundException
            raise NotFoundException(f'Client with id \'{client_id}\' not found')
        return client_model


client_router = Router(path='/clients', route_handlers=[ClientController])

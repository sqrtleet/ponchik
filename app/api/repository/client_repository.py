from sqlalchemy.orm import Session
from models.client import Client
from schemas.Client import ClientInput, ClientOutput
from typing import List, Optional, Type
from uuid import UUID

class ClientRepository:

    def __init__(self, session: Session):
        self.session = session
    
    def create(self, data: ClientInput) -> ClientOutput:
        region = Client(**data.model_dump(exclude_none=True))
        self.session.add(client)
        self.session.commit()
        self.session.refresh(client)
        return ClientOutput(id=client.id, name=client.name)

    def get_all(self) -> List[Optional[ClientOutput]]:
        clients = self.session.query(Client).all()
        return [ClientOutput(**client.__dict__) for client in clients]

    def get_client(self, _id: UUID) -> ClientOutput:
        client = self.session.query(Client).filter_by(id=_id).first()
        return ClientOutput(**client.__dict__)

    def get_by_id(self, _id: UUID) -> Type[Client]:
        return self.session.query(Client).filter_by(id=_id).first()

    def client_exists_by_id(self, _id: UUID) -> bool:
        client = self.session.query(Client).filter_by(id=_id).first()
        return client is not None

    def client_exists_by_name(self, name: str) -> bool:
        client = self.session.query(Client).filter_by(name=name).first()
        return client is not None

    def update(self, client: Type[Client], data: ClientInput) -> ClientInput:
        client.name = data.name
        self.session.commit()
        self.session.refresh(client)
        return ClientInput(**client.__dict__)

    def delete(self, client: Type[Client]) -> bool:
        self.session.delete(client)
        self.session.commit()
        return True
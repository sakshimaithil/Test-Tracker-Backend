
from models import Client
def create_client(db, data):
    client = Client(**data.dict())

    try:
        db.add(client)
        db.commit()
        db.refresh(client)
        return client

    except Exception as e:
        db.rollback()
        raise e


def get_clients(db):
    return db.query(Client).all()
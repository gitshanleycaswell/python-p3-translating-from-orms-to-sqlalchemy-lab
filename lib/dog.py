from models import Dog, Base
from sqlalchemy import create_engine, and_

from sqlalchemy.orm import sessionmaker


def create_table(Base, engine):
    
    engine = create_engine('sqlite:///dogs.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    

def save(session, dog):
    session.bulk_save_objects([dog])
    session.commit()

def get_all(session):
    all_dogs = session.query(Dog).all()
    return all_dogs

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name).first()
    return query

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id).first()
    return query

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(and_(Dog.name == name, Dog.breed == breed)).first()
    return query

def update_breed(session, dog, breed):
    session.query(Dog).update({Dog.breed: breed})
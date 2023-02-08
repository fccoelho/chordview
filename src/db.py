from sqlalchemy import create_engine


def get_engine():
    db = create_engine("sqlite:///../leadsheets.sqlite")
    return db

def _inspect_db():
    pass

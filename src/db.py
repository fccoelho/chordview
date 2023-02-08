from sqlalchemy import create_engine, text
import os

curpath = os.getcwd()
if curpath.endswith(('src', 'tests')):
    dbpath = '../leadsheets.sqlite'
else:
    dbpath = 'leadsheets.sqlite'


def get_engine():
    eng = create_engine(f"sqlite:///{dbpath}")
    assert _inspect_db(eng)
    return eng


def _inspect_db(eng=None):
    engine = eng if eng is not None else get_engine()
    with engine.begin() as conn:
        res = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
        tables = res.fetchall()
    return len(tables) > 0

from db import get_engine
from sqlalchemy import text

def search_song(query: str=''):
    if not query:
        sql = "SELECT title from song"
    else:
        sql = f"SELECT title from song where title like '%{query}%'"
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text("PRAGMA case_sensitive_like=OFF;"))
        res = conn.execute(text(sql))
        titles = res.fetchall()
    return titles

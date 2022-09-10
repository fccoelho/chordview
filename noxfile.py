import nox
from glob import glob

@nox.session
def lint(session):
    session.install("black")
    for f in glob("src/*.py"):
        session.run("black", f)
from sqlmodel import SQLModel, create_engine, Session
from sqlmodel.pool import StaticPool

# Para prod/local: usa archivo
DATABASE_URL = "sqlite:///./library.db"
engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

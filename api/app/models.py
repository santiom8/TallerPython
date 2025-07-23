from sqlmodel import SQLModel, Field

class Book(SQLModel, table=True):
    id:       int    = Field(default=None, primary_key=True)
    name:     str
    price:    float
    pages:    int
    author:   str
    is_sold:  bool   = False

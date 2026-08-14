from pydantic import BaseModel

class TransactionCreate(BaseModel):
    description: str
    amount: float
    type: str # receita ou despesa
    category_id: int 

class TransactionUpdate(BaseModel):
    description: str
    amount: float
    type: str
    category_id: int

class CategoryCreate(BaseModel):
    name: str
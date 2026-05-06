# validação de dados para criação de transações
from pydantic import BaseModel

# Modelo de como os dados devem chegar na API para criar uma transação
class TransactionCreate(BaseModel):
    description: str
    amount: float
    type: str # receita ou despesa
    category_id: int 

# Modelo para atualizar uma transação existente
class TransactionUpdate(BaseModel):
    description: str
    amount: float
    type: str
    category_id: int

# 
class CategoryCreate(BaseModel):
    name: str
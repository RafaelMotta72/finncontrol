from sqlalchemy import Column, Float, Integer, String, ForeignKey # Importando os tipos de dados SQLAlchemy
from .database import Base

# importando o relacionamento entre tabelas, para que seja possivel categorização.
from sqlalchemy.orm import relationship

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    amount = Column(Float)
    type = Column(String)

    category_id = Column(Integer, ForeignKey("categories.id")) # Chave estrangeira para a tabela de categorias(cada transacação agora aponta pra uma categoria)

    category = relationship("Category", back_populates="transactions")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    type = Column(String)  # "receita" ou "despesa"

    transactions = relationship("Transaction", back_populates="category")
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, Base, SessionLocal
from app import models, schemas
from fastapi import HTTPException

# Cria a API usando FastAPI
app = FastAPI()

# cria tabelas no banco automaticamente
Base.metadata.create_all(bind=engine)

# Define o que a rota raiz ("/") deve retornar, se feito um método GET 
@app.get("/")
def read_root():
    return {"mensagem": "API rodando com banco de dados!"}

# Função para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar uma nova transação (CRUD - Create)
@app.post("/transactions")
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):

    category = db.query(models.Category).filter(models.Category.id == transaction.category_id).first()

    if not category:
        raise HTTPException(status_code=400, detail="Categoria inválida")

    new_transaction = models.Transaction(
        description=transaction.description,
        amount=transaction.amount,
        type=transaction.type,
        category_id=transaction.category_id
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction

# Rota para listar todas as transações (CRUD - Read)
@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()

    result = []
    for t in transactions:
        result.append({
            "id": t.id,
            "description": t.description,
            "amount": t.amount,
            "type": t.type,
            "category": t.category.name if t.category else None
        })

    return result


# Rota para atualizar uma transação por ID (CRUD - Update)
@app.put("/transactions/{transaction_id}")
def update_transaction(
    transaction_id: int,
    updated_data: schemas.TransactionUpdate,
    db: Session = Depends(get_db)
):

    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    transaction.description = updated_data.description
    transaction.amount = updated_data.amount
    transaction.type = updated_data.type

    db.commit()
    db.refresh(transaction)

    return transaction


# Rota para deletar uma transação por ID (CRUD - Delete)
@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):

    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    db.delete(transaction)
    db.commit()

    return {"mensagem": "Transação deletada com sucesso"}

# Criação de categorias personalizadas
@app.post("/categories")
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):

    new_category = models.Category(name=category.name)

    existing = db.query(models.Category).filter(models.Category.name == category.name).first()

    if existing:
        raise HTTPException(status_code=400, detail="Categoria já existe")

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

def create_default_categories(db: Session):
    default_categories = ["alimentação", "transporte", "lazer"]

    for name in default_categories:
        exists = db.query(models.Category).filter(models.Category.name == name).first()
        if not exists:
            db.add(models.Category(name=name))

    db.commit()

# listar categorias criadas
@app.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


@app.on_event("startup")
def startup():
    db = SessionLocal()
    create_default_categories(db)
    db.close()
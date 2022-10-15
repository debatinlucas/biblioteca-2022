from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from exceptions import UsuarioException, EmprestimoException, LivroException, ItemEmprestimoException
from database import get_db, engine
import crud, models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# usuário

@app.get("/usuarios/{usuario_id}")
def get_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/usuarios", response_model=schemas.PaginatedUsuario)
def get_all_usuarios(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_usuarios = crud.get_all_usuarios(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_usuarios}
    return response

@app.post("/usuarios", response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_usuario(db, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_usuario(db, usuario_id, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/usuarios/{usuario_id}")
def delete_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

# livro

@app.get("/livros/{livro_id}")
def get_livro_by_id(livro_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_livro_by_id(db, livro_id)
    except LivroException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/livros", response_model=schemas.PaginatedLivro)
def get_all_livros(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_livros = crud.get_all_livros(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_livros}
    return response

@app.post("/livros", response_model=schemas.Livro)
def create_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_livro(db, livro)
    except LivroException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/livros/{livro_id}", response_model=schemas.Livro)
def update_livro(livro_id: int, livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_livro(db, livro_id, livro)
    except LivroException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/livros/{livro_id}")
def delete_livro_by_id(livro_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_livro_by_id(db, livro_id)
    except LivroException as cie:
        raise HTTPException(**cie.__dict__)


# empréstimo

@app.post("/emprestimos", response_model=schemas.Emprestimo)
def create_emprestimo(emprestimo: schemas.EmprestimoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_emprestimo(db, emprestimo)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/emprestimos/{emprestimo_id}")
def get_emprestimo_by_id(emprestimo_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_emprestimo_by_id(db, emprestimo_id)
    except EmprestimoException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/emprestimos", response_model=schemas.PaginatedEmprestimo)
def get_all_emprestimos(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_emprestimos = crud.get_all_emprestimos(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_emprestimos}
    return response

@app.put("/emprestimos/{emprestimo_id}", response_model=schemas.Emprestimo)
def update_emprestimo(emprestimo_id: int, emprestimo: schemas.EmprestimoUpdate, db: Session = Depends(get_db)):
    return crud.update_emprestimo(db, emprestimo_id, emprestimo)

# item empréstimo

@app.post("/itens-emprestimo", response_model=schemas.ItemEmprestimo)
def create_item_emprestimo(item_emprestimo: schemas.ItemEmprestimoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_item_emprestimo(db, item_emprestimo)
    except LivroException as cie:
        raise HTTPException(**cie.__dict__)
    except EmprestimoException as cie:
        raise HTTPException(**cie.__dict__)
    except ItemEmprestimoException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/itens-emprestimo/{emprestimo_id}/{livro_id}")
def delete_item_emprestimo_by_id(emprestimo_id: int, livro_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_item_emprestimo_by_id(db, emprestimo_id, livro_id)
    except ItemEmprestimoException as cie:
        raise HTTPException(**cie.__dict__)

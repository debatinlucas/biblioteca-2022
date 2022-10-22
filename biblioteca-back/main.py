from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from exceptions import UsuarioException, EmprestimoException, LivroException, ItemEmprestimoException
from database import get_db, engine
import crud, models, schemas
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# login
@app.post("/signup", tags=["usuario"])
async def create_usuario_signup(usuario: schemas.UsuarioCreate = Body(...), db: Session = Depends(get_db)):
    try:
        crud.create_usuario(db, usuario)
        return signJWT(usuario.email)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.post("/login", tags=["usuario"])
async def user_login(usuario: schemas.UsuarioLoginSchema = Body(...), db: Session = Depends(get_db)):
    if crud.check_usuario(db, usuario):
        return signJWT(usuario.email)
    return {
        "error": "E-mail ou senha incorretos!"
    }

# usuário

@app.get("/usuarios/{usuario_id}", dependencies=[Depends(JWTBearer())])
def get_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/usuarios", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedUsuario)
def get_all_usuarios(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_usuarios = crud.get_all_usuarios(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_usuarios}
    return response

@app.post("/usuarios", dependencies=[Depends(JWTBearer())], response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_usuario(db, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/usuarios/{usuario_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_usuario(db, usuario_id, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/usuarios/{usuario_id}", dependencies=[Depends(JWTBearer())])
def delete_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

# livro

@app.get("/livros/{livro_id}", dependencies=[Depends(JWTBearer())])
def get_livro_by_id(livro_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_livro_by_id(db, livro_id)
    except LivroException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/livros", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedLivro)
def get_all_livros(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_livros = crud.get_all_livros(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_livros}
    return response

@app.post("/livros", dependencies=[Depends(JWTBearer())], response_model=schemas.Livro)
def create_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_livro(db, livro)
    except LivroException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/livros/{livro_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Livro)
def update_livro(livro_id: int, livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_livro(db, livro_id, livro)
    except LivroException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/livros/{livro_id}", dependencies=[Depends(JWTBearer())])
def delete_livro_by_id(livro_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_livro_by_id(db, livro_id)
    except LivroException as cie:
        raise HTTPException(**cie.__dict__)


# empréstimo

@app.post("/emprestimos", dependencies=[Depends(JWTBearer())], response_model=schemas.Emprestimo)
def create_emprestimo(emprestimo: schemas.EmprestimoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_emprestimo(db, emprestimo)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/emprestimos/{emprestimo_id}", dependencies=[Depends(JWTBearer())])
def get_emprestimo_by_id(emprestimo_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_emprestimo_by_id(db, emprestimo_id)
    except EmprestimoException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/emprestimos", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedEmprestimo)
def get_all_emprestimos(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_emprestimos = crud.get_all_emprestimos(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_emprestimos}
    return response

@app.put("/emprestimos/{emprestimo_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Emprestimo)
def update_emprestimo(emprestimo_id: int, emprestimo: schemas.EmprestimoUpdate, db: Session = Depends(get_db)):
    return crud.update_emprestimo(db, emprestimo_id, emprestimo)

# item empréstimo

@app.post("/itens-emprestimo", dependencies=[Depends(JWTBearer())], response_model=schemas.ItemEmprestimo)
def create_item_emprestimo(item_emprestimo: schemas.ItemEmprestimoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_item_emprestimo(db, item_emprestimo)
    except LivroException as cie:
        raise HTTPException(**cie.__dict__)
    except EmprestimoException as cie:
        raise HTTPException(**cie.__dict__)
    except ItemEmprestimoException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/itens-emprestimo/{emprestimo_id}/{livro_id}", dependencies=[Depends(JWTBearer())])
def delete_item_emprestimo_by_id(emprestimo_id: int, livro_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_item_emprestimo_by_id(db, emprestimo_id, livro_id)
    except ItemEmprestimoException as cie:
        raise HTTPException(**cie.__dict__)

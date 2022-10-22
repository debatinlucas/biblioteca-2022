
from sqlalchemy.orm import Session
from sqlalchemy import and_
from exceptions import UsuarioAlreadyExistError, UsuarioNotFoundError, EmprestimoNotFoundError, LivroNotFoundError, ItemEmprestimoAlreadyExistError, ItemEmprestimoNotFoundError
import models, schemas

# usuário

def check_usuario(db: Session, usuario: schemas.UsuarioLoginSchema):
    db_usuario = db.query(models.Usuario).filter(and_(models.Usuario.email == usuario.email, models.Usuario.senha == usuario.senha)).first()
    if db_usuario is None:
        return False
    return True

def get_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = db.query(models.Usuario).get(usuario_id)
    if db_usuario is None:
        raise UsuarioNotFoundError
    return db_usuario

def get_all_usuarios(db: Session, offset: int, limit: int):
    return db.query(models.Usuario).offset(offset).limit(limit).all()

def get_usuario_by_email(db: Session, usuario_email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == usuario_email).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = get_usuario_by_email(db, usuario.email)
    if db_usuario is not None:
        raise UsuarioAlreadyExistError
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioCreate):
    db_usuario = get_usuario_by_id(db, usuario_id)
    db_usuario.nome = usuario.nome
    db_usuario.email = usuario.email
    if usuario.senha is not "":
        db_usuario.senha = usuario.senha
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = get_usuario_by_id(db, usuario_id)
    db.delete(db_usuario)
    db.commit()
    return

# livro

def get_livro_by_id(db: Session, livro_id: int):
    db_livro = db.query(models.Livro).get(livro_id)
    if db_livro is None:
        raise LivroNotFoundError
    return db_livro

def get_all_livros(db: Session, offset: int, limit: int):
    return db.query(models.Livro).offset(offset).limit(limit).all()

def create_livro(db: Session, livro: schemas.LivroCreate):
    db_livro = models.Livro(**livro.dict())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro

def update_livro(db: Session, livro_id: int, livro: schemas.LivroCreate):
    db_livro = get_livro_by_id(db, livro_id)
    db_livro.titulo = livro.titulo
    db_livro.resumo = livro.resumo
    db.commit()
    db.refresh(db_livro)
    return db_livro

def delete_livro_by_id(db: Session, livro_id: int):
    db_livro = get_livro_by_id(db, livro_id)
    db.delete(db_livro)
    db.commit()
    return

# empréstimo

def create_emprestimo(db: Session, emprestimo: schemas.EmprestimoCreate):
    get_usuario_by_id(db, emprestimo.id_usuario)
    db_emprestimo = models.Emprestimo(**emprestimo.dict())
    db.add(db_emprestimo)
    db.commit()
    db.refresh(db_emprestimo)
    return db_emprestimo

def get_emprestimo_by_id(db: Session, emprestimo_id: int):
    db_emprestimo = db.query(models.Emprestimo).get(emprestimo_id)
    if db_emprestimo is None:
        raise EmprestimoNotFoundError
    return db_emprestimo

def get_all_emprestimos(db: Session, offset: int, limit: int):
    return db.query(models.Emprestimo).offset(offset).limit(limit).all()

def update_emprestimo(db: Session, emprestimo_id: int, emprestimo: schemas.EmprestimoUpdate):
    db_emprestimo = get_emprestimo_by_id(db, emprestimo_id)
    db_emprestimo.status = emprestimo.status
    db.commit()
    db.refresh(db_emprestimo)
    return db_emprestimo

# item empréstimo

def create_item_emprestimo(db: Session, item_emprestimo: schemas.ItemEmprestimoCreate):
    get_emprestimo_by_id(db, item_emprestimo.id_emprestimo)
    get_livro_by_id(db, item_emprestimo.id_livro)

    db_item_emprestimo = get_item_emprestimo_by_ids_create(db, item_emprestimo.id_emprestimo, item_emprestimo.id_livro)
    if db_item_emprestimo is not None:
        raise ItemEmprestimoAlreadyExistError

    db_item_emprestimo = models.ItemEmprestimo(**item_emprestimo.dict())
    db.add(db_item_emprestimo)
    db.commit()
    db.refresh(db_item_emprestimo)
    return db_item_emprestimo

def delete_item_emprestimo_by_id(db: Session, id_emprestimo: int, id_livro: int):
    db_item_emprestimo = get_item_emprestimo_by_ids(db, id_emprestimo, id_livro)
    db.delete(db_item_emprestimo)
    db.commit()
    return

def get_item_emprestimo_by_ids_create(db: Session, id_emprestimo: int, id_livro: int):
    return db.query(models.ItemEmprestimo).filter(and_(models.ItemEmprestimo.id_emprestimo == id_emprestimo, models.ItemEmprestimo.id_livro == id_livro)).first()

def get_item_emprestimo_by_ids(db: Session, id_emprestimo: int, id_livro: int):
    db_item_emprestimo = db.query(models.ItemEmprestimo).filter(and_(models.ItemEmprestimo.id_emprestimo == id_emprestimo, models.ItemEmprestimo.id_livro == id_livro)).first()
    if db_item_emprestimo is None:
        raise ItemEmprestimoNotFoundError
    return db_item_emprestimo
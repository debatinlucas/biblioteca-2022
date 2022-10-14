
from sqlalchemy.orm import Session
from exceptions import UsuarioAlreadyExistError, UsuarioNotFoundError, EmprestimoNotFoundError
import models, schemas

# usuário

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

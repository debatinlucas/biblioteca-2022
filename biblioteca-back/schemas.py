from datetime import date
from typing import List
from pydantic import BaseModel

class EmprestimoBase(BaseModel):
    id_usuario: int
    status: int
    data_retirada: date
class EmprestimoUpdate(BaseModel):
    status: int
class EmprestimoCreate(EmprestimoBase):
    pass
class Emprestimo(EmprestimoBase):
    id: int
    class Config:
        orm_mode = True

class PaginatedEmprestimo(BaseModel):
    limit: int
    offset: int
    data: List[Emprestimo]

class UsuarioBase(BaseModel):
    nome: str
    email: str
class UsuarioCreate(UsuarioBase):
    senha: str
class Usuario(UsuarioBase):
    id: int
    emprestimos: List[Emprestimo] = []
    class Config:
        orm_mode = True

class PaginatedUsuario(BaseModel):
    limit: int
    offset: int
    data: List[Usuario]

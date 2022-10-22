from datetime import date
from typing import List
from pydantic import BaseModel

class LivroBase(BaseModel):
    titulo: str
    resumo: str
class LivroCreate(LivroBase):
    pass
class Livro(LivroBase):
    id: int
    class Config:
        orm_mode = True

class PaginatedLivro(BaseModel):
    limit: int
    offset: int
    data: List[Livro]

class ItemEmprestimoBase(BaseModel):
    id_livro: str
    id_emprestimo: str
class ItemEmprestimoCreate(ItemEmprestimoBase):
    pass
class ItemEmprestimo(ItemEmprestimoBase):
    pass
    class Config:
        orm_mode = True

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
    itens_emprestimo: List[ItemEmprestimo] = []
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
class UsuarioLoginSchema(BaseModel):
    email: str
    senha: str
    class Config:
        schema_extra = {
            "example": {
                "email": "x@x.com",
                "senha": "pass"
            }
        }

class PaginatedUsuario(BaseModel):
    limit: int
    offset: int
    data: List[Usuario]

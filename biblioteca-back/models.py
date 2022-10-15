from sqlalchemy import SmallInteger, Date, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150))
    email = Column(String(150), unique=True, index=True)
    senha = Column(String(255))
    emprestimos = relationship("Emprestimo", back_populates="usuario")

class Emprestimo(Base):
    __tablename__ = 'emprestimos'
    
    id = Column(Integer, primary_key=True, index=True)
    data_retirada = Column(Date)
    status = Column(SmallInteger)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario", back_populates="emprestimos")
    itens_emprestimo = relationship("ItemEmprestimo", back_populates="emprestimo")

class Livro(Base):
    __tablename__ = 'livros'
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150))
    resumo = Column(String(1000))
    itens_emprestimo = relationship("ItemEmprestimo", back_populates="livro")

class ItemEmprestimo(Base):
    __tablename__ = "itens_emprestimo"

    id_livro = Column(Integer, ForeignKey('livros.id'), primary_key=True, nullable=False)
    id_emprestimo = Column(Integer, ForeignKey('emprestimos.id'), primary_key=True, nullable=False)
    livro = relationship("Livro", back_populates="itens_emprestimo")
    emprestimo = relationship("Emprestimo", back_populates="itens_emprestimo")

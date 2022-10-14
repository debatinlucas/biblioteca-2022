from sqlalchemy import SmallInteger, Date, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150))
    email = Column(String(150), unique=True, index=True)
    senha = Column(String(255))
    emprestimos = relationship('Emprestimo', back_populates='usuario')

class Emprestimo(Base):
    __tablename__ = 'emprestimos'
    
    id = Column(Integer, primary_key=True, index=True)
    data_retirada = Column(Date)
    status = Column(SmallInteger)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship('Usuario', backref='usuario')

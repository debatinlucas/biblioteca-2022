class UsuarioException(Exception):
    ...

class UsuarioNotFoundError(UsuarioException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Usuário não encontrado"


class UsuarioAlreadyExistError(UsuarioException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Usuário já cadastrado"

class EmprestimoException(Exception):
    ...

class EmprestimoNotFoundError(EmprestimoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Empréstimo não encontrado"

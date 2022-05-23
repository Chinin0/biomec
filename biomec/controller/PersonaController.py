from ..models.entidades.Persona import Persona 
from ..database import persona_db

# usuario de tipo USER que tendra como resultado de tipo User
def create(persona: Persona) -> Persona:
    # falta implementar los metodos de validacion asi que hay que ingresar datos correctos sino genera error
    return persona_db.create(persona)


def update(persona: Persona) -> Persona:
    return persona_db.update(persona)


def delete(persona: Persona) -> Persona:
    return persona_db.delete(persona)

#Devuelve lista completa 
def list():
    return persona_db.list_all()        


def existe(field: str, value: str) -> bool:
    return persona_db.user_existe(field,value)


def get_persona(field: str, value: str) -> Persona:
    return persona_db.obtener_persona(field,value)
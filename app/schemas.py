from pydantic import BaseModel, ConfigDict

class FilmeBase(BaseModel):
    titulo: str
    diretor: str
    ano: int

class FilmeCreate(FilmeBase):
    pass

class Filme(FilmeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    def to_dict(self):
        return self.model_dump()

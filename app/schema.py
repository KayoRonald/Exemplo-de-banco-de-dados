from typing import Union, Optional
from pydantic import BaseModel

class Item(BaseModel):
  id: Optional[str]
  nome: str
  descricao: Union[str, None] = None
  valor: float
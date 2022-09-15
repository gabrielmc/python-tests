from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Model
class Carga(BaseModel):
    nome: str
    carga: str
    data: Optional[datetime] = datetime
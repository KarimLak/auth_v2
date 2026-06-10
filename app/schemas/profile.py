from enum import Enum
from typing import List
from pydantic import BaseModel, Field

class Sector(Enum):
    contruction: str = "construction"
    service: str = "service"

class ContractType(Enum):
    bien: str = "bien"
    service: str = "service"

class BuisnessProfile(BaseModel):
    name: str = Field(..., max_length=255)
    sector: Sector
    expertise: List[str]
    contract_nature: List[ContractType]
    region: str
    size: int = Field(..., le=0, ge=10000)
    budget_min: int = Field(..., le=0, ge=10000000)
    budget_max: int = Field(..., le=0, ge=10000000)
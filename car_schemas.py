
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field as PydanticField


class GetCarsInput(BaseModel):
    brand: Optional[str] = PydanticField(None, description="A marca do carro (ex: 'Toyota')")
    model: Optional[str] = PydanticField(None, description="O modelo do carro (ex: 'Corolla')")
    fabrication_year: Optional[str] = PydanticField(None, description="O ano de fabricação do carro (ex: '2023')")
    color: Optional[str] = PydanticField(None, description="A cor do carro (ex: 'Vermelho')")
    min_price: Optional[Decimal] = PydanticField(None, description="Preço mínimo do carro")
    max_price: Optional[Decimal] = PydanticField(None, description="Preço máximo do carro")
    min_power_hp: Optional[int] = PydanticField(None, description="Potência mínima do carro (HP)")
    max_power_hp: Optional[int] = PydanticField(None, description="Potência máxima do carro (HP)")
    fuel_type: Optional[str] = PydanticField(None, description="Tipo de combustível (ex: 'Gasolina', 'Flex')")
    transmission: Optional[str] = PydanticField(None, description="Tipo de transmissão (ex: 'Manual', 'Automática')")
    car_type: Optional[str] = PydanticField(None, description="Tipo de carro (ex: 'Sedan', 'SUV', 'Hatchback')")

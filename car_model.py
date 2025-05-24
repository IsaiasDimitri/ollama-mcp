from typing import Optional
from sqlmodel import SQLModel, Field
from decimal import Decimal

class Car(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    brand: str
    model: str
    fabrication_year: str
    model_year: Optional[str] = None
    engine: str
    version: str
    custom_package: Optional[str] = None
    number_of_doors: int
    color: str
    current_km: Decimal
    price: Decimal
    fuel_type: str
    transmission: str
    transmission_name: str
    steering: str
    power_hp: int
    car_type: str
    plate: str

    def __str__(self):
        year = f"{self.fabrication_year}/{self.model_year}" if self.model_year else f"{self.fabrication_year}"
        car = f"{self.brand} {self.model} {self.custom_package} {year}" if self.custom_package else f"{self.brand} {self.model} {year}"
        return car
    
    def to_dict(self):
        return {
            "id": self.id,
            "brand": self.brand,
            "model": self.model,
            "fabrication_year": self.fabrication_year,
            "model_year": self.model_year,
            "engine": self.engine,
            "version": self.version,
            "custom_package": self.custom_package,
            "number_of_doors": self.number_of_doors,
            "color": self.color,
            "current_km": str(self.current_km),
            "price": str(self.price),
            "fuel_type": self.fuel_type,
            "transmission": self.transmission,
            "transmission_name": self.transmission_name,
            "steering": self.steering,
            "power_hp": self.power_hp,
            "car_type": self.car_type,
            "plate": self.plate,
        }
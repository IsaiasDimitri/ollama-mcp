from decimal import Decimal
import os
from typing import List

from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel, Field as PydanticField

from car_model import Car
from car_schemas import GetCarsInput
from db import create_db_and_tables, engine

class CarDatabaseTool:
    """
    Uma ferramenta para consultar carros no banco de dados.
    """
    name: str = "CarDatabaseTool"
    description: str = "Fornece funções para consultar dados de carros no banco de dados, buscando por marca, modelo, ano, cor, preço, potência, tipo de combustível, transmissão ou tipo de carro."

    def __init__(self):
        self.engine = engine 

    def get_cars(self, input_data: GetCarsInput) -> List[dict]:
        """
        Recupera carros do banco de dados com base em vários critérios.
        """
        with Session(self.engine) as session:
            statement = select(Car)
            if input_data.brand:
                statement = statement.where(Car.brand.ilike(f"%{input_data.brand}%"))
            if input_data.model:
                statement = statement.where(Car.model.ilike(f"%{input_data.model}%"))
            if input_data.fabrication_year:
                statement = statement.where(Car.fabrication_year == input_data.fabrication_year)
            if input_data.color:
                statement = statement.where(Car.color.ilike(f"%{input_data.color}%"))
            if input_data.min_price:
                statement = statement.where(Car.price >= input_data.min_price)
            if input_data.max_price:
                statement = statement.where(Car.price <= input_data.max_price)
            if input_data.min_power_hp:
                statement = statement.where(Car.power_hp >= input_data.min_power_hp)
            if input_data.max_power_hp:
                statement = statement.where(Car.power_hp <= input_data.max_power_hp)
            if input_data.fuel_type:
                statement = statement.where(Car.fuel_type.ilike(f"%{input_data.fuel_type}%"))
            if input_data.transmission:
                statement = statement.where(Car.transmission.ilike(f"%{input_data.transmission}%"))
            if input_data.car_type:
                statement = statement.where(Car.car_type.ilike(f"%{input_data.car_type}%"))

            cars = session.exec(statement).all()
            return [car.to_dict() for car in cars]

if __name__ == "__main__":
    create_db_and_tables()
    
    with Session(engine) as session:
        if not session.exec(select(Car)).first():
            car1 = Car(
                brand="Toyota", model="Corolla", fabrication_year="2020", 
                engine="2.0L Dynamic Force", version="XEi", custom_package=None, 
                number_of_doors=4, color="Vermelho", current_km=Decimal('45000.00'), 
                price=Decimal('85000.00'), fuel_type="Flex", 
                transmission="Automática", transmission_name="Direct Shift CVT", 
                steering="Elétrica", power_hp=177, car_type="Sedan", plate="XYZ5678"
            )
            car2 = Car(
                brand="Honda", model="Civic", fabrication_year="2022", 
                engine="2.0L i-VTEC", version="Sport", custom_package=None, 
                number_of_doors=4, color="Azul", current_km=Decimal('28000.00'), 
                price=Decimal('110000.00'), fuel_type="Gasolina", 
                transmission="Automática", transmission_name="CVT", 
                steering="Elétrica", power_hp=158, car_type="Sedan", plate="ABC9012"
            )
            car3 = Car(
                brand="Ford", model="Mustang", fabrication_year="2023", 
                engine="5.0L V8", version="GT Premium", custom_package=None, 
                number_of_doors=2, color="Vermelho", current_km=Decimal('5000.00'), 
                price=Decimal('350000.00'), fuel_type="Gasolina", 
                transmission="Automática", transmission_name="10R80", 
                steering="Elétrica", power_hp=460, car_type="Esportivo", plate="DEF3456"
            )
            
            session.add(car1)
            session.add(car2)
            session.add(car3)
            session.commit()

    tool_instance = CarDatabaseTool()
    red_cars_input = GetCarsInput(color="Vermelho")
    red_cars = tool_instance.get_cars(red_cars_input)
    for car_dict in red_cars: 
        print(Car(**car_dict))
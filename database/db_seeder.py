import json
import random
from faker import Faker
from sqlmodel import Session

from models.car_model import Car


faker = Faker("pt_BR")

def generate_fake_car():
    brands_models = {
        "Toyota": ["Corolla", "Hilux", "Etios"],
        "Honda": ["Civic", "Fit", "HR-V"],
        "Ford": ["Ka", "Focus", "EcoSport"],
        "Chevrolet": ["Onix", "Cruze", "S10"],
        "Volkswagen": ["Golf", "Polo", "T-Cross"]
    }
    brand = random.choice(list(brands_models.keys()))
    model = random.choice(brands_models[brand])
    return {
        "brand": brand,
        "model": model,
        "fabrication_year": str(random.randint(2010, 2022)),
        "model_year": str(random.randint(2010, 2023)),
        "engine": random.choice(["1.0", "1.4", "1.6", "2.0", "2.2"]),
        "version": random.choice([None, "Standard", "Comfortline", "Highline", "XEi", "GLI"]),
        "custom_package": random.choice([None, "Black Pack", "Tech Edition", "Premium"]),
        "number_of_doors": random.choice([2, 4]),
        "color": faker.color_name(),
        "current_km": float(round(random.uniform(10000, 150000), 2)),
        "price": float(round(random.uniform(30000, 150000), 2)),
        "fuel_type": random.choice(["Gasolina", "Etanol", "Diesel", "Flex"]),
        "transmission": random.choice(["Manual", "Automático Convencional", "Automatizado", "CVT"]),
        "steering": random.choice(["Hidráulica", "Elétrica", "Mecânica"]),
        "power_hp": random.randint(70, 200),
        "car_body_type": random.choice(["Hatch", "Sedan", "SUV", "Pickup"])
    }

def generate_json_file(path: str, num_records: int = 100):
    cars = [generate_fake_car() for _ in range(num_records)]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cars, f, indent=2, ensure_ascii=False)

def insert_cars_from_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        cars_data = json.load(f)
    with Session(engine) as session:
        for car_dict in cars_data:
            car = Car(**car_dict)
            session.add(car)
        session.commit()
    print(f"Inseridos {len(cars_data)} carros no banco.")
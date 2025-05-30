CREATE TABLE IF NOT EXISTS cars (
    id SERIAL PRIMARY KEY,
    brand TEXT,
    model TEXT,
    color TEXT,
    engine_type TEXT,
    transmission_type TEXT,
    fuel_type TEXT
);

INSERT INTO cars (brand, model, color, engine_type, transmission_type, fuel_type) VALUES
('Volkswagen', 'Clio', 'Black', 'I4', 'Manual', 'Gasoline'),
('Renault', 'Rio', 'Blue', 'V6', 'Manual', 'Gasoline'),
('Honda', 'Sentra', 'Green', 'Hybrid', 'Automatic', 'Diesel'),
('Kia', 'Golf', 'Blue', 'Electric', 'Manual', 'Diesel'),
('Hyundai', 'Focus', 'Green', 'Electric', 'Automatic', 'Gasoline'),
('Chevrolet', 'Sentra', 'Green', 'Hybrid', 'Manual', 'Gasoline'),
('Peugeot', 'Clio', 'Red', 'Hybrid', 'Manual', 'Electric'),
('Renault', 'Golf', 'Blue', 'I4', 'Automatic', 'Hybrid'),
('Chevrolet', 'Golf', 'Yellow', 'V6', 'Manual', 'Electric'),
('Volkswagen', 'Elantra', 'Red', 'V6', 'Automatic', 'Gasoline'),
('Honda', 'Civic', 'Blue', 'Electric', 'Manual', 'Hybrid'),
('Peugeot', 'Rio', 'Black', 'Electric', 'Automatic', 'Hybrid'),
('Nissan', 'Focus', 'Red', 'Hybrid', 'Automatic', 'Diesel'),
('Hyundai', 'Civic', 'Silver', 'Electric', 'Automatic', 'Electric'),
('Volkswagen', 'Golf', 'Gray', 'Hybrid', 'Automatic', 'Diesel'),
('Honda', 'Focus', 'Green', 'Hybrid', 'Manual', 'Electric'),
('Volkswagen', 'Golf', 'Yellow', 'V6', 'Automatic', 'Electric'),
('Toyota', 'Civic', 'Red', 'V6', 'Automatic', 'Gasoline'),
('Peugeot', 'Focus', 'Blue', 'I4', 'Manual', 'Diesel'),
('Kia', 'Golf', 'Silver', 'V8', 'Automatic', 'Diesel'),
('Ford', 'Golf', 'Black', 'Hybrid', 'Manual', 'Hybrid'),
('Renault', 'Elantra', 'Yellow', 'V6', 'Automatic', 'Diesel'),
('Peugeot', 'Cruze', 'Green', 'Electric', 'Automatic', 'Electric'),
('Toyota', 'Golf', 'Red', 'V6', 'Manual', 'Diesel'),
('Chevrolet', 'Rio', 'Green', 'Electric', 'Manual', 'Electric'),
('Kia', 'Focus', 'White', 'I4', 'Automatic', 'Diesel'),
('Toyota', 'Golf', 'White', 'Hybrid', 'Manual', 'Electric'),
('Ford', 'Cruze', 'Silver', 'V6', 'Manual', 'Electric'),
('Hyundai', 'Golf', 'Red', 'Electric', 'Manual', 'Electric'),
('Honda', 'Golf', 'Black', 'V6', 'Manual', 'Gasoline'),
('Toyota', 'Civic', 'Red', 'I4', 'Manual', 'Hybrid'),
('Chevrolet', 'Cruze', 'Yellow', 'V6', 'Automatic', 'Gasoline'),
('Kia', 'Focus', 'White', 'Hybrid', 'Automatic', 'Gasoline'),
('Volkswagen', 'Focus', 'Silver', 'Hybrid', 'Manual', 'Hybrid'),
('Ford', 'Clio', 'White', 'I4', 'Automatic', 'Diesel'),
('Kia', 'Civic', 'Silver', 'I4', 'Automatic', 'Gasoline'),
('Nissan', 'Focus', 'Silver', 'I4', 'Manual', 'Electric'),
('Toyota', 'Golf', 'White', 'Hybrid', 'Automatic', 'Gasoline'),
('Honda', 'Clio', 'Blue', 'V8', 'Manual', 'Electric'),
('Renault', '208', 'Gray', 'I4', 'Automatic', 'Electric'),
('Volkswagen', 'Golf', 'Blue', 'V6', 'Manual', 'Gasoline'),
('Honda', 'Focus', 'Black', 'Electric', 'Automatic', 'Diesel'),
('Peugeot', 'Golf', 'Gray', 'Electric', 'Manual', 'Diesel'),
('Chevrolet', 'Civic', 'Silver', 'V8', 'Automatic', 'Hybrid'),
('Nissan', 'Golf', 'Red', 'I4', 'Manual', 'Hybrid'),
('Toyota', 'Focus', 'Silver', 'V8', 'Manual', 'Diesel'),
('Peugeot', 'Civic', 'Yellow', 'I4', 'Manual', 'Electric'),
('Honda', 'Golf', 'Black', 'I4', 'Automatic', 'Diesel'),
('Kia', 'Golf', 'Green', 'V6', 'Manual', 'Diesel'),
('Nissan', 'Golf', 'Blue', 'V8', 'Manual', 'Diesel'),
('Volkswagen', 'Cruze', 'Blue', 'Hybrid', 'Manual', 'Electric'),
('Renault', 'Sentra', 'Green', 'I4', 'Automatic', 'Gasoline'),
('Peugeot', 'Golf', 'Yellow', 'Electric', 'Manual', 'Hybrid'),
('Honda', 'Clio', 'Green', 'I4', 'Automatic', 'Diesel'),
('Hyundai', '208', 'Black', 'Hybrid', 'Manual', 'Diesel'),
('Toyota', 'Cruze', 'White', 'V8', 'Manual', 'Diesel'),
('Nissan', '208', 'White', 'I4', 'Automatic', 'Hybrid'),
('Ford', 'Golf', 'Silver', 'Electric', 'Manual', 'Diesel'),
('Peugeot', '208', 'Gray', 'Electric', 'Manual', 'Gasoline'),
('Toyota', 'Golf', 'Red', 'Hybrid', 'Automatic', 'Electric'),
('Honda', 'Civic', 'Blue', 'Electric', 'Automatic', 'Gasoline'),
('Kia', 'Golf', 'Red', 'V8', 'Manual', 'Hybrid'),
('Nissan', 'Golf', 'Red', 'Hybrid', 'Automatic', 'Diesel'),
('Renault', 'Clio', 'Blue', 'V8', 'Manual', 'Hybrid'),
('Hyundai', '208', 'Yellow', 'V8', 'Manual', 'Electric'),
('Honda', 'Cruze', 'Red', 'V6', 'Manual', 'Electric'),
('Kia', 'Elantra', 'Silver', 'Electric', 'Manual', 'Diesel'),
('Toyota', 'Civic', 'Blue', 'V6', 'Manual', 'Diesel'),
('Peugeot', 'Rio', 'White', 'V6', 'Manual', 'Diesel'),
('Volkswagen', '208', 'Blue', 'I4', 'Automatic', 'Diesel'),
('Chevrolet', 'Golf', 'Green', 'I4', 'Automatic', 'Electric'),
('Renault', 'Elantra', 'Green', 'Electric', 'Manual', 'Gasoline'),
('Volkswagen', 'Golf', 'Yellow', 'Electric', 'Automatic', 'Electric'),
('Toyota', 'Golf', 'White', 'V8', 'Manual', 'Gasoline'),
('Ford', '208', 'Black', 'Hybrid', 'Automatic', 'Diesel'),
('Nissan', 'Clio', 'Green', 'Electric', 'Manual', 'Electric'),
('Chevrolet', 'Golf', 'Silver', 'Hybrid', 'Automatic', 'Diesel'),
('Volkswagen', 'Cruze', 'Green', 'Electric', 'Manual', 'Diesel'),
('Honda', 'Civic', 'Silver', 'Hybrid', 'Manual', 'Gasoline'),
('Hyundai', 'Golf', 'Yellow', 'I4', 'Manual', 'Hybrid'),
('Peugeot', 'Golf', 'Red', 'V8', 'Manual', 'Hybrid'),
('Kia', '208', 'Blue', 'Hybrid', 'Manual', 'Electric'),
('Renault', 'Golf', 'Black', 'Electric', 'Automatic', 'Diesel'),
('Nissan', 'Rio', 'Green', 'I4', 'Manual', 'Diesel'),
('Toyota', 'Elantra', 'White', 'Electric', 'Automatic', 'Diesel'),
('Hyundai', 'Golf', 'Red', 'V6', 'Manual', 'Hybrid'),
('Peugeot', 'Elantra', 'Green', 'V8', 'Manual', 'Hybrid'),
('Ford', '208', 'Silver', 'Hybrid', 'Manual', 'Gasoline'),
('Honda', '208', 'Gray', 'I4', 'Manual', 'Electric'),
('Volkswagen', 'Clio', 'White', 'V6', 'Automatic', 'Diesel'),
('Toyota', '208', 'Green', 'Hybrid', 'Manual', 'Gasoline'),
('Kia', 'Golf', 'White', 'Electric', 'Automatic', 'Hybrid'),
('Ford', 'Cruze', 'Yellow', 'I4', 'Automatic', 'Electric'),
('Renault', 'Golf', 'Red', 'Hybrid', 'Manual', 'Gasoline'),
('Chevrolet', '208', 'Green', 'I4', 'Automatic', 'Diesel'),
('Peugeot', 'Civic', 'Black', 'V6', 'Automatic', 'Hybrid'),
('Hyundai', 'Rio', 'Gray', 'Electric', 'Manual', 'Diesel');


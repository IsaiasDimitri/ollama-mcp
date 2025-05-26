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
('Toyota', 'Corolla', 'White', 'I4', 'Automatic', 'Gasoline'),
('Ford', 'Focus', 'Black', 'I4', 'Manual', 'Diesel'),
('Chevrolet', 'Cruze', 'Blue', 'V6', 'Automatic', 'Gasoline');

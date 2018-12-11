-- Item Table
create table items (id INTEGER PRIMARY KEY, name VARCHAR(50),category_id INTEGER, production_year VARCHAR(50), price DECIMAL(8,2), condition VARCHAR(4), created_by VARCHAR(50) );

-- Category Table
create table categories ( id INT, name VARCHAR(50) );

-- Category Items
INSERT INTO categories (id, name) VALUES (1, 'Land Rover');
INSERT INTO categories (id, name) VALUES (2, 'Cadillac');
INSERT INTO categories (id, name) VALUES (3, 'Kia');
INSERT INTO categories (id, name) VALUES (4, 'BMW');
INSERT INTO categories (id, name) VALUES (5, 'Chevrolet');
INSERT INTO categories (id, name) VALUES (6, 'Porsche');
INSERT INTO categories (id, name) VALUES (7, 'Acura');
INSERT INTO categories (id, name) VALUES (8, 'Mercury');
INSERT INTO categories (id, name) VALUES (9, 'Honda');
INSERT INTO categories (id, name) VALUES (10, 'Volkswagen');
INSERT INTO categories (id, name) VALUES (11, 'Mitsubishi');
INSERT INTO categories (id, name) VALUES (12, 'Dodge');
INSERT INTO categories (id, name) VALUES (13, 'Cadillac');
INSERT INTO categories (id, name) VALUES (14, 'Lincoln');
INSERT INTO categories (id, name) VALUES (15, 'Mazda');
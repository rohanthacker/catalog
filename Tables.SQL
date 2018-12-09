create table categories ( id INT, name VARCHAR(50) );

create table items ( name VARCHAR(50),category_id INT, production_year VARCHAR(50), price DECIMAL(8,2), condition VARCHAR(4), created_by VARCHAR(50) );
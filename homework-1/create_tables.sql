-- SQL-команды для создания таблиц
create table employees
(
	employee_id int primary key,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	title varchar(100) not null,
	birth_date date not null,
	notes text
);

create table customers
(
	customer_id varchar(20) primary key,
	company_name text not null,
	contact_name varchar(50)
);

create table orders
(
	order_id int primary key,
	customer_id varchar(20) references customers(customer_id) not null,
	employee_id int references employees(employee_id) not null,
	order_date date,
	ship_city varchar(50) not null
);

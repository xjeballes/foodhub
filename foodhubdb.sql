CREATE TABLE IF NOT EXISTS customer (
 user_id int(11) primary key auto_increment,
 firstname varchar(20),
 lastname varchar(20),
 gender varchar(15),
 username varchar(20),
 email varchar(30),
 password varchar (20),
 contact_number varchar(12)
);

CREATE TABLE IF NOT EXISTS owner (
 owner_id int(11) primary key auto_increment,
 firstname varchar(20),
 lastname varchar(20),
 gender varchar(15),
 username varchar(20),
 email varchar(30),
 password varchar (20),
 contact_number varchar(12)
);

CREATE TABLE IF NOT EXISTS restaurant(
restaurant_id int primary key auto_increment,
restaurant_name varchar(30),
restaurant_type varchar(30),
bio varchar(200),
locations varchar(50)

);

CREATE TABLE IF NOT EXISTS menu(
menu_id int primary key,
price int(5),
item varchar(30),
cat_id int,
index cat_ind (cat_id),
foreign key (cat_id)
	references category(category_id)

);

CREATE TABLE IF NOT EXISTS images(
image_id int primary key,
customer_image longblob,
restaurant_image longblob,
menu_image longblob

)

CREATE TABLE IF NOT EXISTS booking(
booking_id int primary key auto_increment,
booking_status varchar(20),
booking_date timestamp,
pax_number int (5)

)

CREATE TABLE IF NOT EXISTS category(
category_id int primary key,
category_name varchar(20)

)

CREATE TABLE IF NOT EXISTS reviews(
comments varchar(100),
date date,
star_rating double

)
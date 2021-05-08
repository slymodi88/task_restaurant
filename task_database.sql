create database if not EXISTS loacl2;
use loacl2;
create table Tables(
	table_id int primary key auto_increment,
    table_num int default 0,
    num_seats int default 0
);

create table Reservation(
	reservation_id int primary key AUTO_INCREMENT,
    start_time time,
    end_time time,
    reservation_date  date,   
    FOREIGN KEY fk_reservation_table (reservation_id) REFERENCES Tables(table_id)
    
);

create table WorkingHour(
WorkingHour_id int primary key AUTO_INCREMENT,
    start_day time,
    end_day time
);

create table user(

user_id int primary key AUTO_INCREMENT,
	name varchar(255),
	employee_number varchar(4),
	token varchar(255),
    is_staff boolean default False ,
    is_superuser boolean default False 
);



drop database if exists profile;
create database profile;
use profile;

create table Profile_details
(user_id varchar(64) not null primary key,
name varchar(64) not null,
email varchar(64) not null,
mobile varchar(8) not null,
ratings float default null,
counts int default null);
drop database if exists esdg5t4;
create database esdg5t4;
use esdg5t4;

create table Profile_details
(user_id varchar(64) not null primary key,
name varchar(64) not null,
email varchar(64) not null,
mobile varchar(8) not null,
ratings float default null,
counts int default null);

CREATE DATABASE IF NOT EXISTS payment DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE payment;

create table payment(
	seller_id int unique NOT NULL,
    buyer_id int unique NOT NULL ,
    price float NOT NULL,

    payment_id int unique,
    payment_status Boolean NOT NULL,
    primary key (payment_id));

    
insert into payment 
	(seller_id, buyer_id, price, payment_id, payment_status) 
values 

    (1234, 5678, 2.13, 3245, False),
    (4312, 7865, 3.13, 4567, True),
    (2314, 6578, 4.13, 8765, False);

--     (1234, 5678, 2.13, 9876, False),
--     (4312, 7865, 3.13, 8907, True),
--     (2314, 6578, 4.13, 7809, False);


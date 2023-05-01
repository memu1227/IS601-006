CREATE TABLE
    IS601_Orders(
        id int auto_increment PRIMARY KEY,
        user_id int not null,
        total_price float not null,
        address varchar(240) default null COMMENT  'Address of residence', 
        payment_method varchar (240) default null COMMENT ' Payment type (card,cash,etc)', 
        money_received float not null, 
        first_name varchar(240) default null COMMENT "First Name", 
        last_name varchar(240) default null COMMENT "Last Name",
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
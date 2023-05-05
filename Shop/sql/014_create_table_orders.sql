CREATE TABLE
    IS601_S_Orders(
        id int auto_increment PRIMARY KEY,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id),
        first_name varchar(240) default null COMMENT "First Name", 
        last_name varchar(240) default null COMMENT "Last Name",
        address varchar(240) default null COMMENT  'Address of Residence', 
        number_of_items int,
        total_price int,
        payment_method varchar (240) default null COMMENT ' Payment type (card,cash,etc)', 
        money_received float not null,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
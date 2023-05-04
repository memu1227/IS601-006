ALTER TABLE IS601_S_Orders
ADD
    COLUMN number_of_items int not null default True COMMENT 'Number of Items';
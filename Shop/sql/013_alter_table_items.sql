ALTER TABLE IS601_S_Items
ADD
    COLUMN visibility BOOLEAN not null default True COMMENT 'Visibility column';
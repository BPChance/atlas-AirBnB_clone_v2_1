-- create db if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVELEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- apply changes
FLUSH PRIVELEGES;
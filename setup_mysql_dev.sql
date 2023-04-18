-- Srcipt that prepares a MySQL server for the project it should: 
-- create project development database : hbnb_dev_db
-- create new user : hbnb_dev with all privileges with password: hbnb_dev_pwd if it doesnt exist
-- grant all privilages to new user
-- grant the SELECT privilege to user :hbnb_dev in the db performance_schema

-- Creating database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creating user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Granting all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Granting SELECT prileges
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

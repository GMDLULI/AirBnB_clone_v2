-- This script prepares a MySQL server and should:
-- create project testing for database: hbnb_test_db
-- create new user: hbnb_test with all privileges on the hbnb_test_db database
-- if the user doesnt exist it should have password : hbnb_test_pwd when created
-- granting the SELECT privilege for the user hbnb_test on the db performance_schema
-- granting all priviledges to the user: hbnb_test_db

--create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY hbnb_test_pwd;
-- granting privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

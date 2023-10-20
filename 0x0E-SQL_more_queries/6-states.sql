-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database created
USE hbtn_0d_usa;
-- Create a table in the databse
CREATE TABLE IF NOT EXISTS states(
  id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(256));

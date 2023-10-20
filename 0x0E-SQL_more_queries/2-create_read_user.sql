-- Create a databse hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create a user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant the SELECT priviledge
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

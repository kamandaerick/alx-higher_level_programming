-- create a user user_0d_2 with SELECT priviledges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create a user user_0d_2 with SELECT priviledges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant SELECT on hbtn_0c_0 to user_0d_2
GRANT SELECT ON hbtn_0c_2.* TO 'user_0d_2'@'localhost';

-- Create a user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd'
iGRANT ALL PRIVILEGES ON *. * TO 'user_0d_1'@'%';
FLUSH PRIVILEGES;


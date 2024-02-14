MySQL

This project explains and demonstrate the following:
	
	Set up MySQL User
cat mysql_setup
-- script to create MySQL user on web servers

-- create user if not exist
-- user should should be identified with password projectcorrection280hbtn
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- grant holberton_user permission to check primary/replica status
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

transfer the setup file to the server by the following command
./task_0 mysql_setup.sql 34.201.61.16 ubuntu ~/.ssh/school

Execute the setup file on seperate serever using the following command:
cat mysql_setup.sql | sudo mysql

Create Database called tyrell_corp using the following statement
CREATE DATABASE tyrell_corp;

Activate the created database using the following statement:
USE tyrell_corp;

Then, Create a table with the follpwing schema
CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO nexus6 (name) VALUES ('Leon');

Then, grant permission to the user
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

# 0x14. MySQL
## Learning Objectives
What is the main role of a database
What is a database replica
What is the purpose of a database replica
Why database backups need to be stored in different physical locations
What operation should you regularly perform to make sure that your database backup strategy works

## Tasks
0. Install MySQL
Install MySQL on both your web-01 and web-02 servers. 
Requirement
The MySQL distribution must be 5.7.x. 

1. Let us in!
Create a MySQL user named “holberton_user” on both web-01 and web-02 with the hostname set to “localhost” and the password “projectcorrection280hbtn”.
Requirement
Make sure that holberton_user has permission to check the primary/replica status of your databases

2. If only you could see what I've seen with your eyes
Create a database named “tyrell_corp” on your primary MySQL server (web-01). Within the tyrell_corp database create a table named “nexus6” and add at least one entry to it. 
Requirement
Make sure that holberton_user has SELECT permissions on your table

3. Quite an experience to live in fear, isn't it?
On your primary MySQL server (web-01), create a new user for the replica server. The name of the new user should be “replica_user”, with the hostname set to “%”, and can have whatever password you like. 
Requirements
“replica_user” must have the appropriate permissions to replicate your primary MySQL server.
“holberton_user” will need SELECT privileges on the mysql.user table.

4. Setup a Primary-Replica infrastructure using MySQL
Ensure MySQL primary is hosted on web-01 - do not use the “bind-address”, just comment out this parameter. MySQL replica must be hosted on web-02. Set up replication for the MySQL database named “tyrell_corp”. Provide your MySQL primary configuration and replica configurations as answer files.

5. MySQL backup
Write a Bash script that generates a MySQL dump and creates a compressed archive out of it. 
Requirements
The MySQL dump must contain all your MySQL databases
The MySQL dump must be named “backup.sql”
The MySQL dump file has to be compressed to a “tar.gz” archive
The archive must have the following name format: “day-month-year.tar.gz”
The user to connect to the MySQL database must be “root”
The Bash script accepts one argument which is the password used to connect to the MySQL database.


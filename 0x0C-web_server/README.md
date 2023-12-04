# 0x0C. Web server
## Learning Objectives
How to use scp in shell
How to use curl in shell
What is the main role of a web server
What is a child process
Why web servers usually have a parent process and child processes
What are the main HTTP requests
What is DNS main role

## Tasks
0. Transfer a file to your server
Write a Bash script 0-transfer_file that transfers a file from our client to a server. The script accepts 4 parameters; the path to the file to be transferred, the IP of the server we want to transfer the file to, the username scp connects with, and the path to the SSH private key that scp uses.
Requirements
The script displays “Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY” if less than 3 parameters are passed.
scp must transfer the file to the user home directory ~/
Strict host key checking must be disabled when using scp

1. Install nginx web server
Let’s install a web server. Install nginx on your web-01 server. Nginx should be listening on port 80. When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string “Hello World!”. As an answer file, write a Base script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself).
Requirements
You can’t use systemctl for restarting nginx

2. Setup a domain name
.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Provide the domain name in your answer file.
Requirements
Provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech).
Configure your DNS records with an A entry so that your root domain points to your web-01 IP address Warning: the propagation of your records can take time (~1-2 hours)
Go to your profile and enter your domain in the Project website url field

3. Redirection
Configure your Nginx server so that /redirect_me is redirecting to another page.
Requirements
The redirection must be a “301 Moved Permanently”
You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
Using what you did with “1-install_nginx_web_server”, write “3-redirection” so that it configures a brand new Ubuntu machine to the requirements asked in this task

4. Not found page 404
Configure your Nginx server to have a custom 404 page that contains the string “Ceci n’est pas une page”
Requirements
The page must return and HTTP 404 error code
The page must contain the string “Ceci n’est pas une page”
Using what you did with “3-redirection”, write “4-not_found_page_404” so that it configures a brand new Ubuntu machine to the requirements asked in this task


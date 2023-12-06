# 0x0E. Web stack debugging #1
## Network basics
Networking is a big part of what made computers so powerful and why the internet exists. It allows machines to communicate with each other.

## Tasks
0. Nginx likes port 80
Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

Requirements
Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
Write a Bash script 0-nginx_likes_port_80 that configures a server to the above requirements

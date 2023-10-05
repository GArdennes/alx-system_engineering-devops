0x08. Networking basics #1
Resources
ifconfig
The ifconfig tool is used to manage network interfaces on Unix-like operating systems.
ifconfig - displays a list of all network interfaces and configurations
ifconfig <interface> - displays information about a specific interface
ifconfig <interface> <ip address> - configure an IP address for a network interface 

telnet
The telnet tool is used to establish a text-based connection to a remote server.
telnet <server address> <port number> - establishes connection to remote server


nc
The nc tool is used to determine open ports on a remote server, transfer files from one computer to another in a network and to create a realtime chat with another user in the network.
nc -z <ip address> - port scanning on a remote server
nc -lvp <port number> | cat > myfile.txt - file transfer to remote server
nc -lvp <port number> - create chat application

Learning Objectives
1.What is a localhost/127.0.0.1
2.What is 0.0.0.0
3.What is /etc/hosts
4.How to display your machine’s active network interfaces

Tasks
0. Change your home IP
Write a Bash script that configures an Ubuntu server with the below requirements
Requirements
"Localhost" resolves to "127.0.0.2"
"Facebook.com" resolves to "8.8.8.8"

1. Show attached IPs
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

2. Port listening on localhost
Write a Bash script that listens on port 98 on localhost


# Simple web stack
![Image of a simple web stack](0-simple_web_stack.jpg)
## Description
A user wants to access the website www.foober.com. The user’s browser sends a DNS query to the DNS server for the domain name www.foobar.com. A server is a device, a virtual device or a computer program providing functionality for other programs or devices, called “clients”. A domain name is a human-readable name that is used to identify an IP address on the internet. The DNS server queries the authoritative DNS server for foobar.com. The authoritative DNS server for foobar.com returns the DNS record for www.foobar.com which is an A record containing the IP address 8.8.8.8. The recursive server returns the IP address to the browser. The browser sends an HTTP request to the web server at 8.8.8.8:80. The web server receives the HTTP request and forwards it to the application server. The application server processes the HTTP request and generates a response. The application server forwards the response back to the web server. The web server sends the response back to the browser. The browser displays the response to the user.

## Roles
Nginx is a web server responsible for handling HTTP requests and responses. It is also responsible for serving static files, such as HTML, CSS, and JavaScript files. MySQL is a database that is used to store data for the website. The application server uses MySQL to retrieve and store data for the website. The application server is responsible for processing HTTP requests and generating responses. It is also responsible for interacting with the database to retrieve and store data.

## Issues with this infrastructure
This one-server web infrastructure is sufficient for hosting a small website. In this state it cannot support a lot of traffic, it can be scaled and upgraded to support more traffic. The single web server, single database server and vulnerable internet connection represent SPOFs in the web infrastructure.

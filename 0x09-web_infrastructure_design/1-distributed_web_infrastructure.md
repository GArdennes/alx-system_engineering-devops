# Distributed web infrastructure

![Image of distributed web infrastructure](1-distributed_web_infrastructure.jpg)

## Description
In this infrastructure, the user’s browser sends a DNS query for the domain name www.foobar.com. The DNS server returns the IP address of the load balancer. The user’s browser sends an HTTP request to the load balancer. The load balancer distributes the requests to one of the web servers. The web server receives the request and checks to see if the requested file is a static file. If the requested file is a static file, the web server serves the file directly to the user’s browser else the web server forwards the request to the application server. The application server receives the request and processes it. The application server may interact with the database to retrieve and store data. Once the application server has processed the request, it generates a response. The application server forwards the response back to the web server. The web server sends the response back to the load balancer. The load balancer sends the response back to the user’s browser.

## Roles
1. A server is a device, a virtual device or a computer program providing functionality for other programs or devices, called “clients”. Adding two more allows for load distribution.
2. A web server is software that serves web pages to clients upon their request, it does this over the protocol HTTP. Adding one more for the second server.
3. An application server is a type of server that installs, operates, and hosts applications and associated services for end users, IT services, and organizations. Adding one more for the second server.
4. The load balancer (HAProxy) is a software load balancer that helps the website handle more web traffic and avoid downtime by routing traffic to servers based on an active-active setup.
5. The database server helps retrieve the application files in response to the HTTP request.
6. The application file contains the application's code. The application code is responsible for processing HTTP requests and generating responses.

## Issues with Infrastructure
* Lack of security: The system does not implement a firewall to protect the server from unauthorized access.

* Lack of monitoring tools: The system lacks monitoring tools to help detect problems early on so that corrective action can be taken before outages or security breaches.

## FAQ
* What distribution algorithm your load balancer is configured with and how it works
Round Robin: Round Robin passes each new connection request to the next server in line, eventually distributing connections evenly across the array of machines being load-balanced. Round Robin works well in most configurations but could be better if the equipment that you are load balancing is not roughly equal in processing speed, connection speed, and/or memory.

* Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
The load balancer in this setup uses an active-active setup. In an active-active setup, all of the web servers are active and processing traffic. The load balancer distributes traffic across all of the web servers evenly. While with an active-passive setup, only one of the web servers is active at a time. The other server is on standby mode and ready to take over if the active web server fails.

* How a database Primary-Replica (Master-Slave) cluster works
A database primary-replica cluster is a group of database servers that are synchronized with each other. The primary server is the only server that can accept write operations. The replica servers receive updates from the primary server and maintain a copy of the database.

* What is the difference between the Primary node and the Replica node in regard to the application?
When a user makes a change to the database, the change is sent to the primary server. The primary server then sends the change to the replica servers. If the primary server fails, the replica server is promoted to the primary server.


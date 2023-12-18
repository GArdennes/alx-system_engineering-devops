# 0x13. Firewall
## Background Context
There are two types of firewall strategies, deployment method and inspection method. The deployment method can be categorised as host-based deployment and network-based deployment. While the inspection method can be categorised into packet filtering, stateful inspection, and application level. A firewall is a software or hardware security system. A hardware can be installed between the internet gateway device and the router to act as a security mechanism or a software can be installed on a PC to serve the security purposes.

## Tasks
0. Block all incoming traffic but
Let’s install the ‘ufw’ firewall and setup a few rules on ‘web-01’. Configure ‘ufw’ on ‘web-01’ so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)

## Advanced task
1. Port forwarding
Firewalls can not only filter requests, they can also forward them. Configure ‘web-01’ so that its firewall redirects port 8080/TCP to port 80/TCP. 


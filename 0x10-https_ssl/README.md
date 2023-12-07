# 0x10. HTTPS SSL
## Learning Objectives
What are HTTPS SSL 2 main roles?
What is the purpose of encrypting traffic?
What does SSL termination mean?

## Tasks
0. World wide web
Configure your domain zone so that the subdomain “www” points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

1. HAproxy SSL termination
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypted it and pass it on to its destination. Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain “www”

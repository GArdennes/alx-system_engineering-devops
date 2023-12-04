# 0x0F. Load balancer
## Load balancer
Ever wonder how Facebook, Linkedin, Twitter and other web giants handle such huge amounts of traffic? They don’t have just one server, but tens of thousands. To achieve this, web traffic needs to be distributed to these servers, and that is the role of a load-balancer.

## Web stack debugging
Debugging is about verifying assumptions, in a perfect world the software or system we are working on would be working perfectly, the server is in perfect shape and everybody is happy. But actually, it NEVER goes this way, things ALWAYS fail (it’s tremendous!).

For the machine level, you want to ask yourself these questions:
1. Does the server have free disk space? - command: df
2. Is the server able to keep up with CPU load? - command: w, top, ps
3. Does the server have available memory? - command: free
4. Are the server disk(s) able to keep up with read/write IO? - command: htop

If the answer is no for any of these questions, then that might be the reason why things are not going as expected. There are often 3 ways of solving the issue:
1. free up resources (stop processes or reduce their resource consumption)
2. increase the machine resources (adding memory, CPU, disk space…)
3. distributing the resources usage to other machines

For the machine level, you want to ask yourself these questions:
1 Does the server have the expected network interfaces and IPs up and running? - command: ifconfig
2 Does the server listen on the sockets that it is supposed to? - command: netstat (netstat -lpd or netstat -lpn)
3 Can you connect from the location you want to connect from, to the socket you want to connect to? - command: telnet to the IP + PORT (telnet 8.8.8.8 80)
4 Does the server have the correct firewall rules? iptables, ufw: iptables -L, sudo ufw status

If a piece of Software isn’t behaving as expected, it can obviously be because of above reasons…but the good news is that there is more to look into (there is always more to look into actually).
1. Is the software started? - command: init, init.d, service NAME_OF_THE_SERVICE status, /etc/init.d/NAME_OF_THE_SERVICE status
2. Is the software process running? pgrep, ps, pgrep - lf NAME_OF_THE_PROCESS, ps auxf
3. Is there anything interesting in the logs? Look for log files in /var/log/ and tail -f is your friend

## Tasks
0. Double the number of webservers
In this first task, you need to configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests and to understand and track the way a load balancer works. More in the coming tasks

Configure Nginx so that its HTTP response contains a custom header on web-01 and web-02.
The name of the custom HTTP header must be X-Served-By. The value of the custom HTTP header must be the hostname of the server Nginx is running on.

Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task


1. Install your load balancer
Install and configure HAproxy on your lb-01 server. Configure HAproxy so that it sends traffic to web-01 and web-02. Distribute requests using a round-robin algorithm. 


Requirements
Make sure that HAproxy can be managed via an init script
Make sure that your servers are configured with the right hostnames.
For your answer file 1-install_load_balancer, write a Bash script that configures a new Ubuntu machine to respect the above requirements.

# Secured and monitored web infrastructure

![Image of secured and monitored web infrasture](2-secured_and_monitored_web_infrasture.jpg)

## Roles
* Firewalls: The three firewalls are configured to allow traffic to and from the servers in the infrastructure. The firewalls also block all unauthorized traffic.

* SSL certificate: The SSL certificate is installed on the web server. This allows the website to serve encrypted traffic over HTTPS.

* Monitoring Clients: The three monitoring clients are used to monitor the health and performance of the servers in the infrastructure. The monitoring clients will send alerts if they detect any problems.

## Issues with the infrastructure
* Terminating SSL at the load balancer level
One issue is that terminating SSL at the load balancer level can reduce performance and increase latency. This is because the load balancer needs to decrypt and encrypt all traffic, which can be computationally expensive.

* Having only one MySQL server capable of accepting writes
Another issue is that having only one MySQL server capable of accepting writes is a single point of failure. This means that if the MySQL server fails, the entire website will be unavailable.

* Having servers with all the same components
Another issue is that having servers with all the same components can make it difficult to scale the infrastructure. For example, if all of the servers are running the same software, and one of the servers is overloaded, the other servers may also become overloaded.

## FAQ
1. What are firewalls for?
Firewalls are network security devices that monitor and control incoming and outgoing network traffic based on predetermined security rules. A firewall typically establishes a barrier between a trusted network and an untrusted network, such as the Internet.

2. Why is the traffic served over HTTPS?
Traffic is served over HTTPS for security, integrity and authentication reasons. HTTPS encrypts all traffic between the user’s browser and the website’s server. This helps to protect user data from being intercepted and stolen by attackers. HTTPS ensures that the data that is sent between the user’s browser and the website’s server is not tampered with.

3. How does the monitoring tool, SumoLogic collect data?
The Sumo Logic is a cloud-based log management and analytics platform that is used to collect data from either on-premise servers, cloud-based services or openTelemetry. Once the data is collected, Sumo logic indexes it and makes it available for search and analysis. Users can use Sumo logic to create dashboards and alerts to monitor their systems and applications.

4. Explain what to do if you want to monitor your web server QPS
There are a variety of options to monitor your web server queries per second (QPS). Some options are:
* A web server monitoring tool like HAProxy
* A log management and monitoring tool like Sumo logic
* A cloud monitoring tool like Azure Monitor
Once you have a tool to monitor the QPS, you configure it to collect the data by installing the tool, setting the baselines, setting alerts and utilizing the trend analysis tool.


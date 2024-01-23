# 0x1A. Application server
## Requirements
A README.md file, at the root of the folder of the project, is mandatory
Everything Python-related must be done using python3
All config files must have comments

All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks
0. Set up development with Python
This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.
Requirements:
Make sure that task #3 of your SSH project is completed.
Install net-tools package on your server
Git clone your AirBnB_clone_v2 on your web-01 server
Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port  5000.
Your Flask application object must be named app.

1. Set up production with Gunicorn
Install Gunicorn and any libraries required by your application. Your Flask application object will serve as a WSGI entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.
Requirements
Install Gunicorn and any other libraries required by your application.
The Flask application object should be called app. (This will allow us to run and check your code)
To check your code, make sure nothing is listening to port 6000.

2. Serve a page with Nginx
Based on previous tasks, configure nginx to serve your page from the route /airbnb_onepage/
Requirements
Nginx must serve this page both locally and on its public IP on port 80.
Nginx should proxy requests to the process listening on port 5000
Include your Nginx config file as 2-app_server-nginx_config.
Notes
To test this you’ll have to spin up either your production or development application server (listening on port 5000).
You will probably need to reboot your server (by using the command $ sudo reboot ) to have Nginx publicly accessible.

3. Add a route with query parameters
Based on previous tasks, you’ll need to configure nginx to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001. The key to this exercise is getting nginx configured to proxy requests to process listening on two different ports. You are not expected to keep your application server process running.

Requirements
Nginx must serve this page both locally and on its public IP port 80
Nginx should proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) the process listening on port 5001
Include nginx config file as 3-app_server-nginx_config.

4. Let's do this for your API
Let’s serve what you built for AirBnB clone v3 - RESTful API on web-01
Requirements
Git clone your AirBnB_clone_v3
Setup nginx so that the route /api/ points to a Gunicorn instance listening on port 5002
Nginx must serve this page both locally and on its public IP on port 80
To test your setup you should bind Gunicorn to api/v1/app.py
It may be helpful to import your data form <link: this project>
Upload your nginx config file as 4-app_server-nginx_config

5. Serve your AirBnB clone
Let’s serve what you built for AirBnB clone - Web dynamic on web-01.
Requirements
Git clone your AirBnB_clone_v4
Your Gunicorn instance should serve content from web_dynamic/2-hbnb.py on port 5003
Setup nginx so that the route / points to your Gunicorn instance
Setup nginx so that it properly serves the static assets found in web_dynamic/static/ 
For your website to be fully functional, you will need to reconfigure web_dynamic/static/scripts/2-hbnb.js  to the correct IP.
Nginx must serve this page both locally and on its public IP and port 5003.
Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors.
Upload your nginx config as 5-app_server-nginx_config

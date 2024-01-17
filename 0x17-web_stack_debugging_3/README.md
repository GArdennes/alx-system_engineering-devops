# 0x17. Web stack debugging #3
## Background Context
Wordpress is a top-rated tool, it allows you to run blogs, portfolios, ecommerce and company websites. It powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career. Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), a widely used set of tools. 

The web stack you are supposed to debug today is a wordpress website running on a LAMP stack.

## Requirements
All your files will be interpreted on Ubuntu 14.04 LTS
All your files should end with a new line
A README.md file at the root of the folder of the project is mandatory
Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
Your Puppet manifests must run without error
Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
Your Puppet manifests files must end with the extension .pp
Files will be checked with Puppet v3.4

## Tasks
0. Strace is your friend
Find out why Apache is returning a 500 error using “strace”. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
Hint: “strace” can attach to a current running process. You can use tmux t run strace in one window and “curl” in another one.
Requirements
Your 0-strace_is_your_friend.pp file must contain Puppet code
You can use whatever Pupper resource type you want for your fix.

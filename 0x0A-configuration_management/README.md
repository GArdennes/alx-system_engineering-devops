# 0x0A. Configuration management

## Puppet for Configuration Management

Imagine you are a teacher with a classroom full of students. You want to make sure that all of your students are following the same rules and procedures. You also want to make sure that they are all learning the same material. Puppet is like a teacher for your computer systems. It helps you to make sure that all of your computers are configured the same way and that they are all running the same software.

Puppet is a configuration management tool that helps automate the process of deploying, configuring, managing, and maintaining a machine or a system[4]. It is one of the earliest configuration management tools and has gained a huge community of supporters and users[4]. Puppet works by using a client-server model, where the Puppet master server manages the configuration of the Puppet agent nodes[4]. Puppet uses a declarative language to define the desired state of a system, and then applies that state to the system to ensure it is configured correctly[4]. Puppet is popular in the IT world and is being extensively used by Fortune 500 companies[4]. It has a large community of supporters and users who contribute to writing pre-existing modules that are public and available for anyone to download, install, and use[4].

Citations:
[1]( https://youtube.com/watch?v=oTSLn40YsmA)
[2]( https://en.wikipedia.org/wiki/Puppet)
[3] (https://www.tor.com/2017/03/16/writing-for-dummies-the-art-of-ventriloquism/)
[4] (https://intellipaat.com/blog/tutorial/devops-tutorial/puppet-tutorial/)
[5] (https://jbrary.com/new-to-storytime-using-puppets/)


## Tasks

### Create a file
Using Puppet, create a file 0-create_a_file.pp in /tmp with file permission 0744, file owner www-data, file group is www-data and file contains “I love Puppet”.

### 1. Install a package
Using Puppet, write a file 1-install_a_package.pp that installs flask version 2.1.0 from pip3

### 2. Execute a command
Using Puppet, create a manifest 2-execute_a_command.pp that kills a process named killmenow using pkill and the exec Puppet resource.


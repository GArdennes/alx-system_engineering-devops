# 0x0B. SSH
## Learning Objectives
What is a server
Where do physical servers usually live
What is SSH
How to create an SSH RSA key pair
How to connect to a remote host using an SSH RSA key pair
What is the advantage of using “#!/usr/bin/env bash” instead of “/bin/bash”

## Task
0. Use a private key
Write a Bash script 0-use_a_private_key that uses ssh to connect to your server using the private key “~/.ssh/school” with the user ubuntu using only ssh single-character flags.
Requirements
You do not need to handle the case of a private key protected by a passphrase.

1. Create an SSH key pair
Write a Bash script that creates an RSA key pair. The private key must be named school. The number of bits in the created key must be 4096. The created key must be protected by the passphrase betty.

2. Client configuration file
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
Requirements
Your SSH client configuration must be configured to use the private key ~/.ssh/school
Your SSH client configuration must be configured to refuse to authenticate using a password

3. Let me in!
Now that you have successfully connected to your server, we would also like to join the party. 
Add the SSH public key below to your server so that we can connect using the ubuntu user.


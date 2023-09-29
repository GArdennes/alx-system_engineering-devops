0x05. Processes and signals
Learning Objectives
What is a PID
What is a process
How to find a process’ PID
How to kill a process
What is a signal
What are the 2 signals that cannot be ignored

Tasks
0. What is my PID
Write a Bash script that displays its own PID.

1. List your processes
Write a Bash script that displays a list of currently running processes.
Requirement
Must show all processes, for all users, including those which might not have a TTY
Display in a user-oriented format.
Show process hierarchy

2. Show your Bash PID
Using your previous exercise command, write a Bash script that displays lines containing the “bash” word, thus allowing you to easily get the PID of your Bash process.
Requirement
You cannot use pgrep
The third line of your script must be “# shellcheck disable=SC2009” 

3. Show your Bash PID made easy
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word “bash”
Requirement
You cannot use ps

4. To infinity and beyond
Write a Bash script that displays “To infinity and beyond” indefinitely
Requirement
In between each iteration of the loop, add a “sleep 2”

5. Don't stop me now!
We stopped our “4-to_infinity_and_beyond” process using “ctrl+c” in the previous task, there is actually another way to do this.
Write a Bash script that stops “4-to_infinity_and_beyond” process.
Requirement
You must use “kill”

6. Stop me if you can
Write a Bash script that stops “4-to_infinity_and_beyond” process.
Requirements
You cannot use “kill” or “killall”

7. Highlander
Write a Bash script that displays “To infinity and beyond” indefinitely, with a “sleep 2” in between each iteration. “I am invincible!!!” when receiving a “SIGTERM” signal. 
Make a copy of your “6-stop_me_if_you_can” script, name it “67-stop_me_if_you_can”, that kills the “7-highlander” process instead of the “4-to_infinity_and_beyond” one.

8. Beheaded process
Write a Bash script that kills the process “7-highlander”


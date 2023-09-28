0x04. Loops, conditions and parsing
Learning Objectives
1. How to create SSH keys
2. What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
3. How to use “while”, “until” and “for” loops
4. How to use “if”, “else”, “elif” and “case” condition statements
5. How to use the “cut” command
6. What are files and other comparison operators, and how to use them

Tasks
0. Create a SSH RSA key pair
Create a RSA key pair.
Requirements:
1. Share your public key in your answer file “0-RSA_public_key.pub”
2. Fill the “SSH public key” field of your “intranet profile” with the public key you just generated.
3. Keep the private key in a secure location
4. If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location.

1. For Best School loop
Write a Bash script that displays “Best School” 10 times.
Requirement
1. You must use the “for” loop (“while” and “until” are forbidden)


2. While Best School loop
Write a Bash script that displays “Best school” 10 times.
Requirements:
1. You must use the while loop (for and until are forbidden)


3. Until Best School loop
Write a Bash script that displays “Best School” 10 times.
Requirements
1. You must use the until loop (for and while are forbidden)


4. If 9, say Hi!
Write a Bash script that displays “Best School” 10 times, but for the 9th iteration, displays “Best School” and then “Hi” on a new line.
Requirements
1. You must use the “while” loop (for and until are forbidden)
2. You must use the “if” statement


5. 4 bad luck, 8 is your chance
Write a Bash script that loops from 1 to 10 and:
1. Displays “bad luck” for the 4th loop iteration
2. Displays “good luck” for the 8th loop iteration
3. Displays “Best School” for the other iterations


6. Superstitious numbers
Write a Bash script that displays numbers from 1 to 20 and:
1. Displays 4 and then “bad luck from China” for the 4th loop iteration
2. Displays 9 and then “bad luck from Japan” for the 9th loop iteration
3. Displays 17 and then “bad luck from Italy” for the 17th loop iteration


7. Clock
Write a Bash script that displays the time for 12 hours and 59 minutes:
1. Display hours from 0 to 12
2. Display minutes from 1 to 59


8. For ls
Write a Bash script that displays:
1. The content of the current directory
2. In a list format
3. Where only the part of the name after the first dash is displayed

Requirements
1. You must use the for loop
2. Do not display hidden files


9. To file, or not to file
Write a Bash script that gives you information about the “school” file.
Requirements
1. You must use if and else (case is forbidden)
2. Your Bash script should check if the file exists and print:
	a. If the file exists: “school file exists”
	b. If the file does not exist “school file does not exist”
3. If the file exists, print:
	a. If the file is empty: “school file is empty”
	b. If the file is not empty “school file is not empty”
	c. if the file is a regular file: “school is a regular file”
	d. If the file is not a regular file: (nothing)


10. FizzBuzz
Write a Bash script that displays numbers from 1 to 100.

Requirement
1. Displays FizzBuzz when the number is a multiple of 3 and 5
2. Displays Fizz when the number is a multiple of 3
3. Displays Buzz when the number is a multiple of 5
4. Otherwise, displays the number in a list format


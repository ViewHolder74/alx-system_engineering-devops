Command line for the win


The Project demonstrate the use of the SFTP (Secure File Transfer Protocol) 
command-line tool to move local screenshots to the sandbox environment


HERE ARE THE STEPS TO TRANSFER FILE FROM LOCAL MACHINE TO SANDBOX USING SFTP:


Step 1: Open a terminal or command prompt on your local machine

Step 2: Use the SFTP command-line tool to establish a connection to the sandbox environment
		Copy SFTP link from your sandbox and paste it on your terminal, then go ahead and copy the password

Step 3: Once connected, navigate to the directory where you want to upload the screenshots.
	for instance: /root/alx-system_engineering-devops/command_line_for_the_win/


Step 4: Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment.
	for instance: <shell> put /pictures/screenshots/0-first_9_tasks.jpg


Step 5: Confirm that the screenshots have been successfully transferred by checking the sandbox directory.


Step 6: Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.

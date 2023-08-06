This is a simple extention of some useful python scripts on linux as a package, developed in order to make things easier and faster.

Requirements:

Paramiko

1. getcmd : 

	Description: To get the output of linux commands executed on remote servers easily and quickly.
	Arguments: 
		a. hostname(required): Supply the server name/Ip from which you need to command results.
		b. username(required): usernamre to login to the server.
		c. password(required): password corresponding to the username supplied. 
		d. cmds(required): Commands that need to be executed in the server. You can provide multiple commands to execute(a python list)
		e. filename(optional): If provided, appends the output of each command to filename supplied.



For any suggestions, feedbacks or contibution please visit https://github.com/Adityank003/linuxcmd




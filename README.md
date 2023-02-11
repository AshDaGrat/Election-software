# Election-software

This system is a comprehensive solution for conducting secure and efficient voting over a LAN. Built using a combination of Python, JavaScript, HTML, CSS, and the Eel library. It includes a user-friendly interface, voter ID verification, and results calculation.

<img src="https://cdn.discordapp.com/attachments/1073895599910436915/1073897377997541426/image.png" >

<br>

# Installation
```
git clone https://github.com/AshDaGrat/Election-software
```
```
pip install -r requirements.txt
```
<br>

# Running
## On Server Side:
Edit the data\usn.json file with the voter IDs
<img src="https://cdn.discordapp.com/attachments/1073895599910436915/1073900366011322428/image.png">


Run Server.py and copy the IP address:
<img src="https://cdn.discordapp.com/attachments/1073895599910436915/1073898963746439258/image.png">



## On Client Side:
NOTE : Client and server should be connected to the same LAN

Edit the main.py file with the above IP address 
<img src="https://cdn.discordapp.com/attachments/1073895599910436915/1073899663989673984/image.png">

Run main.py

<br>

# Vote Calculation

data\forfeit.json shows the list of voters who forfeit the election

data\done.json shows the list of voters who voted

data\recd.json shows the complete data of how every voter voted

Run data\counting.py to calculate votes

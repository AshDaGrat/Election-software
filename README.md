# Election-software

This system is a comprehensive solution for conducting secure and efficient voting over a LAN. Built using a combination of Python, JavaScript, HTML, CSS, and the Eel library. It includes a user-friendly interface, voter ID verification, and results calculation.

![image](https://github.com/user-attachments/assets/6437b1c1-3c2f-455f-8e4c-d54bc4f47dcb)

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

![image](https://github.com/user-attachments/assets/d29b0c2c-9701-4373-bbe3-c9c26a63c3ce)


Run Server.py and copy the IP address:

![image](https://github.com/user-attachments/assets/0be23973-8340-41e6-bbf0-b21cb5e353a1)



## On Client Side:
NOTE : Client and server should be connected to the same LAN

Edit the main.py file with the above IP address 

![image](https://github.com/user-attachments/assets/d6f5ed22-769c-44e8-ac64-b247f71930e1)



<b> Run main.py </b>
<br>

# Vote Calculation

data\forfeit.json shows the list of voters who forfeit the election

data\done.json shows the list of voters who voted

data\recd.json shows the complete data of how every voter voted

Run data\counting.py to calculate votes

Project to simulate a DDOS attack and be able to really understand how the attack works and experience what it's like both from the attacker and targets point of view. 

**THIS IS FOR EDUCATIONAL PURPOSES ONLY! REMEMBER TO ALWAYS DO THESE SORT OF THINGS IN A CONTROLLED ENVIRONMENT AND ASK FOR PERMISSION BEFORE DOING ANYTHING. **

**Instructions:** Set up 2 VM's, one simulating the attackers machine and the other one simulating the target machine. Create a Nat Network in the virtual machine provider settings (VirtualBox, VMware...) and then go to the VM's settings and set the Network Adapter on both VM's as a NAT Network using the NAT Network you just created. Use this video to guide you up to this point with VirtualBox: https://www.youtube.com/watch?v=DzmUOeFdc-w

After you set up the NAT Network, host a web server (ex: apache2) on the target machine with the command: `sudo systemctl start apache2` if you don't have apache2 installed, then go ahead and install it with these commands: `sudo apt update` and `sudo apt install apache2`. Make sure both VM's are linux because the commands in this instructions are for linux VM's.

In the target machine go to `/var/www/html` and copy the files on this repo minus the python script for the target webpage. Make sure to use sudo and delete the files in the `/var/www/html` directory before copying the web-page files. On the attacker's machine, open your browser and put the IP of the target machine on the search bar and hit enter. You should see the webpage of the target machine in your attacker machine. 

After all this is done, run the python script using `python3 {srciptName.py}` and input what the script asks. If it asks for a port, give it the port `80` as its the port where the apache2 server is running. Lastly for the IP, input the target machine IP and your DDOS attack is ready. The python script is to automate the DDOS attack for the attacker and the rest of the files are files for the target web-page for the DDOS attack. 

**Bonus:** if you want to see what's happening behind the scenes. Before launching the attack, open wireshark in the target machine, select eth0 as your network capture interface and then run the python script on the attackers machine. As the script executes, watch as all the packets and requests are coming in to the target machine to really see why a DDOS attack does what it does and how it takes web-pages down.

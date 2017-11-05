Item Catalog Application

This application provides a list of items within a variety of categories as well as provide a user authentication system. Users will have the ability to post, edit and delete their own items.
Getting Started

You can clone or download this project via GitHub to your local machine.


Prerequisites
You will need to install these following application in order to make this code work.

1. VirtualBox -> https://www.virtualbox.org/wiki/Downloads
2. Vagrant -> https://www.vagrantup.com/downloads.html


VM configuration
Installing

Unzip the VM configuration and you will find a vagrant folder
Use the Terminal to get into the vagrant folder from VM configuration

run the following command

$ vagrant up


This will cause Vagrant to download the Linux operating system and install it.

After it finished and after the shell prompt comes back, you can run this command

$ vagrant ssh


And this will let you login to the Linux VM. (Please do not shut down the terminal after the login)


Setting up the enviroment

Move the folder you downloaded from GitHub and put it into the vagrant folder use the following line to get into the vagrant VM folder

$ cd /vagrant


Use the command line to get in to the folder you just downloaded

Then you can run this command to setup the database:

$ python database_setup.py


To load the initial database:

$ python videogame_items.py


After it added items succesfully, you can run the following command

$ python application.py


After finish running application.py you can use your favorite browser to visit:

http://localhost:5000


From there, you can view the preloaded items, login and add your own.
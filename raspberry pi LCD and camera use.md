# steps to use Raspberry With LCD display and Camera:
	open Raspberry pi imager
	press cntl+shif+x changer the mdp to the wifi and user name
	continuer with the steps
	upload the os on the sd card
	make ssh empty file
	add config.wpa

# Components :
	raspberry pi
	raspberry pi LCD 3.5 inch
	raspberry pi camera

# Use Putty:
	open putty
	connect to Raspberry  through adress ip of the internet use
	enable vnc
	open vnc viewer (install vnc viewer for pc)


# For LCD Configuration Run:

	sudo rm -rf LCD-show 
	git clone  https://github.com/goodtft/LCD-show.git  
	chmod -R 755 LCD-show 
	cd LCD-show/
	sudo ./LCD35-show


# Create the.py file Run :
	nano run_model.py ;
	paste the code provided or write directly personal code
	python run_model.py



# Test Camera Run:
	libcamera-still -o test.jpg


# Results:
	for running the code provided it create a screen using tkinter library to run raspberry pi camera

# NB:
	Install requirements libraries
	 
	










#red light - green light
#by ghKoty
#WARNING: for playing this game you need YeeLight RGB bulb, turn on LAN control in bulb settings and write correct local IP adress
bulb_ip = "192.168.0.103" #  local IP adress of your YeeLight RGB bulb


#code:
from yeelight import *
from time import sleep
from random import randint
b = Bulb(bulb_ip)
b.auto_on = True
b.effect = "sudden"
b.set_brightness(100)
b.set_rgb(0,0,255)
count = int(input("count of rounds\nwrite 0 for infinity:\n"))
current = 0
while current != count or count == 0:
	b.set_rgb(255,0,0)
	if input("press enter to continue\nor s for exit...\n") == "s":
		print("end")
		b.set_color_temp(4700)
		b.set_brightness(100)
		exit()
	sleep(randint(0,3))
	b.set_rgb(0, 255, 0)
	if randint(0, 5) < 4:
		sleep(randint(1,  2))
		if count != 0:
			current = current + 1
b.set_rgb(255,0,0)
print("end")
sleep(1)
b.set_color_temp(4700)
b.set_brightness(100)
exit()
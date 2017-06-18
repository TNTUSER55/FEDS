import random
import netcat_standby as ns
from Message import m
from time import sleep

        ###This is a (F)ree (E)ncription and (D)ecryption (S)cheme. It You can send and resive messages via netcat.
        #this is ver 1.0
print("This is a (F)ree (E)ncription and (D)ecryption (S)cheme FEDS. It uses Netcat and Python")


def IsInMessageBook(name):
        name1="contact_"+name+".txt"
        messagebook=open(name1, "w+")
        if messagebook.readline() == "":
                message = "What is the ip address of this " + name + "?"
                ip=input(message)
                messagebook.write(ip)
        infoforname = messagebook.read()
        messagebook.seek(0)
        ip=messagebook.readline()
        messagebook.close()
        return ip




def start():

        sleep(.1)
        print("b4 ncat")
        input_=input("Who would like to talk to?")
        IP=IsInMessageBook(input_)
        Message=input("What whould you like to say?")
        m(IP, Message)

ns.nc()
start()

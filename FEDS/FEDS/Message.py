from subprocess import call             #importing subprocess
import time                             #importing time
import sys                              #importing sys
def m(ip, me):                          #making a function

    st="nc " + ip + " 6666 > " + me     #creating the statment
    call(st,shell=True)              #running that statment in nc

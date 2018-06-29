#!/usr/bin/env python3
from pexpect import pxssh
import getpass
import threading
import subprocess
from subprocess import call
import time

#simulation time in seconds
try:
    t_sim = int(sys.argv[1])
except:
    t_sim = 7*60


##########################################
#       Starting server script           #
##########################################
#Node 9: server
#interface='eth5'

def connect_to_node(number=9):
    try:
        #Connecting to the chosen node
        s = pxssh.pxssh()
        hostname = "10.10.2." + str(number)
        username = "nas"
        password = "naslab"
        s.login(hostname, username, password)
        return s

    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)
        return 0

def server_func(t_sim, t_parse):
    s = connect_to_node(9);

    s.sendline('cd simone_scripts/')    # run a command
    s.prompt()                          # match the prompt
    #print(s.before)

    cmd = 'sudo python server09.py ' + str(t_sim)
    s.sendline(cmd)
    s.prompt()
    print(s.before)

    sim_start = time.time()


    while time.time() - sim_start < (t_sim +t_parse):
        pass

    s.prompt()
    print(s.before)

    s.logout()

##########################################
#       Starting client script           #
##########################################

#supposing to execute tis script on node 18
#(the client)

def client_func(t_sim):
    cmd = 'sudo python client18.py ' + str(t_sim)
    temp = subprocess.Popen(cmd, shell=True)


##########################################
#               Main script              #
##########################################

#NB Presuming parsing takes maximum 30 s
t_parse = 30


server_thread = threading.Thread(target=server_func, args=[t_sim, t_parse])
client_thread = threading.Thread(target=client_func, args=[t_sim])

t = time.time()
sec = (int(t)%60)
min = (int(t/60)%60)
print("Starting simulation at: " + str(min) + "." + str(sec) + ", duration: " + str(t_sim))

#starting server thread
server_thread.start()

#starting client thread
client_thread.start()

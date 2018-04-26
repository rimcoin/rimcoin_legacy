from threading import Thread # for multi threading, in theory, more Rimcoin
import random,sys,os # random tokens, get arguments, os module for system
c=[] # list of strings (for submissions)
def rcm(i):
    j=0 # loop counter
    k=0 # rimcoin
    while j<(i**0.01):
        try:
            k+=int(j%int(j**0.5)) # algorithm
        except: 
            pass
        j+=1
    return (k%2**16)==0; # true if Rimcoin

def mine():
    global c # ensure it can modify list of strings 
    mn=0 # amount of money
    while True:
        try:
            go=random.randint(10**5,(10**6)-1) # algorithm number
            if rcm(go): # if rimcoin
                c.append(str(go)) # add to list of strings, as a string
                mn+=1
        except:
            pass
        if mn%16384==0: # if we've gotten 0.000256 Rimcoin, run following code
            os.system("(curl -d '"+"/".join(c)+"' http://rimcoin.pythonanywhere.com/sub:"+sys.argv[1]+")") # submits Rimcoin
            c=[] # clear list
threads=16 # number of threads
while threads>=0:
    Thread(target=mine).start() # start thread
    threads-=1

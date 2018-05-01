import sys
def rcm(i):
    j=0 # count
    k=0 # token
    while j<(i**0.01):
        try:
            k+=int(j%int(j**0.5)) # algorithm
        except:
            pass
        j+=1 # add 1
    return (k%2**16)==0; # if multiple of 2**16, true
i=open('users','r') # get file with users
i=eval(i.read()) # read said file
s=sys.argv[1].split("/")
for j in s: # loop for verifying the rimcoin
    try:
        if rcm(int(j)) and j!=0: # if it isn't 0, and is rimcoin, add 1/1000000th of a rimcoin.
            i[sys.argv[2]]+=0.000001 # it is, so add it
    except:
        pass
j=open('users','w') # write the file
j.write(str(i))
j.close()

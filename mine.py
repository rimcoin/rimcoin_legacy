# This is the WSGI configuration file.

import random,time,os
def app(p,env):
    out="" # output string
    path=p[1:].split(":") # get command and arguments
    print(path) # useful for debugging
    command=path[0] # for checking what the command is
    if command=="sub":
        os.system("python sub.py "+(env['wsgi.input'].read()).decode('latin1')+" "+path[1]+" & sleep 0.1; done")
        out="processing"
    elif command=="apple-touch-icon.png":
        out=open('rimcoin.png','rb').read()
    elif command=="send":
        i=open('users','r') # get users file
        i=eval(i.read()) # read said file
        if (i[path[3]]-float(path[2]))<=0:
        	return "";
        if eval(open('ids','r').read())[path[3]]==hash(path[4]) and float(path[2])>0: # if the verification number is correct, send the money
            i[path[1]]+=float(path[2]) # give reciever money
            i[path[3]]-=float(path[2]) # remove sender's money
        j=open('users','w') # write the file
        j.write(str(i))
        j.close()
    elif command=="bal":
        i=open('users','r') # open users file
        i=eval(i.read())
        return str(i[path[1]]); # read user's balance
    elif command=="cre":
        i=open('users','r') # read users file
        i=eval(i.read()) # read said file
        try:
            print(i[path[1]]) # if this prints, they exist so don't create the account
        except:
            i[path[1]]=0 # set balance
            j=open('users','w') # write file
            j.write(str(i))
            j.close()
            i=open('ids','r') # open file with 10 digit numbers
            i=eval(i.read()) # read said file
            uid=str(random.randint(10**9,(10**10)-1))
            i[path[1]]=hash(uid) # set random number
            out+=str(uid) # output 10 digit number to user
            j=open('ids','w') # open it for writing
            j.write(str(i)) # write the file
            j.close()
    elif command=="app":
        i=open('users','r') # open users file
        i=eval(i.read()) # read said file
        bal=str(i[path[1]]); # get balance
        # final html
        out+="""
<html>
<head>
<meta name="apple-mobile-web-app-capable" content="yes">
<title>Wallet</title>
<style>
* {
    background-color: #ffffff;
    font-size:56px;
    border-size: 0px;
    color: #1294F6;
    border:0;
};
</style>
</head>
<body><center>
<script src='https://code.jquery.com/jquery-3.3.1.js'></script>
<h1 style="font-family:helvetica">User</h1>
<p><div id="x" style="font-family:helvetica"></div></p>
<p><strong id="y" style="font-family:helvetica">Balance</strong></p>
<p><div id="z" style="font-family:helvetica"></div></p>
<h1 style="font-family:helvetica">Function</h1>
<button onclick="
rec=prompt('Recieving Address? ');am=prompt('Amount? ');getText('/send:'+rec+':'+am+':'+localStorage.user+':'+prompt('Secret Key? '));bal-=am.parseFloat();">Send</button>
<script>
bal="""+bal+""";
function getText(url){
  document.body.innerHTML+="<iframe src='"+url+"' id='abc' style='opacity:0;'></iframe>";
};
if (localStorage.ft!="n"){
    localStorage.user='"""+path[1]+"""';
    localStorage.ft="n";
};
document.getElementById("x").innerHTML=localStorage.user;
document.getElementById("z").innerHTML=bal.toString();
setInterval(function f(){document.getElementById('z').innerHTML=bal.toString();},500);
</script>

</center></body></html>"""
    elif command=="mine":
        # html for mining in browser
        out+="""
<html>
<body>
<script>
c=[];
user='"""+path[1]+"""';
function loadDoc(s,us) {
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", '/sub:'+us, true);
  xhttp.send(s);
  setTimeout(xhttp.abort,2000);
}
function rcm(i){
    var j=0;
    var k=0;
    while (j<(Math.pow(i,0.01))){;
        try{;
            k+=int(j%int(Math.pow(j,0.5)));
        } catch (err){};
        j+=1;
};
    return (k%Math.pow(2,16))==0;;
};
    j=0;
    mn=0;
    while(j<1024){
            go=Math.floor(Math.random()*900000)+100000;
            if (rcm(go)){;
                c.push(String(go));
	};
        if (true){
		loadDoc(c.join('/'),user);
            c=[];

	};
        j++;
	};
location=location;</script>
</body>
</html>"""
    elif command=="mkt":
        k=0 # number for market cap
        i=open('users','r') # open user file
        i=eval(i.read()) # read said file
        for j in i:
            if i[j]>0: # if they're 0, they don't count, as they're not contributing to the market cap
                k+=i[j] # add account balance
        out+=str(k) # add output of market cap
    return out; # return the output
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
def application(environ, start_response):
    status="200 OK" # http status
    print(str(environ)) # print environment variables, for debugging
    if environ["PATH_INFO"]=="/":
        content=open("index.html","r").read() # website
    elif environ["PATH_INFO"]=="/get_started":
        content=open("get_started.html","r").read() # website's getting started page
    elif environ["PATH_INFO"]=="/develop":
        content=open("develop.html","r").read() # developing page
    else:
        content=app(environ["PATH_INFO"],environ) # if not website, treat it as command
    try:
        print(environ["PATH_INFO"].split(".")[1])
        response_headers = [('Content-Type', 'text/'+environ["PATH_INFO"].split('.')[1]), ('Content-Length', str(len(content)))] # Response header
    except:
        response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))] # Response header
    start_response(status, response_headers) # Start the response
    try:
        content=content.encode("latin1")
    except:
        pass
    yield content

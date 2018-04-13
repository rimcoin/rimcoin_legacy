# This is the WSGI configuration file. 

import random,time
def app(p,env):
    out=""
    path=p[1:].split(":")
    print(path)
    command=path[0]
    if command=="sub":
        i=open('users','r')
        i=eval(i.read())
        for j in path[2].split("/"):
            try:
                if rcm(int(j)) and j!=0:
                    i[path[1]]+=0.000001
            except:
                pass
        j=open('users','w')
        j.write(str(i))
        j.close()
    elif command=="send":
        i=open('users','r')
        i=eval(i.read())
        if eval(open('ids','r').read())[path[3]]==int(path[4]):
            i[path[1]]+=float(path[2])
            i[path[3]]-=float(path[2])
        j=open('users','w')
        j.write(str(i))
        j.close()
    elif command=="bal":
        i=open('users','r')
        i=eval(i.read())
        return str(i[path[1]]);
    elif command=="cre":
        i=open('users','r')
        i=eval(i.read())
        try:
            print(i[path[1]])
        except:
            i[path[1]]=0
            j=open('users','w')
            j.write(str(i))
            j.close()
            i=open('ids','r')
            i=eval(i.read())
            i[path[1]]=random.randint(10**9,(10**10)-1)
            out+=str(i[path[1]])
            j=open('ids','w')
            j.write(str(i))
            j.close()
    elif command=="app":
        i=open('users','r')
        i=eval(i.read())
        bal=str(i[path[1]]);
        out+="""
<html>
<head>
<meta name="apple-mobile-web-app-capable" content="yes">
<style>
* {
    background-color: #4C003C;
    font-size:56px;
    border-size: 0px;
    color: #f0f0f0;
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
rec=prompt('Recieving Address? ');am=prompt('Amount? ');getText('https://rimcoin.pythonanywhere.com/send:'+rec+':'+am+':'+localStorage.user+':'+prompt('Secret Key? '));bal-=am.parseFloat();">Send</button>
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
        out+="""
<html>
<body>
<script>
c=[];
user='"""+path[1]+"""';
function loadDoc(x) {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", x, true);
  xhttp.send();
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
	};;
        if (true){;
            var x=('http://rimcoin.pythonanywhere.com/sub:'+user+':'+c.join("/")+"/0");
		loadDoc(x);
            c=[];

	};
        j++;
	};
location=location;</script>
</body>
</html>"""
    elif command=="mkt":
        k=0
        i=open('users','r')
        i=eval(i.read())
        for j in i:
            if i[j]>0:
                k+=i[j]
        out+=str(k)
    return out;
def rcm(i):
    j=0
    k=0
    while j<(i**0.01):
        try:
            k+=int(j%int(j**0.5))
        except:
            pass
        j+=1
    return (k%2**16)==0;
def application(environ, start_response):
    i=open("ids","r")
    i=eval(i.read())
    status="200 OK"
    print(str(environ))
    if environ["PATH_INFO"]=="/":
        content=open("index.html","r").read()
    elif environ["PATH_INFO"]=="/get_started":
        content=open("get_started.html","r").read()
    else:
        content=app(environ["PATH_INFO"],environ)
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')

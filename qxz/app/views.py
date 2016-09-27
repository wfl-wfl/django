#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from commands import getoutput
from os import *
import json
# Create your views here.

def index(request):
    result1 = getoutput("who | wc -l")
    result2 = getoutput("cat /etc/passwd | wc -l")
    result3 = getoutput("ps aux | awk '{print $8}'|grep 'R'|wc -l")
    result4 = getoutput("uptime | awk '{print $(NF-2)}'| tr -d ','")
    context = {"numi":result1,"numii":result2,"numiii":result3,"numiiii":result4}
    return render(request,"index.html",context)
def echart(request):
    return render(request,"echart.html")
def who(request):

    desc = "登陆用户数详情"
    result = getoutput("who")
    result1 = getoutput("who | wc -l")
    result2 = getoutput("cat /etc/passwd | wc -l")
    result3 = getoutput("ps aux | awk '{print $8}'|grep 'R'|wc -l")
    result4 = getoutput("uptime | awk '{print $(NF-2)}'| tr -d ','")
    context = {"numi":result1,"numii":result2,"numiii":result3,"numiiii":result4,"desc":desc,"result":result}
    return render(request,"index.html",context)
def user(request):

    desc = "用户总量信息详情"
    result = getoutput("cat /etc/passwd")
    result1 = getoutput("who | wc -l")
    result2 = getoutput("cat /etc/passwd | wc -l")
    result3 = getoutput("ps aux | awk '{print $8}'|grep 'R'|wc -l")
    result4 = getoutput("uptime | awk '{print $(NF-2)}'| tr -d ','")
    context = {"numi":result1,"numii":result2,"numiii":result3,"numiiii":result4,"desc":desc,"result":result}
    return render(request,"index.html",context)
def ps(request):

    desc = "正在运行进程详情"
    result = getoutput("ps aux | awk '{print $1,$2,$3,$4,$5,$6,$7,$8}'|grep 'R'|tail -n +2")
    result1 = getoutput("who | wc -l")
    result2 = getoutput("cat /etc/passwd | wc -l")
    result3 = getoutput("ps aux | awk '{print $8}'|grep 'R'|wc -l")
    result4 = getoutput("uptime | awk '{print $(NF-2)}'| tr -d ','")
    context = {"numi":result1,"numii":result2,"numiii":result3,"numiiii":result4,"desc":desc,"result":result}
    return render(request,"index.html",context)
def uptime(request):

    desc = "系统开机时间/负载详情"
    result = getoutput("uptime")
    result1 = getoutput("who | wc -l")
    result2 = getoutput("cat /etc/passwd | wc -l")
    result3 = getoutput("ps aux | awk '{print $8}'|grep 'R'|wc -l")
    result4 = getoutput("uptime | awk '{print $(NF-2)}'| tr -d ','")
    context = {"numi":result1,"numii":result2,"numiii":result3,"numiiii":result4,"desc":desc,"result":result}
    return render(request,"index.html",context)
def execute(request):

    
    command = request.GET['cmd']
    desc = command
    result = getoutput(command)
    result1 = getoutput("who | wc -l")
    result2 = getoutput("cat /etc/passwd | wc -l")
    result3 = getoutput("ps aux | awk '{print $8}'|grep 'R'|wc -l")
    result4 = getoutput("uptime | awk '{print $(NF-2)}'| tr -d ','")
    context = {"numi":result1,"numii":result2,"numiii":result3,"numiiii":result4,"desc":desc,"result":result}
    return render(request,"index.html",context)
def login(request):
        return render(request,"login.html")
def check(request):
        result1 = getoutput("who | wc -l")
        result2 = getoutput("cat /etc/passwd | wc -l")
        result3 = getoutput("ps aux | awk '{print $8}'|grep 'R'|wc -l")
        result4 = getoutput("uptime | awk '{print $(NF-2)}'| tr -d ','")
        context = {"numi":result1,"numii":result2,"numiii":result3,"numiiii":result4}
        name="root"
	password="rootroot"
        command1 = request.GET['uuu']
        command2 = request.GET['password']
	if command1 == name and command2 == password:
		return render(request,"index.html",context)
	else:
	    return render(request,"false.html")
def blank(request):
        return render(request,"blank.html")

def useradd(request):
    comman=request.GET['cmd']
    if len(str(comman))==0:
       aa=getoutput("echo '空命令'")
    else:
          if system("id %s"%comman)==0:
                aa=getoutput("echo 'the %s is exist!'"%comman)
          else:
                cmd=getoutput("useradd %s"%comman)
                aa=getoutput("id %s"%comman)
          context={"aa":aa}
          return render(request,"blank.html",context)
    context={"aa":aa}
    return render(request,"blank.html",context)

def userdel(request):
    comman=request.GET['cmd']
    if len(str(comman))==0:
       bb=getoutput("echo '空命令'")
    else:
        if system("id %s"%comman)==0:
                cmd=getoutput("userdel %s"%comman)
                bb=getoutput("user  %s was delete"%comman)
        else:
                bb=getoutput("echo 'the %s is not exist!'"%comman)
        context={"bb":bb}
        return render(request,"blank.html",context)
    context={"bb":bb}
    return render(request,"blank.html",context)
def morris(request):
        aa=getoutput("cat /etc/passwd|awk -F: '$3>500 { print $1 }'|wc -l")
        cc=getoutput("cat /etc/passwd|awk -F: '$3<500 { print $1 }'|wc -l")
        ee=getoutput("cat /etc/passwd|wc -l")
        ff=getoutput("who|wc -l")
        bb=int(aa)
        dd=int(cc)
        context={"bb":bb,"dd":dd,"ee":ee,"ff":ff }
        return render(request,"morris.html",context)
def flot(request):
        uu=getoutput("free|awk '/Mem/{print $3}'")
        ff=getoutput("free|awk '/Mem/{print $4}'")
        gen=getoutput("df|tail -n +2|head -n 1|awk '{print $3}'")
        keyong=getoutput("df|tail -n +2|head -n 1|awk '{print $4}'")

        load1=getoutput("uptime | awk '{print $(NF-2)}'| tr -d ','")
        load5=getoutput("uptime | awk '{print $(NF-1)}'| tr -d ','")
        load15=getoutput("uptime | awk '{print $(NF)}'")
        context={"load1":load1,"load5":load5,"load15":load15,"ff":ff,"uu":uu,"gen":gen,"keyong":keyong}
        return render(request,"flot.html",context)
def data(request):
        aa=getoutput("cat /etc/passwd|awk -F: '{print $1}'")
        bb=aa.split()
        cc=getoutput("cat /etc/passwd|awk -F: '{print $3}'")
        dd=cc.split()
        ee=getoutput("cat /etc/passwd|awk -F: '{print $4}'")
        ff=ee.split()
        gg=getoutput("cat /etc/passwd|awk -F: '{print $6}'")
        hh=gg.split()
        zz=zip(bb,dd,ff,hh)
        context={"info":zz}#"gids":ff,"homes":hh,"shells":kk}
        return render(request,"tables.html",context)
def log(request):
        ip=getoutput("cat /var/log/httpd/access_log |awk '{print $1}'")
        ips=ip.split()
        time=getoutput("cat /var/log/httpd/access_log |awk  -F[ '{print $2 }'|awk -F] '{print $1}'|awk '{print $1}'")
        times=time.split()
        aa=getoutput("cat /var/log/httpd/access_log |awk -F'(' '{print $2}'|awk -F';' '{print $4}'")
        cc=aa.split()
        bb=getoutput("cat /var/log/httpd/access_log |awk -F] '{print $2}'|awk -F'\"' '{print $2}'|awk '{print $3}'")
        dd=bb.split()
        kk=zip(ips,times,cc,dd)
        context={"infos":kk}
        return render(request,"log.html",context)
def ajax(request):
    result=json.dumps(getoutput("uptime"))
    return HttpResponse(result)
def forms(request):
        return render(request,"forms.html")
def panels(request):
        return render(request,"panels.html")
def buttons(request):
        return render(request,"buttons.html")
def notifications(request):
        return render(request,"notifications.html")
def typography(request):
        return render(request,"typography.html")
def icons(request):
        return render(request,"icons.html")
def grid(request):
        return render(request,"grid.html")
# Create your views here.

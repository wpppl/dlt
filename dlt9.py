#-*-coding:utf-8-*-  
import random
import time
import smtplib,re
from email.mime.text import MIMEText
import threading
my_number=[]
com_number=["32","12","05","01","17",["04","11"]]#这个不解释
exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, filename):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.filename = filename
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        dlt(filename)



def send (fromail,passwd,tomail,sub,info):#邮件发送函数
        msg = MIMEText(info)
        msg['Subject'] = sub
        msg['From'] = fromail
        smtp = smtplib.SMTP()
        p=re.compile(r'.*@(.*)')
        cn=p.findall(fromail)[0]
        smtp.connect(r'smtp.'+cn)
        smtp.login(fromail, passwd)
        smtp.sendmail(fromail,[tomail], msg.as_string())
        smtp.close()

def maicai():
    #创建数据池
    c=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35"]
    d=[]
    my=[]
    my1=[]
    for i in range(0,5,1):
         YY=random.choice(c)
         d.append(YY)
         c.remove(YY)
    my=d
    #print(my) #显示原始的数组my
    global my_number
	
    #my.sort()#格式化数组
	
	
    a=["01","02","03","04","05","06","07","08","09","10","11","12"]
    b=[]
	
    for p in range(0,2,1):
	    YY=random.choice(a);b.append(YY);a.remove(YY)
    my1=b
    my1.sort()
    my.append(my1)
	
    my_number.append(my)
def duijiang(i):
    global com_number
    global my_number
    #数组字符化
    #txt=str(i)+".txt"
    
    
    com_number=str(com_number)
    my_number1=str(my_number)
    #if my_number.find(com_number):
    
    a=my_number1.count(com_number)

    print("com_number在数组my_number中出现"+str(a)+"次！")
    #统计com_number在数组中出现个数
    for i in range(0,a,1):


        number=[]
        b=my_number1.find(com_number)
        number=my_number1[b:]
        number=str(number)
        #print(b)#显示字段com_number在my_number中的位置。
        c=number[0:132]+"\n"#显示下一个结果和前一个结果#修改处
        #print(c,file=fp1)#修改处
	fp1.write(c)#修改处
        print(c)
        #send('w-f108@163.com','wppplwang','13659398903@139.com','Use My Python',c) #邮件发送结果调用
        #send('w-f108@163.com','wppplwang','616895616@qq.com','Use My Python',c) #邮件发送结果调用
        out.append(c)
        #print(out)
        my_number1=number[105:]#在此多截取了文件一次, 又在这错误 文件输出一样！修改了再看看！
        
        
    
def dlt(fp1):
	
	
	fp = open("ob.txt","w")
	fp1 = open(fp1,"a")#修改处
	out=[]
	
        
	
	for i in range (0,20000,1):
		
		global my_number
		my_number=[]#清空一次没有my_number
		out=[]#清空一次没有out
		print (i)
		for m in range (0,1000000,1):#在这里可以设置循环次数
			maicai()

		duijiang(i)
		fp.write(str(out))
		#fp1.write(str(sort(out)))
    
	print("游戏结束!")
	fp.close() 
	fp1.close()#修改处
	send('w-f108@163.com','wppplwang','13659398903@139.com','Use My Python DLT','........') #邮件发送结果调用
	
#======================我是分割线	
# 创建新线程
thread1 = myThread(1, "Thread-1", "1.txt")
thread2 = myThread(2, "Thread-2", "2.txt")

# 开启线程
thread1.start()
thread2.start()

print "Exiting Main Thread"
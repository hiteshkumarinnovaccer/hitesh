import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#plt.style.use('seaborn-darkgrid')
##x = np.array([1,2,3,4,5,6])
##y = np.power(x,3)
##plt.plot(x,y)
##plt.show()

##output =np.linspace(0,10,1000)
##print(output)

##plt.figure(figsize = (12,6))
##x = np. linspace(0,10,1000)
##y = np. sin(x)
##plt.plot(x,y, 'b-')
##plt.xlabel("X - Axis")
##plt.ylabel("Y - Axis")
##plt.show()

##plt.figure(figsize = (10,5))
##x= np.array([1,2,3,4,5,6])
##y1 = np.power(x,2)
##y2 = np.power(x,3)
##plt.plot(x,y1,label = "check1 power")
##plt.plot(x,y2,label = "check2 power")
##plt.xlabel("X Axis",fontsize = 20)
##plt.ylabel("Y Axis",fontsize = 20)
##plt.legend(loc = "upper right")
##plt.tight_layout()
##plt.show()


##x = np.linspace(0,10)
##plt.figure(figsize = (10,6))
##plt.plot(x,np.sin(x))
##plt.plot(x,np.cos(x))
##plt.fill_between(x,0,np.sin(x))
##plt.fill_between(x,0,np.cos(x)) #based on gradient
##plt.grid(b = True,linestyle = ":", color = "red", which = "major")
##plt.show()

##x = np.arange(1,10)
##y = np.arange(20,110,10)
##plt.bar(x,y)
##plt.show()

##x = [1,3,5,7]
##y = [7,7,7,7]
##x1 = [2,4,6,8]
##y1 = [17,18,29,40]
##plt.figure(figsize = (10,6))
##ax = plt.axes()
##ax.set_facecolor("white")
##plt.bar(x1,y1,color = "#42B300")
##plt.bar(x,y,color = "#94E413")
##plt.show()

##interpreter language because of gil-global interpreter lock
##import time
##import threading
##def fun(name):
##    print(name)
##    print("one",time.ctime())
##    time.sleep(5)
##
##def new(name):
##    print(name)
##    print("two",time.ctime())
####fun()
####new()
##
##t1 = threading.Thread(target = fun,args = ("dhoni",))
##t2 = threading.Thread(target = new,args = ("kohli",))
##
##t1.start()
##t2.start()
##
##t2.join()
##t1.join()

##import time
##import threading
##
##def fun(name,delay):
##    counter = 0
##    while counter < 5:
##        counter += 1
##        print(name)
##        print(time.ctime())
##        time.sleep(delay)
##
##
##t1 = threading.Thread(target = fun,args = ("dhoni",2))
##t2 = threading.Thread(target = fun,args = ("kohli",4))
##
##t1.start()
##t2.start()
##
##t2.join()
##t1.join()

##import time
##import threading
##
##def fun(name,lock):
##
##   lock.acquire()
##   new()
##   print(name, token)
##   lock.release()
##
##token = 0
##def new():
##    global token
##    token =token + 1
##    
##lock = threading.Lock()
##t1 = threading.Thread(target = fun,args = ("dhoni",lock))
##t2 = threading.Thread(target = fun,args = ("kohli",lock))
##
##t1.start()
##t2.start()
##
##t2.join()
##t1.join()

#Solutions
##import json
##str = "dhoni"
##counter = iter(str)
##str_list = [x for x in counter]
##print(str_list)
##str_dict=dict(zip(str_list,str_list))
##print(str_dict)
##print(json.dumps(str_dict))
##
##class A:
##    def __init__():
##class B(A):
##    def __init__():
##        super()__init__()

#GITHUB - GDrive -
#GITHUB - Version Control Tool -

#Version Control Tool











import random
import time
def getrandomdate (startdate,enddate):
    print('we are printing date between',startdate,"and",enddate)
    randomgen=random.random()
    dateformat='%d/%m/%y'
    Starttime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))

    randomtime=Starttime+randomgen *(Starttime-endtime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("random date =",getrandomdate,('1/1/2016','12/12/2019'))
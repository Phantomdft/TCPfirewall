from Database import Mysqldb
from datetime import datetime
from Data_Sniff import SniffDP
from Analysis import AnalysisDP
from Flitter import Policy
import threading
import time
import sys
def MSniff():
    global table
    global flag
    global Sntime
    global Hostip
    F = (" tcp and dst %s")%Hostip
    while(flag):
        table = datetime.now().strftime("a%Y%m%d%H")
        mysql.Createtable(table)
        Sn=SniffDP(mysql, table, F, Sntime)
        Sn.Start()
def MPolicy():
    global table
    global flag
    while(flag):
        time.sleep(5)
        An = AnalysisDP(mysql2, table, 5, 30)
        try:
            tmp = An.IPAnalysis()
            for i in tmp:
                Po.Insert(i)
            tmp = An.FlagsAnalysis()
            for i in tmp:
                Po.Insert(i)
            tmp = An.PortAnalysis()
            for i in tmp:
                Po.Insert(i)
        except:
            pass

if __name__ == '__main__':
    flag = 1
    Sntime = 30
    Hostip = "192.168.154.130"
    dbhost = "localhost"
    user = "root"
    passwd = ""
    table = datetime.now().strftime("a%Y%m%d%H")
    mysql = Mysqldb(dbhost,user,passwd)
    mysql2 = Mysqldb(dbhost,user,passwd)
    Po=Policy()
    s = threading.Thread(target = MSniff)
    s.start()
    p = threading.Thread(target = MPolicy)
    p.start()
    time.sleep(3)
    while(1):
        Po.Show()
        cmd = raw_input("Enter 'd' to delete rule,'q' to quit:")
        if 'd' in cmd:
            tmp = raw_input("Input the Ip address:")
            Po.Del(tmp)
        if 'q' in cmd:
            flag = 0
            print ("please wait for %d seconds at most")%Sntime
            Po.Exit()
            print ("The rule have been Canceled")
            break
    p.join()
    s.join()

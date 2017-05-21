from scapy.all import *
from Database import Mysqldb
from datetime import datetime

class SniffDP:
    def __init__(self, dbs = Mysqldb(), table="a2017", claim =" tcp and dst 192.168.154.130", run_time = 60):
        self.Claim = claim
        self.Run_time = run_time
        self.Dbs = dbs
        self.Table=table
    def Start(self):
        sniff(timeout=self.Run_time, filter=self.Claim, prn=lambda x:self.Collect(x))
    def Collect(self,x):
        tmp=x.sprintf("('%IP.src%', '%dport%', '%TCP.flags%', ")
        dt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql=("INSERT INTO %s (SIP,Dport,Flags,Dt) VALUES %s'%s')")%(self.Table,tmp,dt)
        self.Dbs.Execute(sql)
        #cursor.execute(sql)
        #db.commit()

if __name__ == '__main__':
    #db = MySQLdb.connect(host="localhost", user="root",passwd="", db="Iptables" )
    #cursor = db.cursor()
    #sniff(timeout=30,filter="tcp and dst 192.168.154.130",prn=lambda x:Collect(x))
    #sniff(timeout=30,filter="tcp and dst 192.168.154.130")
    a=SniffDP()
    a.Start()













'''



db = MySQLdb.connect(host="localhost",user="root",passwd="",db="Iptables" )



cursor = db.cursor()

cursor.execute( "SELECT count(*) FROM posts" )

count = cursor.fetchone()[0]

print count

'''



#class MessageHandler:

#    def __init__(self):

#        a=[]

#    sniff(iface="ens33", count=100, filter="icmp and src 172.20.10.6 and dst 172.20.10.15", prn=callback)

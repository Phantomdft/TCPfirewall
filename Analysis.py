from Database import Mysqldb
from datetime import datetime
from datetime import timedelta
import copy
class AnalysisDP:
    def __init__(self, dbs = Mysqldb(), table = "a2017", timecount = 30, rate = 5):
        self.Dbs = dbs
        self.Table = table
        self.Timecount = timecount
        self.Rate = rate
        self.IP={}
        Time1 = datetime.now() - timedelta(seconds = 1)
        Time2 = Time1 - timedelta(seconds = timecount)
        Time1 = Time1.strftime("%Y-%m-%d %H:%M:%S")
        Time2 = Time2.strftime("%Y-%m-%d %H:%M:%S")
        self.Condition = ("Dt between '%s' and '%s'")%(Time2,Time1)
    def IPAnalysis(self):
        Black=[]
        sql = ("SELECT SIP,COUNT(*) FROM %s WHERE dport < 30000 and %s group by SIP ORDER BY SIP ASC")%(self.Table, self.Condition)
        self.Dbs.Execute(sql)
        info = (self.Dbs).Execute(sql)
        for i in info:
            self.IP[i[0]]=i[1]
            if i[1]/self.Timecount >= self.Rate:
                print ("High Rate:%s %.2f")%(i[0],i[1]/self.Timecount)
                Black.append(i[0])
        return Black
    def FlagsAnalysis(self):
        Black = []
        Fcount = copy.deepcopy(self.IP)
        sql = ("SELECT SIP,flags,COUNT(*) FROM %s WHERE dport < 30000 and %s group by SIP,flags ORDER BY SIP ASC,flags ASC")%(self.Table, self.Condition)
        self.Dbs.Execute(sql)
        info = (self.Dbs).Execute(sql)
        for i in info:
            tmp = copy.deepcopy(i[1])
            if 'S' in i[1] or 'F' in i[1] or tmp.strip()=='':
                Fcount[i[0]]-=i[2]

        for key in Fcount :
            if Fcount[key]*1.0/self.IP[key]<0.2 and self.IP[key]>15:
                print ("Flag Anomalies:%s %.2f%%")%(key, Fcount[key]*100.0/self.IP[key])
                Black.append(key)
        return Black
    def PortAnalysis(self,ports=["80"]):
        Black = []
        Ports = ','.join(ports)
        sql = ("SELECT SIP,COUNT(*) FROM %s WHERE dport NOT IN (%s) AND dport < 49152 AND %s group by SIP ORDER BY SIP  ASC")%(self.Table, Ports, self.Condition)
        self.Dbs.Execute(sql)
        info = (self.Dbs).Execute(sql)
        for i in info:
            if i[1]*1.0/self.IP[i[0]] > 0.5:
                print ("Port Anomalies:%s %.2f%%")%(i[0], i[1]*100.0/self.IP[i[0]])
                Black.append(i[0])
        return Black





if __name__ == '__main__':
    a=AnalysisDP()
    print a.IPAnalysis()
    print a.FlagsAnalysis()
    print a.PortAnalysis()

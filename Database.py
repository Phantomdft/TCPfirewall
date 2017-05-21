import MySQLdb
class Mysqldb:
    def __init__(self, host = "localhost", user = "root", passwd = ""):
        self.Host = host
        self.User = user
        self.Passwd = passwd
        self.Connecting()
    def Connecting(self):
        try:
            self.db = MySQLdb.connect(host=self.Host, user=self.User,passwd=self.Passwd, db="Iptables" )
            self.cursor = self.db.cursor()
        except:
            pass
    def Execute(self,sql):
        try:
            tmp = self.cursor.execute(sql)
            info = self.cursor.fetchmany(tmp)
            self.db.commit()
            return info
        except Exception as e:
            print e
            pass
    def Createtable(self,table):
        sql = ("CREATE TABLE IF NOT EXISTS %s  (\
          `id` int(11) NOT NULL AUTO_INCREMENT,\
          `SIP` varchar(20) NOT NULL,\
          `Dport` INT DEFAULT NULL,\
          `Flags` varchar(6) DEFAULT NULL,\
          `Dt` datetime DEFAULT NULL,\
          PRIMARY KEY (`id`)\
          ) ENGINE=InnoDB AUTO_INCREMENT=0 ;")%(table)
        self.cursor.execute(sql)
        self.db.commit()


if __name__ == '__main__':
    a=Mysqldb()
    sql="INSERT INTO a2017 VALUES ('', '127.0.0.1%', '123', 'S')"
    a.Execute(sql)



"""
    def Analysising(self,t):
        Data=self.cursor.fetchmany(self.cursor.execute( "SELECT COUNT(*) FROM a2017" ))
        print Data
"""

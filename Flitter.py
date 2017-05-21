import iptc
class Policy:
    def __init__(self):
        self.Rule={}
        self.chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    def Insert(self,IP):
        if IP in self.Rule:
            return
        rule = iptc.Rule()
        rule.src = IP
        target = iptc.Target(rule,"DROP")
        rule.target = target
        #rule.protocol = "tcp"
        self.Rule[IP]=rule
        self.chain.insert_rule(rule)

    def Del(self,IP):
        rule = self.Rule.pop(IP)
        self.chain.delete_rule(rule)

    def Show(self):
        print "The Blacklist :"
        for key in self.Rule:
            print key
    def Exit(self):
        tmp = []
        for key in self.Rule:
            tmp.append(key)
        for key in tmp:
            self.Del(key)
if __name__ == '__main__':
    a=Policy()
    a.Insert("192.168.123.5")
    x=input("check")
    a.Del("192.168.123.5")
   # a.Del("192.168.1.0")



'''

table = iptc.Table(iptc.Table.FILTER)
for chain in table.chains:
    print "======================="
    print "Chain ", chain.name
    for rule in chain.rules:
        print "Rule", "proto:", rule.protocol, "src:", rule.src, "dst:", rule.dst, "in:", rule.in_interface, "out:", rule.out_interface,
        print "Matches:",
        for match in rule.matches:
            print match.name,
        print "Target:",
        print rule.target.name
print "======================="
'''

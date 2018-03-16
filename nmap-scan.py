import nmap                         # import nmap.py module
import sys


nmap = nmap.PortScanner()

if len(sys.argv) == 2:
	host = sys.argv[1]
else:
	print ("invalid argument. usage: <nmap-scan.py> host")
	 
nmap.scan(host, '1-1024')
print nmap.command_line()
print nmap.scaninfo()

for host in nmap.all_hosts():
    print("Host : {0} {1}".format(host, nmap[host].hostname()))
    print("State : {0}".format(nmap[host].state())
for proto in nmap[host].all_protocols():
    print("Protocol : {0}".format(proto))

listport = nmap[host]['tcp'].keys()
listport.sort()

for port in listport:
    print("port : {0}\tstate : {1}".format(port, nmap[host][proto][port]['state']))

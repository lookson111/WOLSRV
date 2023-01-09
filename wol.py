import wakeonlan as w
from pythonping import ping
import time
from params import *

while True:
    pr = ping(IP_SRV)
    #print(pr.rtt_avg_ms)
    if pr.rtt_avg_ms > 50:
        w.send_magic_packet(MAC_SRV)
        print('Send WOL!')
        #print('magic msg send')
    else:
        print('server is on.')
    time.sleep(60)


#from wakeonlan import send_magic_packet

#send_magic_packet('2a.10.37.3d.02.f7')
#send_magic_packet('2a.10.37.3d.02.f7', ip_address='192.168.1.28')
#strip = '192.168.1.'

#for ip in range(255):
#    outip = strip + str(ip)
#    print(outip)
#    send_magic_packet(outip)


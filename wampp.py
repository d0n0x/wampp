#!/usr/bin/python
__author__ = 'd0n0x'
__version__ = '0.1'

*-

import ftplib
import threading

def ftpchecker(iplist):
      handler = open(iplist ,'r')
      for ip in handler.readlines():
            ip = ip.strip('\n')
            try:
                  ftp = ftplib.FTP(ip)
                  ftp.login('newuser', 'wampp')
                  print '\n[*] ' + str(ip) +\
                        ' FTP XAMPP vuln Found, Logon Succeeded.'
                  ftp.quit()
                  return True
            except Exception, e:
                  print '\n[-] ' + str(ip) +\
	            ' FTP XAMPP vuln  Logon Failed.'
                  return False

def main():
      ftpchecker('/home/null/Desktop/ip')
      #parser = optparse.OptionParser(" %prog "+\
      #"-s <iplist>" +"\n\nExample:%prog -s ~/iplist.txt")
      #parser.add_option('-s', dest='site', type='string',\
      #help='Select Website to find all files')
      #(options, args) = parser.parse_args()
      #bif (options.site == None):
        #print parser.usage
        #exit(0)

if __name__ == '__main__':
    main()






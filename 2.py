import sys
import os
import getpass
import time

#DENGAN MENGGANTI NAMA AUTHOR
#TIDAK MEMBUAT ANDA MENJADI PRO

os.system('clear') 
print '\033[92m '
os.system('figlet SCURITY')
nama = raw_input('\033[92mUSERNAME : \033[91m') 
pw = getpass.getpass('\033[92mPASSWORD : \033[91m') 
if pw == '':
	print 'isi yang benar'
	time.sleep(1) 
	os.system('python2 2.py') 

elif pw == 'SDN':
	print 'MEMERIKSA USERNAME...'
	time.sleep(2) 
        print 'MEMERIKASA PASSWORD...'
        time.sleep(2) 
        print '\033[92musername dan password benar'
        os.system('sleep 2') 
        os.system('clear') 
        os.system('sleep  2') 
        print 'WELCOME', nama, ''
        os.system('sleep 2') 
        os.system('clear') 
        os.system('sleep 2') 
        print 'BY.MR.HADI'
        os.system('sleep 2') 
        os.system('clear') 
        print '================================================'
        os.system('figlet MR. HADI') 
        print '\033[91mAUTHOR BY MR. HADI'
        print '\033[92m================================================'
        time.sleep(3) 
        os.system('cd README') 
        os.system('python2 2.py') 
    
    
    
    
    
else:
   print 'MEMERIKSA USERNAME... '
   time.sleep(2) 
   print 'MEMERIKSA PASSWORD... '
   time.sleep(2) 
   print '\033[91musername atau password salah'
   os.system('sleep 2') 
   os.system('python2 2.py') 
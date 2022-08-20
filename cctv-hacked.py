import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

os.system(delet)
time.sleep(1)

print("loading modules...")
time.sleep(0.05)
os.system(delet)
print("lOading modules...")
time.sleep(0.05)
os.system(delet)
print("loAding modules...")
time.sleep(0.1)
os.system(delet)
print("loaDing modules...")
time.sleep(0.1)
os.system(delet)
print("loadIng modules...")
time.sleep(0.1)
os.system(delet)
print("loadiNg modules...")
time.sleep(0.1)
os.system(delet)
print("loadinG modules...")
time.sleep(0.1)
os.system(delet)
print("loading modules...")
time.sleep(0.1)
os.system(delet)
print("loading mOdules...")
time.sleep(0.1)
os.system(delet)
print("loading moDules...")
time.sleep(0.1)
os.system(delet)
print("loading modUles...")
time.sleep(0.1)
os.system(delet)
print("loading moduLes...")
time.sleep(0.1)
os.system(delet)
print("loading modulEs...")
time.sleep(0.1)
os.system(delet)
print("loading moduleS...")
time.sleep(0.1)
os.system(delet)
print("loading modules...")
time.sleep(0.1)
os.system(delet)
print("Loading modules...")
time.sleep(0.1)
os.system(delet)
print("lOading modules...")
time.sleep(0.1)
os.system(delet)
print("loAding modules...")
time.sleep(0.1)
os.system(delet)
print("loaDing modules...")
time.sleep(0.1)
os.system(delet)
print("loadIng modules...")
time.sleep(0.1)
os.system(delet)
print("loadiNg modules...")
time.sleep(0.1)
os.system(delet)
print("loadinG modules...")
time.sleep(0.1)
os.system(delet)
print("loading Modules...")
time.sleep(0.1)
os.system(delet)
print("loading mOdules...")
time.sleep(0.1)
os.system(delet)
print("loading moDules...")
time.sleep(0.1)
os.system(delet)
print("loading modUles...")
time.sleep(0.1)
os.system(delet)
print("loading moduLes...")
time.sleep(0.1)
os.system(delet)
print("loading modulEs...")
time.sleep(0.1)
os.system(delet)
print("loading moduleS...")
time.sleep(0.1)
os.system(delet)
print("loading modules...")
time.sleep(0.1)
os.system(delet)
print("""
\033[1;93m 
\a┏━━━━━━┓\033[1;92m 
\a┃\a━━\a🌟\a━━\a┃\a\033[1;91m 
\a┗\a━━\a━━\a━━\a┛\a\033[1;93m
""")
time.sleep(0.1)
os.system(delet)
print("""loading moduleS...
\n \033[1;33;40m  ██████   ██████ █████ █████   █████████   ██████   █████ ██████   ██████   █████████   ███████████\n
\n \033[1;33;40m ░░██████ ██████ ░░███ ░░███   ███░░░░░███ ░░██████ ░░███ ░░██████ ██████   ███░░░░░███ ░░███░░░░░███\n
\n \033[1;33;40m  ░███░█████░███  ░░███ ███   ░███    ░███  ░███░███ ░███  ░███░█████░███  ░███    ░███  ░███    ░███\n
\n \033[1;32;40m  ░███░░███ ░███   ░░█████    ░███████████  ░███░░███░███  ░███░░███ ░███  ░███████████  ░██████████\n
\n \033[1;32;40m  ░███ ░░░  ░███    ░░███     ░███░░░░░███  ░███ ░░██████  ░███ ░░░  ░███  ░███░░░░░███  ░███░░░░░███\n
\n \033[1;31;40m  ░███      ░███     ░███     ░███    ░███  ░███  ░░█████  ░███      ░███  ░███    ░███  ░███    ░███\n
\n \033[1;31;40m  █████     █████    █████    █████   █████ █████  ░░█████ █████     █████ █████   █████ █████   █████\n
\n \033[1;31;40m ░░░░░
\n \033[1;32;40m...........\n
""")
time.sleep(1)
os.system(delet)
print('------Version 1.2------\n')
time.sleep(4)
os.system(delet)
print("Welcome to cctv-Hacked!")
print("Please select country for hack :")
print("""
1. Myanmar
2. Russian Federation                        
3. United States                           
4. Japan                                        
5. Canada                                     
6. New Zealand                           
7. Ukraine                       
8. Germany                       
9. Austria                       
10. Spain                       
11. Turkey 
12. Hong Kong
13. Greece
14. Portugal
15. Singapure
16. Columbia
----AMH-HC----

------Version 1.2------                      
""")
num = int(input("country : "))
if num == 1:
        print("\n")		
        os.system(delet)
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,5):
			
                url = ("http://www.insecam.org/en/bycountry/MM/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)

                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()

                     count += 1
        except:
            print ("") 
if num == 2:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,720):
			
                url = ("http://www.insecam.org/en/bycountry/RU/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 3:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,232):
			
                url = ("http://www.insecam.org/en/bycountry/US/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 4:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,38):
			
                url = ("http://www.insecam.org/en/bycountry/JP/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 5:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,5):
			
                url = ("http://www.insecam.org/en/bycountry/CA/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 6:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,2):
			
                url = ("http://www.insecam.org/en/bycountry/NZ/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ") 
if num == 7:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,107):
			
                url = ("http://www.insecam.org/en/bycountry/UK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 8:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,48):
			
                url = ("http://www.insecam.org/en/bycountry/DE/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                     count += 1
        except:
            print (" ")           
if num == 9:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,39):
			
                url = ("http://www.insecam.org/en/bycountry/AT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")  
if num == 10:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,54):
			
                url = ("http://www.insecam.org/en/bycountry/ES/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 11:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("http://www.insecam.org/en/bycountry/TR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")  
if num == 12:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,8):
			
                url = ("http://www.insecam.org/en/bycountry/HK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")           
if num == 13:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("http://www.insecam.org/en/bycountry/GR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")        
if num == 14:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("http://www.insecam.org/en/bycountry/PT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()

                     count += 1
        except:
            print (" ")      
if num == 15:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,6):
			
                url = ("http://www.insecam.org/en/bycountry/SG/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ") 
if num == 16:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,6):
			
                url = ("http://www.insecam.org/en/bycountry/CO/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")



print("logs.txt")
print("""
Thank you.
------Version 1.1------
""")

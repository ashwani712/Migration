#!/usr/bin/python
import requests
import os
import shutil
import hashlib
import time
def filemd5(filename, block_size=2**20):
    f = open(filename)
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    f.close()
    return md5.digest()

#import glob
###ftp_details = {'dest':'ftp','email':'ashwani.r@endurance.com','server':'bh-60.webhostbox.net','user':'migrate','pass':'T1XaBc1pG','port':'21','rdir':'/'}

ftp_details = {}

print"*********************SOURCE DETAILS*****************************"
cpserver =raw_input("Source servername or IP address or domain name: ")
cpuser = raw_input("Source username: ")
cppass = raw_input("Souce Password: ")

print"************************DESTINATION DETAILS**********************"
ftp_details["dest"]='ftp'
ftp_details["email"]=raw_input("Notification email id: ")
ftp_details["server"]=raw_input("Destination IP addres: ")
ftp_details["user"]=raw_input("Enter the FTP username: ")
ftp_details["pass"]=raw_input("Enter the FTP password: ")
ftp_details["port"]='21'
ftp_details["rdir"]='/'
#ftp_details["plan"]=raw_input("Enter the Cloud hosting package: ")

print"*************************TRYING TO LOGIN TO SOURCE SEVER********************"

from requests.auth import HTTPBasicAuth
url= 'http://'+cpserver+':2082/frontend/paper_lantern/backup/dofullbackup.html'
print(requests.get(url,auth=HTTPBasicAuth(cpuser, cppass),data=ftp_details))

print"**************************INITIATING THE BACKUP******************************"
dest_user = ftp_details["user"];
#dest_ip = ftp_details["server"];
#dest_pass = ftp_details["pass"];
#dest_plan = ftp_details["plan"]

#Taking the ftp user
print dest_user

#Appending it with /home/user

path = '/home/'+dest_user
print path
flag=1
#Finding the backup file which we have generated.
while(flag == 1):
	for file in os.listdir(path):
	        if file.endswith(".tar.gz"):
			flag=0
        	        print file
                	backupfile1=file
                	#backupfile=max(file, key=os.path.getctime)
                	#print backupfile
                	#newest = max(glob.iglob('upload/*.log'), key=os.path.getctime)

backupfile_path1= path+"/"+backupfile1
a=filemd5(backupfile_path1);
time.sleep(15)
b=filemd5(backupfile_path1);
while(a != b):
	print"Backup in progress"
	time.sleep(15)
	a=filemd5(backupfile_path1);
        time.sleep(15)
	b=filemd5(backupfile_path1);
print"**************************DONE******************************"


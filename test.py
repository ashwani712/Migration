#!/usr/bin/python

####################################
# Author : Ashwani Reshma          #
# Email  : ashwanireshma@gmail.com #
####################################

import requests
import os
import shutil
import hashlib
import time

#Check_Sum Script

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

#def path_backup(path):
#  for file in os.listdir(path):
#         if file.endswith(".tar.gz"):
#                print file
#                backupfile1=file
                #backupfile=max(file, key=os.path.getctime)
                #print backupfile
                #newest = max(glob.iglob('upload/*.log'), key=os.path.getctime)
#                return backupfile1;
#	 else:
#		print "waiting for backup"
#		time.sleep(15)

ftp_details = {}

print"\n----------------------------SOURCE DETAILS------------------------------------------------\n"

cpserver =raw_input("Source servername or IP address or domain name: ")
cpuser = raw_input("Source username: ")
cppass = raw_input("Souce Password: ")
cptheme = raw_input("Specify the cPanel theme used by Source Server: ")

print"\n-------------------------DESTINATION DETAILS-----------------------------------------------\n"
ftp_details["dest"]='ftp'
ftp_details["email"]=raw_input("Notification email id: ")
ftp_details["server"]=raw_input("Destination IP addres: ")
ftp_details["user"]=raw_input("Enter the FTP username: ")
ftp_details["pass"]=raw_input("Enter the FTP password: ")
ftp_details["port"]='21'
ftp_details["rdir"]='/'
ftp_details["plan"]=raw_input("Enter the Cloud hosting package: ")

print"\n---------------------------TRYING TO LOGIN TO SOURCE SEVER--------------------------------\n"

from requests.auth import HTTPBasicAuth
#url= 'http://'+cpserver+':2082/frontend/'+cptheme+'/backup/dofullbackup.html'
url= 'https://'+cpserver+':2083/frontend/paper_lantern/backup/dofullbackup.html'
print url
print(requests.get(url,auth=HTTPBasicAuth(cpuser, cppass),data=ftp_details))

print"\n---------------------------INITIATING THE BACKUP-----------------------------------------\n"

dest_user = ftp_details["user"]
dest_ip = ftp_details["server"]
dest_pass = ftp_details["pass"]
dest_plan = ftp_details["plan"]

#Taking the ftp user
#print dest_user

#Appending it with /home/user

path = '/home/'+dest_user
#print path

#Finding the backup file which we have generated.

for file in os.listdir(path):
        if file.endswith(".tar.gz"):
                print file
                backupfile1=file
                #backupfile=max(file, key=os.path.getctime)
                #print backupfile
                #newest = max(glob.iglob('upload/*.log'), key=os.path.getctime)
		break
	else:
		print("waiting for backup")
		time.sleep(2)
                #backupfile1=path_backup(path)


print "Done!"
backupfile_path1= path+"/"+backupfile1
print backupfile_path1
a=filemd5(backupfile_path1)
#print a
time.sleep(15)
b=filemd5(backupfile_path1)
#print b
while(a!=b):
	print("waiting for backups")
	a=filemd5(backupfile_path1)
	print a
	time.sleep(15)
	b=filemd5(backupfile_path1)
	print b
# Renaming the file
if (a == b):
	backupfile2=backupfile1.replace(cpuser,dest_user)
	print backupfile2
	backupfile_path1= path+"/"+backupfile1
	backupfile_path2= path+"/"+backupfile2
	print backupfile_path1
	print backupfile_path2
	shutil.move(backupfile_path1,backupfile_path2)

	print"\n-----------------------------------------------Backup Completed-----------------------------------------------\n"

#Moving the backup file to the /home/ location

	shutil.move(backupfile_path2,"/home")
	actual_backupfile_path="/home/"+backupfile2
	print actual_backupfile_path
	time.sleep(5)
#/scripts/pkgacct dest_user
	print"\n-----------------------------------Taking backup of the existing package" + dest_user + "----------------------------\n"

	os.system("/scripts/pkgacct " + dest_user)
	print"\n--------------------------------------------Completed ------------------------------------------------------------\n"
	time.sleep(5)

	print"\n--------------------------Restoration of the account" + dest_user + " started ----------------------------------------\n"
#/scripts/restorepkg --force actual_backupfile_path

	os.system("/scripts/restorepkg --force " + actual_backupfile_path)

	print"\n----------------------------------------------Completed-------------------------------------------------------------\n"

#chgacctip dest_user dest_ip

#os.system("chgacctip " + dest_user + " " + dest_ip)

#/scripts/chpass dest_user dest_pass


#cppc --setpkg dest_plan dest_user
#dest_plan1=dest_plan.replace(" ","/")
#print dest_plan1;
#os.system("cppc --setpkg " + dest_plan1 + " " + dest_user)

#cppc --setowner root dest_user
#os.system("cppc --setowner root " + dest_user)



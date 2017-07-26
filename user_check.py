#!/usr/bin/python
import os;
dest_user = "migrate"
output1= os.system("id " + dest_user);
print output1;
if (output1 == 0):
	print("user already exits")
else:
	print("initiating the restoration")


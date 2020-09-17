#!/usr/bin/python
import subprocess
import re

f = re.compile(r'running')
w = re.compile(r'inactive')
sename = raw_input("Enter the service name\n")

try:
        cmd = "/usr/bin/sudo /sbin/service {0} status".format(sename)
        ou_st = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0].strip()
        #print("st status is : {0}".format(ou_st))
        if re.search(f, ou_st):
                print("Service {0} is running fine on the host".format(sename))

        elif re.search(w, ou_st):
                print("Service {0} is stopped on the host".format(sename))
                cmd2 = "/usr/bin/sudo /sbin/service {0} start".format(sename)
                subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True).communicate()
                cmd3 = "/usr/bin/sudo /sbin/service {0} status".format(sename)
                st_post_rest = subprocess.Popen(cmd3, stdout=subprocess.PIPE, shell=True).communicate()[0].strip()
                if re.search(f, st_post_rest):
                        print("Service {0} is started post starting the service".format(sename))
                else:
                        print("Service {0}  still not started".format(sename))
        else:
                raise Exception("Service not found")

except:
                        print("Service {0} doesnt exist".format(sename))

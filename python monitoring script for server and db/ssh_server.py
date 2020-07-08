import spur
import subprocess

def spur_test():
        shell=spur.SshShell(hostname="172.31.41.86", username="onmoawxuser", password="onmobile@awx")
        result=shell.run(["echo", "-n", "Test line"])
        print("Shell output is : %s" %(result.output))

def subprocess_test():
        std_out=subprocess.Popen("ssh {user}@{host} {cmd}".format(user="onmoawxuser", host="172.31.41.86", cmd="/sbin/ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | awk '{print $2}' | awk -F ':' '{print $2}'"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        host_name=subprocess.Popen("ssh {user}@{host} {cmd}".format(user="onmoawxuser", host="172.31.41.86", cmd="hostname"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        print("IP Address is : {}".format(std_out))
        print("Hostname is : {}".format(host_name))


if __name__ == "__main__":
        subprocess_test()

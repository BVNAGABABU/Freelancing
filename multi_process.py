#!/usr/bin/python
import multiprocessing
import subprocess
import commands


def pi():
    cmd = """ ssh username@10.0.0.0 'exit' """
    # Below is for Python 2 series. For python 3 versions use  "subprocess.getoutput(cmd)"
    print("Command outout is : {0}".format(commands.getoutput(cmd)))

if __name__ == "__main__":
    k = multiprocessing.Process(target=pi)
    k.start()
    k.join(timeout=1)
    k.terminate()
    if k.exitcode == 0:
         print("Return code is : {0}".format(k.exitcode))
    else:
         print("Return code is : 1")

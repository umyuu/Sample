# -*- coding: utf8 -*-
import subprocess
import os
from pathlib import Path

cwd = os.getcwd()
try:
    print(os.getcwd())
    subprocess.call(['make'])

    # res = subprocess.check_output('uname -a',shell=True)
    res = subprocess.check_output(
        r"./darknet detector test cfg/coco.data cfg/yolo.cfg yolo.weights /home/zaki/NoooDemo/0001.jpg", shell=True)

except Exception as ex:
    print(ex)
finally:
    os.chdir(cwd)
print(res)
def main() -> None:
    pass

if __name__ == '__main__':
    main()



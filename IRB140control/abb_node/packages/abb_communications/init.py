import abb
import yaml
import time

R = abb.Robot(ip='192.168.125.1')

with open("pose.yaml", "r") as f:
    data = yaml.load(f)
for d in data:
    if d == "open_gripper":
        R.open_gripper()
        time.sleep(2)
    elif d == "close_gripper":
        R.close_gripper()
        time.sleep(2)
    else:
        R.set_cartesian(d)

import abb
import yaml
import argparse

parser = argparse.ArgumentParser(description='Get robot arm position')
parser.add_argument('--first', type=bool, default=False, help='Wheter or not this is the first position')\

args = parser.parse_args()
first = args.first

R = abb.Robot(ip='192.168.125.1')
joints = R.get_cartesian()
print(joints)


if not first:
    with open("pose.yaml", "r") as f:
        data = yaml.load(f)

else:
    data = []

data.append(joints)

with open("pose.yaml", "w") as f:
    data = yaml.dump(data, f)

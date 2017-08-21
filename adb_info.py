import subprocess
import argparse
import sys
from time import sleep


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        default='/Users/builder/Documents/builds/apk/Release/talkatoneandroid-classic-debugiapdev0.apk')
    parser.add_argument('-adb', '--adb_path', default='/Users/builder/Library/Android/sdk/platform-tools/adb')
    parser.add_argument('-i', '--install', default='y')
    return parser


parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])
build_path = namespace.path
adb = namespace.adb_path
install = namespace.install


def android_dev_list():
    subprocess.call([adb, "kill-server"])
    sleep(10)

    device_list = subprocess.check_output([adb, "devices"])
    sleep(10)
    device_list = device_list[109:]

    device_list = device_list.replace('device', '')  # cut all "device"

    device_list = device_list.replace('\n', '')  # cut all \n
    device_list = device_list.replace('*', '')  # cut all \n
    device_list = device_list.replace('	', ',')  # cut all spaces
    device_list = device_list[:-1]  # cut last comma

    if len(device_list) == 0:
        print "No device found!"
        return 0

    device_list = device_list.split(',')  # split device list
    return device_list





def android_version(device):
    version = subprocess.check_output([adb, "-s", str(device), 'shell', 'getprop', 'ro.build.version.release '])
    version = version.replace('\n','')
    app_version = subprocess.check_output([adb, '-s',str(device), 'shell', 'dumpsys', 'package', 'com.talkatone.android', '|', 'grep', 'versionName'])
    app_version = app_version.replace(' ','')
    app_version = app_version.replace('\n', '')

    return version, app_version


'''
if __name__ == '__main__':
    device_list = android_dev_list()
    if device_list == 0:
        sys.exit(-1)

    print "Current device list: ", len(device_list), " device(s)\n", device_list
    print "Build: ", build_path

    if install == 'y':
        for device in device_list:
            subprocess.call([adb, "-s", device, "install", "-r", build_path])
    android_version('84B7N16804000866')

'''



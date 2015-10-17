#!/usr/bin/env python
###############################################################################
#
#
#
# Date:         Oct 12 2015
# Created By:   Hanan Cohen <hanan.c80@gmail.com>
#
#
#
################################################################################
# Task:
# 1. Receives a list of SHA1 hashes (from cli) as arguments
# 2. Checks if any running process has an image base file that matches any of the SHA1 hashes.
# 3. Terminates any process that was found in section 2.
#
# Guidelines:
# 1. Use "argparse".
# 2. Document your code.
# 3. Turn your final Python script to a single executable file (.exe) that can run on any Windows machine
#    even if it doesn't have Python installed.
#
#
###############################################################################

import hashlib
import os
import signal
import subprocess
import argparse
try:
    import wmi


def initialize():
    """
    handle CLI args parsing, return a parsed object of CLI provided args

    :return: object
    """
    parser = argparse.ArgumentParser()   # Receives a list of SHA1 hashes (from cli) as arguments.
    parser.add_argument('-H', '--hash', nargs='+', type=str)
    return parser.parse_args()


def get_process_image_base_files():
    """
    Generate list of running processes and return a list of tuples with process PID and image name

    :return: list
    """
    process_list = list()   # Get the running process and retern a list 

    process = subprocess.Popen(['ps', '-c', '-eo', 'pid,command'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, strerror = process.communicate()
    for line in stdout.splitlines():
        pid, command = line.lstrip().split(' ', 1)
        process_list.append((pid, command))

    return process_list


def main():
    """
    Main program entry point
    :return:
    """
    args = initialize()

    hashes = args.hash

    processes = get_process_image_base_files()

    for hash in hashes:
        for process in processes:
            if hash == hashlib.sha1(process[1]).hexdigest():
                print "Killing process %s" % (process[1])
                # Check if the process match the SHA1 funded in sec 1 & Kill process by PID
                os.kill(int(process[0]), signal.SIGTERM)


if __name__ == "__main__":
    main()
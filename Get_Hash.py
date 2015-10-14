#!/usr/bin/env python
########################################################################
#
#  Author: Hanan Cohen 
#
########################################################################



import os, sys
import subprocess
import hashlib
import argparse
import traceback
try:
    import psutils


############################ Vars #####################################


############################ Funcs ####################################

def convert2Hash(var):
    """
    """ 
        # Get hashes as argument 
    digester=hashlib.sha1()
    digester.update(hashVar.read())
    fileDigest= digester.hexdigest()
    return fileDigest


def get_proc_list_win():
    """
    """
        # Get process list (win)
    c = wmi.WMI ()
        for process in c.Win32_Process ():


def compare_Sha1_Sig(Var1, Var2):
    """
    """ 
        # Comare betwee the hashes and the processes base image 
    if Var1 != Var2:
        print "no process"
    else:
        ps_check(Var2)


def ps_check(seekitem):
    """
    """
        # Kill process if the base image file is match to the hashes  
    plist = psutil.get_process_list()
    str1=" ".join(str(x) for x in plist)
    if seekitem in str1:
        os.system('tskill %s' %seekitem)



############################## Main ################################### 

def main():
   sha1_list[]
   var=input('please enter sha1 ')
   sha1_list.append('var')

    proc = get_proc_list_win()

if __name__ == "__main__":
    main()

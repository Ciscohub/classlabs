#!/usr/bin/env python3

import pyexcel
import paramiko
import os
import datetime

def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read().decode('utf-8')

sshsession = paramiko.SSHClient()

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshsession.connect(hostname="10.10.2.3", username="bender", password="alta3")

x = "uptime"

timelog = (commandissue(x).lstrip().split(", "))
exctime = (timelog[0].split())
mylist = []
td = (datetime.datetime.today())
    
d = {"exec_time": exctime[0], "up_days": exctime[2], "up_hours_mins": timelog[1], "right_now": str(td)}
mylist.append(d)
pyexcel.save_as(records=mylist, dest_file_name="benderlog.xls") 
sshsession.close()

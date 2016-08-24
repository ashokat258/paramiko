import paramiko
import sys
import time

#setting parameters like host IP, username, passwd and number of iterations to gather cmds
HOST = "10.0.2.57"
USER = "ubuntu"
PASS = " "
ITERATION = 3
localpath='/home/ashok/hello'
remotepath='/home/ubuntu/hello'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
private_key = paramiko.RSAKey.from_private_key_file('new.pem')
client.connect(HOST,username=USER,password=PASS,pkey=private_key)
sftp = client.open_sftp()
sftp.put(localpath, remotepath)
(stdin, stdout, stderr) = client.exec_command('./home/ubuntu/hello')
print stdout.read();
(stdin, stdout, stderr) = client.exec_command('ifconfig')
print stdout.read()


print " new files is added\n"

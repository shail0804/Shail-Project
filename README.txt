Documentation
-------------

1)To Execute file name as ssh_multiple_server_in_parallel_Code.py follow the below instructions:

Prerequsite:
1)Python 2.7.x is required
2)cmd tool should be installed:This you can check by running the import cmd command at python CLI.
3)paramiko should e installed:This you can check by running the import paramiko command at python CLI.


sTEP TO INSTALL PARAMIKO for windows:
1)Install python-2.7.3.amd64.msi
2)Install pycrypto-2.6.win-amd64-py2.7.exe
3)Install setuptools-1.4.2.win-amd64-py2.7.exe
4)Install pip-1.4.1.win-amd64-py2.7.exe
5)Run pip install ecdsa
6)Download and extract https://github.com/paramiko/paramiko/archive/master.zip
7)Run setup.py install
8)Open IDLE, run import paramiko


sTEP TO INSTALL PARAMIKO for Linux:
Depending on the installation approaches :

https://code.google.com/p/robotframework-sshlibrary/wiki/InstallationInstructions#Installation

Paramiko and PyCrypto may be installed automatically by SSHLibrary.

If not automatically installed, you may use your distribution's package manager. For example on Debian variants, running sudo apt-get install python-paramiko should install them.

Alternatively, you can always install them using the source distributions from PyPI:

PyCrypto: https://pypi.python.org/pypi/pycrypto
Paramiko: https://pypi.python.org/pypi/paramiko


Read the following document for instruction

http://paramiko-www.readthedocs.org/en/latest/installing.html


4)Step to be followed:
a)Give command python <filename> to run the python file
  $python ssh_multiple_server_in_parallel_Code.py
b)Give following command to add the remote host to the list of IP adress available.
  ssh > add_host ip address,<username>,<password>
c)To connect to remote server give command:
  ssh > connect
d)Use Command "run <command>" to run the command.
  ssh > run ifconfig
e)Use command "close" to close the connection
  ssh > close

f)Use command "exit" to exit form cli.
  ssh > exit

Note:To Run the command in multiple server in parallel, add all the remote server IP address on which you want to execute code parrallel and then use command connect.

Ex -sample output

$python <filename>

ssh > add_host ip address1,username,password
ssh > add_host ip address2,username,password
ssh > connect
ssh > run uptime
host: ip address1:  18:06:20 up 6 days,  6:01,  3 users,  load average: 0.12, 0.12, 0.14
host: ip address2:  18:06:20 up 6 days,  6:01,  3 users,  load average: 0.12, 0.12, 0.14
ssh > close
ssh > exit


======================================================================================

2)To Run the file log_parsing_for_http_request_bash_script.sh

1)Use the command $ ./filename | sort | uniq -c     for unix
2)Use the command $ bash filename |sort | uniq -c    for bash shell

Ex-sample output:

$./log_parsing_for_http_request_bash_script.sh | sort | uniq -c
     39 HTTP 200
      1 HTTP 302
      2 HTTP 304
      5 HTTP 404
      3 HTTP 502
      1 Total number of HTTP 404 ERROR count in sample.log is : 5



=======================================================================================

3)To run the file word_series.py

$ python <filename.py>

EX-sample output

please enter the character: H
The Value of  H : 502  

Please enter a word: BANGALORE
for B value is 4
for A value is 1
for N value is 32752
for G value is 247
for A value is 1
for L value is 8178
for O value is 65519
for R value is 524268
for E value is 57
The sum of given words is:  631027  

Enter the number: 45787
The Word is:  NLKHGCCAAA  




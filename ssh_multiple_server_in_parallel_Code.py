#!/usr/bin/python

import paramiko
import cmd

class SSH(cmd.Cmd):
    """ Shell  interface to run a command on the host """

    prompt = 'ssh > '

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.hosts = []
        self.connections = []

    def do_add_host(self, args):
        """add_host
        Add the host to the host list"""
        if args:
            self.hosts.append(args.split(','))
            print('abc',self.hosts)
        else:
            print "usage: host "

    def do_connect(self, args):
        """Connect to all hosts in the hosts list"""
        for host in self.hosts:
            client = paramiko.SSHClient()
            #Any missing host key will be automaticaly added to the \
            #host file
            client.set_missing_host_key_policy(
                paramiko.AutoAddPolicy())
            client.connect(host[0],
                username=host[1],
                password=host[2])
            self.connections.append(client)


    def do_run(self, command):
        """run
        This function run's given command in all hosts in the list
        ex run <command>"""
        if command:
            for host, conn in zip(self.hosts, self.connections):
                stdin, stdout, stderr = conn.exec_command(command)
                stdin.close()
                for line in stdout.read().splitlines():
                    #print 'line',line
                    print 'host: %s: %s' % (host[0], line)
        else:
            print "usage: run "

    def do_close(self, args):
        """ This function close the connection from the remote host"""
        for conn in self.connections:
            conn.close()

    def do_exit(self, args):
        """This function allows user to exit from shell interface"""
        return -1


if __name__ == '__main__':
    SSH().cmdloop()

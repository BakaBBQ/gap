#!/usr/bin/env python

import urllib
import urllib2
import argparse
import spur
import os


parser = argparse.ArgumentParser(description="retrieve a file from a server")
parser.add_argument('server', metavar='server', help='server in favor of user@host')
parser.add_argument('file_url', metavar='file_url')
parser.add_argument('-n', metavar='filename', default='',help='the final filename of the downloaded file')
parser.add_argument('-p', metavar='password', help='ssh password', required=True)
args = parser.parse_args()


host = args.server.split('@')[1]
user = args.server.split('@')[0]
if '' == args.n:
    args.n = args.file_url.split('/')[-1]

def remote_retrieve_file():
    shell = spur.SshShell(hostname=host, username=user, password=args.p)
    with shell:
        com = """import urllib
urllib.urlretrieve('{url}', '{file}')
print 'finished'
        """

        com = com.format(url=args.file_url, file=args.n)
        print com
        result = shell.run(["python", '-c', com])
        print result.output


def curl_file():
    shell = spur.LocalShell()
    cmd = "curl -o {filename} sftp://{user}:{password}@{host}/~/{filename}".format(filename=args.n, user=user, host=host, password=args.p)
    os.system(cmd)
    print cmd

def clean_trash():
    shell = spur.SshShell(hostname=host, username=user, password=args.p)
    with shell:
        result = shell.run(["rm", args.n])
        print result.output

#the server will fetch the file
remote_retrieve_file()
#then your computer gets it from the server
curl_file()
#server trash cleanup
clean_trash()

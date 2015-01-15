Gap
=====================
A quick dirty download cli tool, wget + scp

```
usage: gap.py [-h] [-n filename] -p password server file_url

retrieve a file from a server

positional arguments:
server       server in favor of user@host
file_url

optional arguments:
-h, --help   show this help message and exit
-n filename  the final filename of the downloaded file
-p password  ssh password
```

###Primary Initiative
I have a VPN, and the VPN 60% is used for downloading blocked resources.
It just becomes more and more exasperating for just downloading a single file just to connect to VPN while I am yearning to play hisoutensoku or minecraft with others.
Thus recently I began to set my vps to wget a file first, then I retrieve it via sftp.
Therefore the script you see here is the python script version of it.

###Problems / Possible New Features
passwords in cli arguments
caching the default server would be nice
_synchronously let the server and client retrieve files_ would be extremely nice
add to pip
maybe get rid of the "curl"


###Notables
Currently only works on curl with sftp enabled
Very dirty, sordid, or whatever you want to call in code, bunch of hacked up code


###License
MIT

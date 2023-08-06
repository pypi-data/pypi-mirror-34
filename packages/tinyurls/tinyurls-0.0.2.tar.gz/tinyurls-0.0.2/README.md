# tinyurls

URL shortening service to be used in a microservices environment.

This service does the following:
1. Takes a long url and stores an md5 key and the url in a database table. 
The md5 key is used to lookup the long url. This step returns an short link 
with md5.
2. Takes a short link and redirects you to the long link.





## Installation
Use virtual environment
```bash
virtualenv env
source env/bin/activate

```
Change into tinyurls directory and install
```
cd tinyurls
python setup.py install 

```

## Execute
```bash
tinyurls -h
usage: tinyurls [-h] [-p PORT] [-d DATABASE]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Port used for this service
  -d DATABASE, --database DATABASE Database to use


tinyurls -p 8888
```





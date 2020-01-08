
## Access_Log Processing in Python

- logparser.py
  
  - This  module will parse access_log fields and return as dict.

  - #### logline before parsing
  ```
  109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0"
  ```
  - #### logline after parsing
  ```
  {'host': '109.169.248.247', 'identity': '-', 'user': '-', 'time': '12/Dec/2015:18:25:11 +0100', 'request': 'POST /administrator/index.php HTTP/1.1', 'status': '200', 'size': '4494', 'referer': 'http://almhuette-raith.at/administrator/', 'agent': 'Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0'}
  ```

## Example:

```
$ python3 ipcounter.py access_log 250
```
```
37.1.206.196         : 534
213.150.254.81       : 434
148.251.50.49        : 1929
178.191.155.244      : 284
84.112.161.41        : 712
52.22.118.215        : 734
91.200.12.22         : 287
205.167.170.15       : 15695
79.142.95.122        : 3207
```
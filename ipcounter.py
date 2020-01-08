import logparser
import os
import sys


USAGE = "python3 ipcounter.py /path/to/access.log  minimum_count"

arguments = sys.argv

if len(arguments) == 3:

  log = arguments[1]
  mcount = arguments[2]

 
  if not os.path.isfile(log):

    print('Not a valid file {}.'.format(log))
    sys.exit(1)

  if not mcount.isdigit():
    
    print('Not a valid digit {}'.format(mcount)) 
    sys.exit(1)

  #############################################################
  # Counting Client ip address
  #############################################################
  ipCounter = {}
  fh = open(log)
  for logLine in fh:
    
    logFields = logparser.parser(logLine)
    clientIp = logFields['host']

    if clientIp not in ipCounter:
    
      ipCounter[clientIp] = 1
   
    else:

      ipCounter[clientIp] = ipCounter[clientIp] + 1

  ############################################################
  # Printing Result
  #############################################################

  
  for ip in ipCounter:
    
    hit = ipCounter[ip]
    if hit >= int(mcount):

      print('{:20} : {}'.format(ip,hit))

else:
  print(USAGE)





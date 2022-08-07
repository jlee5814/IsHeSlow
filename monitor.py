touch monitor.py

import speedtest
s = speedtest.Speedtest()
while True:
  print(s.download(), s.upload())
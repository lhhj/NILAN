# pycts602api.py must be somewhere in PATH
from pycts602api import CTS602API

m = CTS602API('/dev/ttyUSB0') # change appropriately
data = m.get_realtime_data()
data1 =m.get_all_realtime_data()
print data1

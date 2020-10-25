# pycts602api.py must be somewhere in PATH
from pycts602api import CTS602API

m = CTS602API('/dev/ttyUSB0') # change appropriately
data = m.get_realtime_data()
# print out humidity (%)
#turn on genvex
#m.turn_on()
m.set_vent_step(2)
#set temp
m.set_user_temp(19)
m.reset_alarm()
m.turn_on()

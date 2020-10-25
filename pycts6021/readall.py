# pycts602api.py must be somewhere in PATH
from pycts602api import CTS602API

m = CTS602API('/dev/ttyUSB0') # change appropriately
data = m.get_all_realtime_data()
# print out humidity (%)
print data
print 'filter:', data['filter_alarm']['value']
print 'boiling:',data['boiling']['value']
print 'board_temp:',data['board_temp']['value']
print 'intake_temp:',data['intake_temp']['value']
print 'condenser_temp:',data['condenser_temp']['value']
print 'evaporator_temp:',data['evaporator_temp']['value']
print 'inlet_temp:',data['inlet_temp']['value']
print 'outdoor_temp:',data['outdoor_temp']['value']
print 'outlet_temp:',data['outlet_temp']['value']
print 'water_top_temp:',data['water_top_temp']['value']
print 'water_bottom_temp:',data['water_bottom_temp']['value']
print 'panel_temp:',data['panel_temp']['value']
print 'humidity:',data['humidity']['value']
print 'status:',data['status']['value']
print 'status_time:',data['status_time']['value']
print 'is_summer:',data['is_summer']['value']
print 'display_text:',data['display_text']
print 'exhaust_speed:',data['exhaust_speed']['value']
print 'inlet_speed:',data['inlet_speed']['value']
print data['running']['value']
print data['mode']['value']
print data['vent_step']['value']
print data['air_set_temp']['value']
print data['water_set_temp']['value']
#m.turn_on()

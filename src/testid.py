    """ 
    testing canbus ids to see if it works
    """
import os
import can
import logging

#check system name, in linux will print 'posix' and in windows will print 'nt'
print(os.name)
logging.debug("CanBus Testing starting...")

logging.debug("CanBus Starting can network...")
os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')
logging.debug('Canbus Started...')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')
logging.debug('Canbus data thats being sent is id: 0x620 bytes: 00,00,01,00,00,00,00')
msg = can.Message(arbitration_id=0x620, data=[00, 00, 01, 00,00,00,00], extended_id=False)
for i in range(50):
    can0.send(msg)
    print('sent messag about'+i)
    logging.debug('message sent')

logging.debug("test completed")
os.system('sudo ifconfig can0 down')

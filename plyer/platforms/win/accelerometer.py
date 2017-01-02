'''
'Windows' accelerometer
---------------------
A dummy accelerometer for phone emulation
'''

from plyer.facades import Accelerometer
from sensor_simulate import SemiRandomData
# from multiprocessing import Process, Manager
from threading import Thread
import time
import sys


class AccelerometerSensorListener(object):

    def __init__(self):
        self.sensor = 'DummySensorObj'
        # manager = Manager()
        # self.values = manager.list([None, None, None])
        self.values = [None, None, None]
        # self.state = manager.Value('is_enabled', False)
        self.state = False

    def enable(self):
        # self.state.value = True
        self.value = True
        # self.process_get_data = Process(target=self.get_data)
        self.process_get_data = Thread(target=self.get_data)
        self.process_get_data.start()

    def disable(self):
        # self.state.value = False
        self.value = False

    def get_data(self):
        sps_obj = SemiRandomData(3, 3, 9.8, .02)
        # while self.state.value is True:
        while self.value is True:
            a, b, c = sps_obj.get_value()
            self.values[0] = a
            self.values[1] = b
            self.values[2] = c
            time.sleep(.01)

    def monitor(self, time_length=10, frequency=1):
        for i in range(time_length):
            time.sleep(frequency)
            sys.stdout.write(str(self.values) + '\n')
            sys.stdout.flush()


class WinAccelerometer(Accelerometer):
    def __init__(self):
        super(WinAccelerometer, self).__init__()
        self.bState = False

    def _enable(self):
        if (not self.bState):
            self.listener = AccelerometerSensorListener()
            self.listener.enable()
            self.bState = True

    def _disable(self):
        if (self.bState):
            self.bState = False
            self.listener.disable()
            del self.listener

    def _get_acceleration(self):
        if (self.bState):
            return tuple(self.listener.values)
        else:
            return (None, None, None)

    def __del__(self):
        if(self.bState):
            self._disable()
        super(self.__class__, self).__del__()


def instance():
    return WinAccelerometer()

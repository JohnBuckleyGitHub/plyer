'''
'Windows' pressure sensor
---------------------
A dummy pressure sensor for phone emulation
'''

from plyer.facades import Pressure
from sensor_simulate import SemiRandomData
# from multiprocessing import Process, Manager
from threading import Thread
import time
import sys


class PressureSensorListener(object):

    def __init__(self):
        self.sensor = 'DummySensorObj'
        # manager = Manager()
        # self.values = manager.list([None, None, None])
        self.values = [None, None, None]
        # self.state = manager.Value('is_enabled', False)
        self.state = False

    def enable(self):
        # self.state.value = True
        self.state = True
        # self.process_get_data = Process(target=self.get_data)
        self.process_get_data = Thread(target=self.get_data)
        self.process_get_data.start()

    def disable(self):
        # self.state.value = False
        self.state = False

    def get_data(self):
        srd_obj = SemiRandomData(3, 3, 1000, .05)
        # while self.state.value is True:
        while self.state is True:
            a, b, c = srd_obj.get_value()
            self.values[0] = a
            self.values[1] = b
            self.values[2] = c
            time.sleep(.01)

    def monitor(self, time_length=10, frequency=1):
        for i in range(time_length):
            time.sleep(frequency)
            sys.stdout.write(str(self.values) + '\n')
            sys.stdout.flush()


class WinPressure(Pressure):
    def __init__(self):
        super(WinPressure, self).__init__()
        self.bState = False

    def _enable(self):
        if (not self.bState):
            self.listener = PressureSensorListener()
            self.listener.enable()
            self.bState = True

    def _disable(self):
        if (self.bState):
            self.bState = False
            self.listener.disable()
            del self.listener

    def _get_pressure(self):
        if (self.bState):
            return tuple(self.listener.values)
        else:
            return (None, None, None)

    def __del__(self):
        if(self.bState):
            self._disable()
        super(self.__class__, self).__del__()


def instance():
    return WinPressure()

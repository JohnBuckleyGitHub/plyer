class Pressure(object):
    '''Pressure facade.

    .. versionadded:: 1.xxx
    '''

    @property
    def pressure(self):
        '''Property that returns values of the current Pressure sensor, currently as
        three part tuple. Returns (None, None, None) if no data is currently
        available.
        '''
        return self.get_pressure()

    def enable(self):
        '''Activate the Pressure sensor.
        '''
        self._enable()

    def disable(self):
        '''Disable the Pressure sensor.
        '''
        self._disable()

    def get_pressure(self):
        return self._get_pressure()

    # private

    def _enable(self):
        raise NotImplementedError()

    def _disable(self):
        raise NotImplementedError()

    def _get_pressure(self):
        raise NotImplementedError()

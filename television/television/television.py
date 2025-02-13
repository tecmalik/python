class Television:
    def __init__(self):
        self._is_on = False
        self._volume = 50
        self._channel = 1
        self.initial_volume = 0

    @property
    def is_on(self)->bool:
        return self._is_on
    def turn_on(self):
        self._is_on = True
    def turn_off(self):
         self._is_on = False

    def increase_volume(self):
        if self._is_on == False:
            raise Exception('Television is not turned on')
        if self._volume == 100:
            raise Exception('Maximum Volume is 100')
        self._volume+=10
    @property
    def volume(self):
        return self._volume

    def decrease_volume(self):
        if self._is_on == False:
            raise Exception('Television is not turned on')
        if self._volume == 0:
            raise Exception('Minimum Volume is 0')
        self._volume-=10

    def mute(self):
        if self._is_on == False:
            raise Exception('Television is not turned on')
        self.initial_volume = self._volume
        self._volume = 0

    def unmute(self):
        if self._is_on == False:
            raise Exception('Television is not turned on')
        self._volume = self.initial_volume

    def channel_up(self):
        if self._is_on == False:
            raise Exception('Television is not turned on')
        if self._channel == 10:
            raise Exception('Maximum Channel Level is 10')
        self._channel += 1

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel_level):
        if self._is_on == False:
            raise Exception('Television is not turned on')
        if channel_level > 10:
            raise Exception('Maximum Channel Level is 10')
        if channel_level <= 0:
            raise Exception('Minimum Channel Level is 0')
        self._channel = channel_level

    def channel_down(self):
        if self._is_on == False:
            raise Exception('Television is not turned on')
        if self._channel == 1:
            raise Exception('Maximum Channel Level is 10')
        self._channel -= 1

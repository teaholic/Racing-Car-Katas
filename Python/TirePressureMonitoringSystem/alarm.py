class Alarm(object):

    def __init__(self, is_on: bool = False):
        self.is_on = is_on

    def set(self):
        return Alarm(is_on=True)
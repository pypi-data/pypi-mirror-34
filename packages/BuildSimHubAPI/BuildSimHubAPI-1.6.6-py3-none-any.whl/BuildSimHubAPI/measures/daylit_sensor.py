from .model_action import ModelAction


class DaylightingSensor(ModelAction):
    def __init__(self):
        ModelAction.__init__(self, 'daylight_sensor')
        self._default_list = [1, 0]
        self._data = 1

    def get_num_value(self):
        return ModelAction.num_of_value(self)

    def set_datalist(self, datalist):
        # this is just a on off option
        ModelAction.set_datalist(self, self._default_list)

    def set_data(self, data):
        if data != 1 and data != 0:
            return False
        else:
            ModelAction.set_data(self, data)

    def set_min(self, min_val):
        ModelAction.set_min(self, 0)

    def set_max(self, max_val):
        ModelAction.set_max(self, 1)

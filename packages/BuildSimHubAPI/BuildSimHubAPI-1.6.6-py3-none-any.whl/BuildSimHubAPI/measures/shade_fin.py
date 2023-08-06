from .model_action import ModelAction

'''
Measures to add fin to the model

if the model has fins, it will change the fins depth
to the specified values
if the mode has no fins, it will add fins to the left and right side of the building with the specified 
depth.

This measure applies to windows for all orientations

'''


class ShadeFin(ModelAction):
    # this shows the ip to si conversion rate
    # if unit is 'ip', then multiply this rate.
    # for ft to meter
    # The conversion will change ft to m if ip shows
    CONVERSION_RATE = 3.28084

    def __init__(self, unit="si", orientation=None):

        if orientation is None:
            ModelAction.__init__(self, 'window_fin', unit)
        else:
            orientation = orientation.lower()
            if orientation == 'w':
                ModelAction.__init__(self, 'window_fin_w', unit)
            elif orientation == 'e':
                ModelAction.__init__(self, 'window_fin_e', unit)
            elif orientation == 's':
                ModelAction.__init__(self, 'window_fin_s', unit)
            elif orientation == 'n':
                ModelAction.__init__(self, 'window_fin_n', unit)
            else:
                ModelAction.__init__(self, 'window_fin', unit)

    def get_num_value(self):
        return ModelAction.num_of_value(self)

    def set_datalist(self, datalist):
        if ModelAction.unit(self) == 'ip':
            for i in range(len(datalist)):
                datalist[i] = datalist[i] / ShadeFin.CONVERSION_RATE
        ModelAction.set_datalist(self, datalist)

    def set_data(self, data):
        if ModelAction.unit(self) == 'ip':
            data = data / ShadeFin.CONVERSION_RATE
        ModelAction.set_data(self, data)

    def set_min(self, min_val):
        if ModelAction.unit(self) == 'ip':
            min_val = min_val / ShadeFin.CONVERSION_RATE
        ModelAction.set_min(self, min_val)

    def set_max(self, max_val):
        if ModelAction.unit(self) == 'ip':
            max_val = max_val / ShadeFin.CONVERSION_RATE
        ModelAction.set_max(self, max_val)
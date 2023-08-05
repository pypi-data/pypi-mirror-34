"""This module contains classes of graphoelements.

These graphoelements can be generated by the package "detect".

"""
from copy import deepcopy

from numpy import empty, asarray, sum, mean

from .datatype import Data


class Graphoelement:
    """Class containing all the events of one type in one dataset.

    Attributes
    ----------
    chan_name : ndarray (dtype='U')
        list of channels
        
    """
    def __init__(self):
        self.chan_name = None
        self.events = []

    def __iter__(self):
        for one_event in self.events:
            yield one_event
            
    def __len__(self):
        return len(self.events)
    
    def __getitem__(self, index):
        return self.events[index]

    def __call__(self, func=None):

        events = []
        for one_ev in self.events:
            if func(one_ev):
                events.append(one_ev)

        output = deepcopy(self)
        output.events = events

        return output

    def to_data(self, parameter, operator=mean):

        data = Data()
        data.axis = {'chan': empty(1, dtype='O')}
        data.axis['chan'][0] = self.chan_name
        data.data = empty(1, dtype='O')

        values = []
        for one_chan in self.chan_name:
            if parameter == 'count':
                value = sum(1 for x in self.events if x['chan'] == one_chan)
            else:
                value = operator([x[parameter] for x in self.events
                                  if x['chan'] == one_chan])
            values.append(value)

        data.data[0] = asarray(values)
        return data
    
    def to_annot(self, annot, name):
        """Write events to Annotations file.
        
        Parameters
        ----------
        filename : instance of Annotations
            Annotations file
        name : str
            name for the event type        
        """
        for one_ev in self.events:
            annot.add_event(name,
                            (one_ev['start'], one_ev['end']),
                            chan=one_ev['chan'])


class Ripple(Graphoelement):
    def __init__(self):
        super().__init__()
        pass


class SlowWaves(Graphoelement):
    """Class containing all the slow waves in one dataset.

    Attributes
    ----------
    events : list of dict
        list of slow waves, where each SW contains:
            - start_time : float
                start time of the SW
            - trough_time : float
                time of the lowest value
            - zero_time : float
                time of the neg to pos zero-crossing
            - peak_time : float
                time of the highest value
            - end_time : float
                end time of the SW
            - trough_val : float
                the lowest value
            - peak_val : float
                the highest value
            - dur: float
                duration of the SW
            - area_under_curve : float
                sum of all values divided by duration
            - ptp : float
                peak-to-peak (difference between highest and lowest value)
            - chan': str
                channel label
    
    """
    def __init__(self):
        super().__init__()
        
        one_sw = {'start_time': None,
                  'trough_time': None,
                  'zero_time': None,
                  'peak_time': None,
                  'end_time': None,
                  'trough_val': None,
                  'peak_val': None,
                  'dur': None,
                  'area_under_curve': None,
                  'ptp': None,
                  'chan': [],
                  }
        self.events.append(one_sw)


class Spindles(Graphoelement):
    """Class containing all the spindles in one dataset.

    Attributes
    ----------
    mean : ndarray (dtype='float')
        mean of each channel
    std : ndarray (dtype='float')
        standard deviation of each channel
    det_value : ndarray (dtype='float')
        value used for detection for each channel
    sel_value : ndarray (dtype='float')
        value used for selection for each channel
    events : list of dict
        list of spindles, where each spindle contains:
            - start_time : float
                start time of the spindle
            - end_time : float
                end time of the spindle
            - peak_time : float
                time of the highest value
            - peak_val : float
                the highest value
            - chan': str
                channel label

    """
    def __init__(self):
        super().__init__()
        self.mean = None
        self.std = None
        self.det_value = None
        self.sel_value = None
        self.density = None

        one_spindle = {'start_time': None,
                       'end_time': None,
                       'chan': [],
                       'peak_val': None,
                       'peak_time': None,
                       }
        self.events.append(one_spindle)

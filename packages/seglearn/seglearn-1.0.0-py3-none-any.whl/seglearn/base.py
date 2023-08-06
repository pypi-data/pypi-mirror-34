'''
This module has some base classes for time series data
'''

# Author: David Burns
# License: BSD

class TS_Data(object):
    '''
    Iterable/indexable class for time series data with context data
    Numpy arrays are sufficient time series data alone is needed

    Parameters
    ----------
    ts_data : array-like, shape (N, )
        time series data
    context_data : array-like (N, )
        contextual data

    '''

    def __init__(self, ts_data, context_data, sample_period = 1):
        N = len(ts_data)
        # assert len(context_data) == N
        self.ts_data = ts_data
        self.context_data = context_data
        self.sample_period = 1
        self.index = 0
        self.N = N
        self.shape = [N] # need for safe_indexing with sklearn

    def __iter__(self):
        return self

    def __getitem__(self, indices):

        return TS_Data(self.ts_data[indices], self.context_data[indices])

    def __next__(self):
        if self.index == self.N:
            raise StopIteration
        self.index = self.index +1
        return TS_Data(self.ts_data[self.index], self.context_data[self.index])

    def __len__(self):
        return self.N


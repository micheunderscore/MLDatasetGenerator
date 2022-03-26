import time
from enum import Enum, unique

import numpy as np
import numpy.random as rand
import pandas as pd


@unique
class outType(Enum):
    BOOL = 0
    INT = 1
    FLOAT = 2

# Random date generator
def str_time_prop(start, end, time_format, prop):

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

def genDataset (varName = 'var', varCount = 1, dataCount = 100, target = 'target', outputDType = outType.BOOL) -> pd.DataFrame:
    """genDataset(varName = 'var', varCount = 1, dataCount = 100, target = 'target', outputDType = outType.BOOL) -> pd.DataFrame
    
    Generates a new dataset

    varName -- Name of dataset features (default: 'var')
    varCount -- Number of features in dataset (default: 1)
    dataCount -- Number of data to be generated (default: 100)
    target -- Name of target feature (default: 'target')
    outputDType -- Data type of target feature (default: outType.BOOL)
    """

    timestamp = {'timestamp': [random_date("1/1/2008 1:30 PM", "12/31/2020 4:50 AM", rand.random()) for i in range(dataCount)]}
    
    columns = {}

    # I have no idea why I did it this way
    minMax = np.zeros((varCount, 2), dtype=int)

    for i in range(varCount):
        minMax[i, 0] = abs(rand.randint(0, 9*11))
        minMax[i, 1] = rand.randint(0, minMax[i, 0])
        columns[f'{varName}{i + 1}'] = [rand.uniform(minMax[i, 0], minMax[i, 1]) for n in range(dataCount)]

    targetCol = dataCount * [0]
    operations = [rand.randint(0, 2) for i in range(varCount)]

    for i in range(dataCount):
        val = 0
        for j, ele in enumerate(columns):
            if (operations[j] == 0):
                val += columns[ele][i]
            elif (operations[j] == 1):
                val -= columns[ele][i]

        if (outputDType == outType.BOOL):
            targetCol[i] = 0 if np.ceil(val) % 2 == 0 else 1
        elif (outputDType == outType.INT):
            targetCol[i] = np.ceil(val)
        elif (outputDType == outType.FLOAT):
            targetCol[i] = val

    columns[target] = targetCol

    return pd.DataFrame({**timestamp, **columns})

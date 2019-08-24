# syshie

import math
import random
import numpy as np
import scipy as sp
import sklearn as sk
import pandas as pd
import statsmodels as sm
import matplotlib.pyplot as plt
import seaborn as sns


def version():
    mods = ['np', 'sp', 'sk', 'pd', 'sm', 'sns']
    for mod in mods:
        print(mod + ': ', eval(mod).__version__)


if __name__ == '__main__':
    version()

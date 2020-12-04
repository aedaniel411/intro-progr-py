import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

datos = pd.read_excel('datos02.xlsx')

print (datos['fuerza'])

"""Model"""
import numpy as np
import pymc3 as pm

class Model:
    def __init__(x: np.ndarray, y: np.ndarray):
        self.x = x
        self.y = y



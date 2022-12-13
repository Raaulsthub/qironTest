import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class SentimentPlotter:
    def __init__(path):
        self.path = path
        self.data = pd.read_csv(path)
    
    def update():
        self.data = pd.read_csv(self.path)

    def plot():
        # plot function based on time (saved on memory) or y axis np simple array
        # to decide yet
        pass
    
    

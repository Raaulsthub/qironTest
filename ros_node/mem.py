# SENTIMENT MEMORY FOR PLOTTING
import pandas as pd
from datetime import datetime

# consists in a list of tuples indicating a certain face expression and it's predicted confidence
class Memory:
    def __init__(self):
        self.mem = []

    def save_expression(self, expression, confidence, time):
        self.mem.append((expression, confidence, time))

    def save(self, file_name):
        data = pd.DataFrame(self.mem)
        data.to_csv('./saved_analysis/' + file_name)
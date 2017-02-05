import pandas as pd
from matplotlib import pyplot as plt
from abc import ABCMeta, abstractmethod


class Plot(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        plt.show()


class CsvPlot(Plot):
    def __init__(self, parent_path):
        self.parent_path = parent_path

    def show(self, is_execute=False):
        super().show() if is_execute else None

    def plot(self, file_name, title, is_execute=False):
        (lambda f, t: pd.read_csv(self.parent_path.format(f)).plot(title=t))(
            file_name, title)
        self.show(is_execute)

    def plots(self, file_names, titles, is_execute=False):
        [self.plot(f, t) for f, t in zip(file_names, titles)]
        self.show(is_execute)

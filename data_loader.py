import pandas as pd
import json
import requests
import matplotlib.pyplot as plt

class DataLoader:
    @staticmethod
    def load_csv(filepath):
        return pd.read_csv(filepath)
    
    @staticmethod
    def load_json(filepath):
        return pd.read_json(filepath)
    
    @staticmethod
    def load_api(url):
        response = requests.get(url)
        data = response.json()
        return pd.DataFrame(data)

class DataVisualizer:
    def __init__(self):
        self.figures = []

    def add_histogram(self, data, column, title="Histogram", xlabel="Value", ylabel="Frequency"):
        fig, ax = plt.subplots()
        ax.hist(data[column].dropna())
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        self.figures.append(fig)

    def add_line_plot(self, data, x_column, y_column, title="Line Plot", xlabel="X-axis", ylabel="Y-axis"):
        fig, ax = plt.subplots()
        ax.plot(data[x_column], data[y_column])
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        self.figures.append(fig)

    def add_scatter_plot(self, data, x_column, y_column, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
        fig, ax = plt.subplots()
        ax.scatter(data[x_column], data[y_column])
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        self.figures.append(fig)

    def remove_last_visualization(self):
        if self.figures:
            self.figures.pop()

    def show_visualizations(self):
        for fig in self.figures:
            fig.show()

class DataCleaner:
    @staticmethod
    def count_missing_values(data):
        return data.isna().sum()
    
    @staticmethod
    def report_missing_values(data):
        missing_values = DataCleaner.count_missing_values(data)
        total_missing = missing_values.sum()
        total_values = data.size
        percent_missing = (total_missing / total_values) * 100
        
        report = f"Missing Values Report:\n\n{missing_values}\n\n"
        report += f"Total Missing Values: {total_missing}\n"
        report += f"Total Values: {total_values}\n"
        report += f"Percentage of Missing Values: {percent_missing:.2f}%"
        
        return report
    
    @staticmethod
    def fill_missing_values(data, method='mean'):
        if method == 'mean':
            return data.fillna(data.mean())
        elif method == 'median':
            return data.fillna(data.median())
        elif method == 'mode':
            return data.fillna(data.mode().iloc[0])
        else:
            raise ValueError("Method must be 'mean', 'median', or 'mode'")

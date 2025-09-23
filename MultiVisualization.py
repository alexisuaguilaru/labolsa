from pathlib import Path
import matplotlib.pyplot as plt
import re

def GetDataFromFile(
        FileName
    ):

    AveragePricesStock = []
    with open(FileName,'r') as data_file:
        for line_row in data_file.readlines():
            if line_row.startswith('MEX1'):
                values = re.split(r'\s+',line_row.strip())
                AveragePricesStock.append(float(values[3]))

    return AveragePricesStock

if __name__ == '__main__':
    folder = Path('.')
    fig , axes = plt.subplots()
    for file in folder.iterdir():
        if file.name[-3:] == 'dat':
            AveragePrices = GetDataFromFile(file.name)
            if AveragePrices:
                axes.plot(AveragePrices)

    fig.savefig('MultiPlot.png')
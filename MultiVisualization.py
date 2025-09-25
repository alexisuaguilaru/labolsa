from pathlib import Path
import matplotlib.pyplot as plt
import re
from numpy import mean

def GetDataFromFile(
        FileName
    ):

    AveragePricesStock = []
    average = None
    with open(FileName,'r') as data_file:
        for line_row in data_file.readlines():
            if line_row.startswith('#CODE'):
                if average:
                    AveragePricesStock.append(mean(average))
                else:
                    average = []
            elif line_row.startswith('MEX'):
                values = re.split(r'\s+',line_row.strip())
                average.append(float(values[3]))

    return AveragePricesStock

if __name__ == '__main__':
    folder = Path('.')
    NameParameters = iter(range(10,110,10))
    fig , axes = plt.subplots()
    for file in folder.iterdir():
        if file.name[-3:] == 'dat':
            AveragePrices = GetDataFromFile(file.name)
            if AveragePrices:
                axes.plot(
                    AveragePrices,
                    label = f"{next(NameParameters)}",
                )

    axes.set_xlabel('Iterations')
    axes.set_ylabel('Average Price')
    axes.legend(title='Numero Compañías')
    axes.set_title("Experimentos Variando el  Número de Compañías")

    fig.savefig('MultiPlot.png')
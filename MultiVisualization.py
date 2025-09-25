from pathlib import Path
import matplotlib.pyplot as plt
import re
from numpy import mean , std , log10 , apply_along_axis

def GetDataFromFile(
        FileName
    ):

    AveragePricesStock = []
    average = []
    with open(FileName,'r') as data_file:
        for line_row in data_file.readlines():
            if line_row.startswith('#CODE'):
                if average:
                    AveragePricesStock.append(mean(average))
                    average = []
            elif line_row.startswith('MEX'):
                values = re.split(r'\s+',line_row.strip())
                average.append(float(values[3]))

    return AveragePricesStock

if __name__ == '__main__':
    folder = Path('.')
    NameParameters = 10,20,50,100,200,500,1000,2000,5000,10000
    fig , axes = plt.subplots()
    StdSimulation = []
    StdParameters = []
    for file in folder.iterdir():
        if file.name[-3:] == 'dat':
            index_parameter = int(file.name[4:-4])
            AveragePrices = GetDataFromFile(file.name)
            value_parameter = NameParameters[index_parameter-1]
            if AveragePrices:
                axes.plot(
                    apply_along_axis(log10,0,AveragePrices,),
                    label = value_parameter,
                )
                StdSimulation.append(std(AveragePrices,ddof=1))
                StdParameters.append(value_parameter)

    axes.set_xlabel('Iterations')
    axes.set_ylabel('Log10(Average Price)')
    axes.legend(title='Numero Compañías')
    axes.set_title("Experimentos Variando el  Número de Compañías")

    fig.savefig('MultiPlot.png')

    fig , axes = plt.subplots()
    axes.bar(StdParameters,StdSimulation,width=5)
    axes.set_xlabel('Numero de Compañías')
    axes.set_ylabel('Volatilidad')
    axes.set_title('Experimentos Variando el  Número de Compañías')
    fig.savefig('VolatilidadPlot.png')
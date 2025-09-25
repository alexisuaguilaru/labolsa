import subprocess
from itertools import product

def RunSimulation(
        name,
        companies,
        users,
        orders,
        stock_value,
        n_stock,
        cash,
        max_iter,
        Experiment,
    ):

    try:
        print(f'./labolsa {name} {companies} {users} {orders} {stock_value} {n_stock} {cash} {max_iter} > test{Experiment}.dat')
        subprocess.run(
            f'./labolsa {name} {companies} {users} {orders} {stock_value} {n_stock} {cash} {max_iter} > test{Experiment}.dat',
            shell = True,
            timeout = 10,
        )
        result_execution = 0
    except:
        result_execution = -1
    
    return result_execution

def GridParameters(
        ParametersList: list[list],
    ):

    return enumerate(product(*ParametersList),1)

def MainExecution(
        SpaceOfParameters,
    ):

    Exitosos = 0
    for num_experiment , parameters in GridParameters(SpaceOfParameters):
        result = RunSimulation(
            *parameters,
            Experiment = num_experiment,
        )

        Exitosos += 1 if result == 0 else 0

    return Exitosos , num_experiment-Exitosos

if __name__ == '__main__':
    SpaceOfParameters = [
        ['MEX'],
        [10,20,50,100,200,500,1000,2000,5000,10000],
        [100],
        [20_000],
        [100],
        [100],
        [20_000],
        [100],
    ]

    Exitosos , Fallidos = MainExecution(SpaceOfParameters)

    print(f'Exitosos :: {Exitosos}\nFallidos :: {Fallidos}')
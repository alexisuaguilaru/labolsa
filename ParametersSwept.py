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

    return product(*ParametersList)

def MainExecution(
        SpaceOfParameters,
    ):

    Exitosos = 0
    for num_experiment , parameters in enumerate(GridParameters(SpaceOfParameters),1):
        result = RunSimulation(
            *parameters,
            Experiment = num_experiment,
        )

        Exitosos += 1 if result == 0 else 0

    return Exitosos , num_experiment-Exitosos

if __name__ == '__main__':
    SpaceOfParameters = [
        ['MEX'],
        range(10,100),
        [100],
        [1000],
        [20],
        [100],
        [500],
        [10],
    ]

    Exitosos , Fallidos = MainExecution(SpaceOfParameters)

    print(f'Exitosos :: {Exitosos}\nFallidos :: {Fallidos}')
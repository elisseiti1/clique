# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Clique import Clique
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = np.array([
        [0.45660137634625386, 0.43280640922410835],
        [0.6113784672224188, 0.5286245988894975],
        [0.45029897412145387, 0.7116061205092745],
        [0.6390150501606866, 0.46074398219372076],
        [0.6289567839292338, 0.32346951478531516]
        ])
    number_data_points = np.shape(a)[0]

    clique = Clique(xi=3, tau=0.2, pruning=False)
    clique.fit(data=a)
    # print(clique.generate_oneDimensionalUnits())
    clique.run_clique()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

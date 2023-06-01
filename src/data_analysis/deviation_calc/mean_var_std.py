import numpy as np


def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  else:
    matrixList = np.reshape(list, (3, 3))
    print(matrixList)
    calculations = {'mean': 0}
    calculations['mean'] = [
      matrixList.mean(axis=0).tolist(),
      matrixList.mean(axis=1).tolist(),
      matrixList.flatten().mean().tolist()
    ]      
    print(calculations)
    calculations['variance'] = [
      matrixList.var(axis=0).tolist(),
      matrixList.var(axis=1).tolist(),
      matrixList.flatten().var().tolist()
    ]
    calculations['standard deviation'] = [
      matrixList.std(axis=0).tolist(),
      matrixList.std(axis=1).tolist(),
      matrixList.flatten().std().tolist()
    ]
    calculations['max'] = [
      matrixList.max(axis=0).tolist(),
      matrixList.max(axis=1).tolist(),
      matrixList.flatten().max().tolist()
    ]
    calculations['min'] = [
      matrixList.min(axis=0).tolist(),
      matrixList.min(axis=1).tolist(),
      matrixList.flatten().min().tolist()
    ]
    calculations['sum'] = [
      matrixList.sum(axis=0).tolist(),
      matrixList.sum(axis=1).tolist(),
      matrixList.flatten().sum().tolist()
    ]

  return calculations

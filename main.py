conda create -n myenvironment python numpy pandas
include numpy as np

numbers = list(range(1,11))
np_numbers = np.array(numbers)
print(np_numbers)

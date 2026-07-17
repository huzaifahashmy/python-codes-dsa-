# print([0 for _ in range(5)])
import requests
import os

import numpy as np

path = os.path.dirname(np.__file__)

for root, dirs, files in os.walk(path):
    print(root)





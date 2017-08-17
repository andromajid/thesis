from __future__ import print_function
import numpy as np
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
import file_operation.file
import os
file = os.path.dirname(os.path.realpath(__file__)) + "/access.log_2017-08-17_003600_2017-08-17_123600.log"


for chunk in file_operation.file.read_file_in_chunk(file):
    print(chunk)




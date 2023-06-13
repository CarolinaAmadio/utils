import pandas as pd
import glob
import os
import numpy as np

# Get data file names
path = '/g100_scratch/userexternal/camadio0/VALIDAZIONE_RUN_CMEMS_scripts/VALIDAZIONE_FLOAT/NEW_O2O_VALIDATION/O2_VALIDATION/'
filenames = glob.glob(path + "/O2o*.csv")
df = []
for filename in filenames:
    df.append(pd.read_csv(filename))
# Concatenate all data into one DataFrame
frame = pd.concat(df, ignore_index=True)


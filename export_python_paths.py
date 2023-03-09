import sys
import pandas as pd
from platform import python_version


print(python_version())

paths = sys.path
df = pd.DataFrame({'paths':paths})
df.to_csv('./qgis_sys_paths.csv', index=False)


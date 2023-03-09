import sys
import pandas as pd
paths = sys.path
df = pd.DataFrame({'paths':paths})
df.to_csv('./qgis_sys_paths.csv', index=False)
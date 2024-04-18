# importing pandas as pd
import pandas as pd

# read an excel file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_excel("myexcel.xlsx"))

# show the dataframe
print(df.head)

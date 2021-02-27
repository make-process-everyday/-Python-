import json
import pandas as pd
"""
https://www.zhihu.com/column/c_1242092341365792768
"""

data_final = pd.DataFrame()
for i in range(1, 6):
    with open(str(i) + ".txt", 'r', encoding="UTF-8") as file_open:
        data = json.load(file_open)
        df_data = pd.DataFrame(data['data']["list"])
        data_final = data_final.append(df_data)
        print(i)
data_final.to_csv("Java_10K以上岗位情况.csv")
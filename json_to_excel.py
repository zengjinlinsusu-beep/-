import json
import pandas as pd

# 读取JSON文件
with open("重返未来.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 找出最长的数组长度
max_length = max(len(values) for values in data.values())

# 将数据转换为DataFrame，填充空值
df_data = {}
for key, values in data.items():
    # 如果数组长度不够，用空字符串填充
    padded_values = values + [''] * (max_length - len(values))
    df_data[key] = padded_values

# 创建DataFrame
df = pd.DataFrame(df_data)

# 导出到Excel
output_file = "重返未来.xlsx"
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"已成功导出到 {output_file}")
print(f"共 {len(df)} 行数据，{len(df.columns)} 列字段")
print(f"字段列表: {', '.join(df.columns.tolist())}")

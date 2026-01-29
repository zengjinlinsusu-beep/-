import json
import pandas as pd

# 读取Excel文件中第五人格sheet的数据
df = pd.read_excel("字段属性使用.xlsx", sheet_name="第五人格", engine='openpyxl')

# 读取当前JSON文件
with open("第五人格.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 还原"时装稀世对应角色名"字段（过滤空值）
data["时装稀世对应角色名"] = df["时装稀世对应角色名"].fillna('').tolist()
data["时装稀世对应角色名"] = [x for x in data["时装稀世对应角色名"] if x != '']

# 还原"时装-稀世"字段（过滤空值）
data["时装-稀世"] = df["时装-稀世"].fillna('').tolist()
data["时装-稀世"] = [x for x in data["时装-稀世"] if x != '']

# 保存回文件
with open("第五人格.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"已还原 '时装稀世对应角色名' 和 '时装-稀世' 字段")
print(f"时装稀世对应角色名: {len(data['时装稀世对应角色名'])} 条记录")
print(f"时装-稀世: {len(data['时装-稀世'])} 条记录")

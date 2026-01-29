import json
from pathlib import Path

# 读取第五人格.json文件
with open("第五人格.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 获取两个需要合并的字段
role_names = data["时装奇珍对应的角色名"]
fashion_names = data["角色-时装奇珍"]

# 按行合并，用"-"连接
fashion_merged = [f"{role}-{fashion}" for role, fashion in zip(role_names, fashion_names)]

# 添加新的"时装"字段
data["时装"] = fashion_merged

# 保存回文件
with open("第五人格.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"已生成新的'时装'字段，共 {len(fashion_merged)} 条记录")
print(f"示例数据:")
for i in range(min(5, len(fashion_merged))):
    print(f"  {fashion_merged[i]}")

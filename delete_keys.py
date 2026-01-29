import json

# 读取第五人格.json文件
with open("第五人格.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 删除指定的key
del data["时装稀世对应角色名"]
del data["时装-稀世"]

# 保存回文件
with open("第五人格.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("已删除 '时装稀世对应角色名' 和 '时装-稀世' 字段")
print(f"当前文件中的字段: {', '.join(data.keys())}")

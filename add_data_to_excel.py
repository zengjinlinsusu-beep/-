import pandas as pd

# 读取Excel文件
df = pd.read_excel("重返未来.xlsx", engine='openpyxl')

# 在对应列的最后一行添加新数据
# 使用 len(df) 获取当前行数，作为新行的索引
df.loc[len(df), "6星角色"] = "我是谁"
df.loc[len(df)-1, "5星角色"] = "你是我"  # 因为上面添加了一行，所以用len(df)-1

# 保存回Excel文件
df.to_excel("重返未来.xlsx", index=False, engine='openpyxl')

print("已成功添加数据:")
print(f"- 6星角色: 我是谁 (第{len(df)}行)")
print(f"- 5星角色: 你是我 (第{len(df)}行)")
print(f"\n现在表格共有 {len(df)} 行数据")

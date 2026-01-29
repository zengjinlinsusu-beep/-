import json
import pandas as pd
from pathlib import Path

excel_file = Path("字段属性使用.xlsx")

# 读取Excel文件的所有sheet
excel_data = pd.read_excel(excel_file, sheet_name=None, engine='openpyxl')

# 为每个sheet创建对应的JSON文件
for sheet_name, df in excel_data.items():
    # 将DataFrame转换为字典，每列作为key，列数据作为value（数组）
    data = {}
    for column in df.columns:
        # 将列数据转换为列表，过滤掉空字符串，NaN值转换为空字符串
        column_data = df[column].fillna('').tolist()
        # 过滤掉空字符串
        data[column] = [x for x in column_data if x != '']

    # 创建JSON文件名
    json_filename = f"{sheet_name}.json"
    json_path = Path(json_filename)

    # 保存为JSON文件，确保中文正常显示
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"已生成: {json_filename} ({len(data)} 个字段)")

print(f"\n完成！共处理 {len(excel_data)} 个sheet")

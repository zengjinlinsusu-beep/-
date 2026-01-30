"""
快速更新脚本 - 简化版
使用方法见底部说明
"""

import json
from datetime import datetime

def quick_update(game_name, updates_dict):
    """
    快速更新游戏数据

    参数:
        game_name: 游戏名称，如 "火影忍者"
        updates_dict: 更新内容字典，如:
            {
                "S忍": "宇智波斑「神驹佑将」",
                "A忍": "旗木卡卡西「神威对决」"
            }
    """

    # 读取游戏数据
    json_file = f"{game_name}.json"
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            game_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found - {json_file}")
        return False

    # 添加新数据
    for key, value in updates_dict.items():
        if key not in game_data:
            game_data[key] = []
            print(f"[NEW] Created field: {key}")

        if isinstance(game_data[key], list):
            if value not in game_data[key]:
                game_data[key].append(value)
                print(f"[OK] Added: {key} = {value}")
            else:
                print(f"[SKIP] Already exists: {key} = {value}")
        else:
            print(f"[WARNING] {key} is not a list, skipped")

    # 保存游戏数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(game_data, f, ensure_ascii=False, indent=2)

    # 记录更新日志
    update_log = {
        "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "game": game_name,
        "updates": updates_dict
    }

    try:
        with open('updates.json', 'r', encoding='utf-8') as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    logs.insert(0, update_log)

    with open('updates.json', 'w', encoding='utf-8') as f:
        json.dump(logs[:100], f, ensure_ascii=False, indent=2)

    print(f"\n[SUCCESS] Updated: {game_name}")
    print(f"Time: {update_log['time']}")
    print(f"Fields: {len(updates_dict)}")

    return True


# ========== 在这里编辑你的更新内容 ==========

# 示例1: 火影忍者更新
quick_update("火影忍者", {
    "S忍": "宇智波斑「神驹佑将」",
    "A忍": "旗木卡卡西「神威对决」",
    "B忍": "雨乃"
})

# 示例2: 其他游戏更新
# quick_update("原神", {
#     "五星角色": "新角色名",
#     "四星角色": "另一个新角色"
# })

# ===========================================

print("\nDone! Don't forget to push to GitHub:")
print("  git add -A")
print('  git commit -m "Update game data"')
print("  git push")

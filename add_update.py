import json
import sys
from datetime import datetime

def add_update(game_name, updates):
    """
    添加游戏更新并记录到更新日志

    参数:
        game_name: 游戏名称
        updates: 字典格式的更新数据，例如：
            {
                "S忍": "宇智波斑「神驹佑将」",
                "A忍": "旗木卡卡西「神威对决」",
                "B忍": "雨乃"
            }
    """
    # 1. 读取并更新游戏数据文件
    json_file = f"{game_name}.json"

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            game_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found {json_file}")
        return False

    # 添加新数据到对应字段
    for key, value in updates.items():
        if key in game_data:
            if isinstance(game_data[key], list):
                # 如果是列表，追加新值
                game_data[key].append(value)
                print(f"[OK] Added to {key}: {value}")
            else:
                print(f"[WARNING] {key} is not a list, skipped")
        else:
            # 如果字段不存在，创建新字段
            game_data[key] = [value]
            print(f"[OK] Created new field {key} and added: {value}")

    # 保存更新后的游戏数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(game_data, f, ensure_ascii=False, indent=2)

    # 2. 记录到更新日志
    update_log = {
        "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "game": game_name,
        "updates": updates
    }

    # 读取现有日志
    try:
        with open('updates.json', 'r', encoding='utf-8') as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    # 添加新日志到开头
    logs.insert(0, update_log)

    # 保存日志（只保留最近100条）
    with open('updates.json', 'w', encoding='utf-8') as f:
        json.dump(logs[:100], f, ensure_ascii=False, indent=2)

    print(f"\n[SUCCESS] Update completed!")
    print(f"Time: {update_log['time']}")
    print(f"Game: {game_name}")
    print(f"Items updated: {len(updates)}")

    return True


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python add_update.py \"GameName\" \"Field1:Value1\" \"Field2:Value2\" ...")
        print("\nExample:")
        print('python add_update.py "火影忍者" "S忍:宇智波斑「神驹佑将」" "A忍:旗木卡卡西「神威对决」" "B忍:雨乃"')
        sys.exit(1)

    game_name = sys.argv[1]

    # 解析更新数据
    updates = {}
    for arg in sys.argv[2:]:
        if ':' in arg:
            key, value = arg.split(':', 1)
            updates[key.strip()] = value.strip()

    add_update(game_name, updates)

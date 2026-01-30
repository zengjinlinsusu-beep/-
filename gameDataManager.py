import json
import os
import sys
from pathlib import Path

class GameDataManager:
    """游戏数据管理工具"""

    def __init__(self):
        self.games = []
        self.load_games_list()

    def load_games_list(self):
        """加载所有游戏列表"""
        json_files = []
        for file in Path('.').glob('*.json'):
            if file.name not in ['games.json', 'updates.json']:
                json_files.append(file.stem)

        self.games = sorted(json_files)
        return self.games

    def display_games(self):
        """显示游戏列表"""
        print("\n" + "="*60)
        print("[GAME] 游戏列表")
        print("="*60)
        for i, game in enumerate(self.games, 1):
            print(f"{i:3d}. {game}")
        print("="*60)

    def get_game_data(self, game_name):
        """获取游戏数据"""
        json_file = f"{game_name}.json"
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"[ERROR] 错误: 找不到文件 {json_file}")
            return None

    def save_game_data(self, game_name, data):
        """保存游戏数据"""
        json_file = f"{game_name}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] 已保存到 {json_file}")

    def display_fields(self, game_name):
        """显示游戏的所有字段"""
        data = self.get_game_data(game_name)
        if not data:
            return

        print(f"\n[LIST] {game_name} 的字段列表:")
        print("-"*60)
        for i, (key, value) in enumerate(data.items(), 1):
            count = len(value) if isinstance(value, list) else 1
            print(f"{i:2d}. {key:30s} ({count} 项)")
        print("-"*60)

    def display_field_values(self, game_name, field_name):
        """显示某个字段的所有值"""
        data = self.get_game_data(game_name)
        if not data:
            return

        if field_name not in data:
            print(f"[ERROR] 字段 '{field_name}' 不存在")
            return

        values = data[field_name]
        if not isinstance(values, list):
            values = [values]

        print(f"\n[LIST] {game_name} - {field_name} 的值列表:")
        print("-"*60)
        for i, value in enumerate(values, 1):
            print(f"{i:3d}. {value}")
        print("-"*60)

    def add_value(self, game_name, field_name, value):
        """添加值到字段"""
        data = self.get_game_data(game_name)
        if not data:
            return False

        if field_name not in data:
            data[field_name] = []
            print(f"[OK] 创建新字段: {field_name}")
        elif not isinstance(data[field_name], list):
            print(f"[ERROR] 错误: {field_name} 不是列表类型")
            return False

        # 检查值是否已存在
        if value in data[field_name]:
            print(f"[WARNING]  警告: 值 '{value}' 已存在")
            return False

        data[field_name].append(value)
        self.save_game_data(game_name, data)
        self.log_update(game_name, {field_name: value})
        print(f"[OK] 已添加: {field_name} = {value}")
        return True

    def update_value(self, game_name, field_name, old_value, new_value):
        """修改字段中的某个值"""
        data = self.get_game_data(game_name)
        if not data:
            return False

        if field_name not in data:
            print(f"[ERROR] 字段 '{field_name}' 不存在")
            return False

        if not isinstance(data[field_name], list):
            print(f"[ERROR] 错误: {field_name} 不是列表类型")
            return False

        if old_value not in data[field_name]:
            print(f"[ERROR] 值 '{old_value}' 不存在于字段中")
            return False

        index = data[field_name].index(old_value)
        data[field_name][index] = new_value
        self.save_game_data(game_name, data)
        print(f"[OK] 已修改: {field_name}[{index}] {old_value} → {new_value}")
        return True

    def delete_value(self, game_name, field_name, value):
        """删除字段中的某个值"""
        data = self.get_game_data(game_name)
        if not data:
            return False

        if field_name not in data:
            print(f"[ERROR] 字段 '{field_name}' 不存在")
            return False

        if not isinstance(data[field_name], list):
            print(f"[ERROR] 错误: {field_name} 不是列表类型")
            return False

        if value not in data[field_name]:
            print(f"[ERROR] 值 '{value}' 不存在于字段中")
            return False

        data[field_name].remove(value)
        self.save_game_data(game_name, data)
        print(f"[OK] 已删除: {field_name} = {value}")
        return True

    def log_update(self, game_name, updates):
        """记录更新到日志"""
        from datetime import datetime

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

    def interactive_mode(self):
        """交互模式"""
        while True:
            print("\n" + "="*60)
            print("[GAME] 游戏数据管理工具")
            print("="*60)
            print("1. 查看所有游戏")
            print("2. 查看游戏字段")
            print("3. 查看字段值")
            print("4. 添加值")
            print("5. 修改值")
            print("6. 删除值")
            print("0. 退出")
            print("="*60)

            choice = input("\n请选择操作 (0-6): ").strip()

            if choice == '0':
                print(" 再见!")
                break
            elif choice == '1':
                self.display_games()
            elif choice == '2':
                self.display_games()
                game_idx = input("\n请输入游戏编号: ").strip()
                if game_idx.isdigit() and 1 <= int(game_idx) <= len(self.games):
                    game_name = self.games[int(game_idx) - 1]
                    self.display_fields(game_name)
                else:
                    print("[ERROR] 无效的编号")
            elif choice == '3':
                self.display_games()
                game_idx = input("\n请输入游戏编号: ").strip()
                if game_idx.isdigit() and 1 <= int(game_idx) <= len(self.games):
                    game_name = self.games[int(game_idx) - 1]
                    self.display_fields(game_name)
                    field_name = input("\n请输入字段名称: ").strip()
                    self.display_field_values(game_name, field_name)
                else:
                    print("[ERROR] 无效的编号")
            elif choice == '4':
                self.display_games()
                game_idx = input("\n请输入游戏编号: ").strip()
                if game_idx.isdigit() and 1 <= int(game_idx) <= len(self.games):
                    game_name = self.games[int(game_idx) - 1]
                    self.display_fields(game_name)
                    field_name = input("\n请输入字段名称: ").strip()
                    value = input("请输入要添加的值: ").strip()
                    self.add_value(game_name, field_name, value)
                else:
                    print("[ERROR] 无效的编号")
            elif choice == '5':
                self.display_games()
                game_idx = input("\n请输入游戏编号: ").strip()
                if game_idx.isdigit() and 1 <= int(game_idx) <= len(self.games):
                    game_name = self.games[int(game_idx) - 1]
                    self.display_fields(game_name)
                    field_name = input("\n请输入字段名称: ").strip()
                    self.display_field_values(game_name, field_name)
                    old_value = input("请输入要修改的值: ").strip()
                    new_value = input("请输入新值: ").strip()
                    self.update_value(game_name, field_name, old_value, new_value)
                else:
                    print("[ERROR] 无效的编号")
            elif choice == '6':
                self.display_games()
                game_idx = input("\n请输入游戏编号: ").strip()
                if game_idx.isdigit() and 1 <= int(game_idx) <= len(self.games):
                    game_name = self.games[int(game_idx) - 1]
                    self.display_fields(game_name)
                    field_name = input("\n请输入字段名称: ").strip()
                    self.display_field_values(game_name, field_name)
                    value = input("请输入要删除的值: ").strip()
                    confirm = input(f"确认删除 '{value}'? (y/n): ").strip().lower()
                    if confirm == 'y':
                        self.delete_value(game_name, field_name, value)
                    else:
                        print("[ERROR] 已取消")
                else:
                    print("[ERROR] 无效的编号")
            else:
                print("[ERROR] 无效的选择")


def main():
    """主函数"""
    if len(sys.argv) > 1:
        # 命令行模式
        manager = GameDataManager()

        if sys.argv[1] == 'add' and len(sys.argv) >= 5:
            # python gameDataManager.py add 游戏名 字段名 值
            game_name = sys.argv[2]
            field_name = sys.argv[3]
            value = ' '.join(sys.argv[4:])
            manager.add_value(game_name, field_name, value)

        elif sys.argv[1] == 'update' and len(sys.argv) >= 6:
            # python gameDataManager.py update 游戏名 字段名 旧值 新值
            game_name = sys.argv[2]
            field_name = sys.argv[3]
            old_value = sys.argv[4]
            new_value = ' '.join(sys.argv[5:])
            manager.update_value(game_name, field_name, old_value, new_value)

        elif sys.argv[1] == 'delete' and len(sys.argv) >= 5:
            # python gameDataManager.py delete 游戏名 字段名 值
            game_name = sys.argv[2]
            field_name = sys.argv[3]
            value = ' '.join(sys.argv[4:])
            manager.delete_value(game_name, field_name, value)

        elif sys.argv[1] == 'list' and len(sys.argv) >= 3:
            # python gameDataManager.py list 游戏名 [字段名]
            game_name = sys.argv[2]
            if len(sys.argv) >= 4:
                field_name = sys.argv[3]
                manager.display_field_values(game_name, field_name)
            else:
                manager.display_fields(game_name)

        else:
            print("用法:")
            print("  交互模式: python gameDataManager.py")
            print("  添加值:   python gameDataManager.py add 游戏名 字段名 值")
            print("  修改值:   python gameDataManager.py update 游戏名 字段名 旧值 新值")
            print("  删除值:   python gameDataManager.py delete 游戏名 字段名 值")
            print("  查看字段: python gameDataManager.py list 游戏名 [字段名]")
    else:
        # 交互模式
        manager = GameDataManager()
        manager.interactive_mode()


if __name__ == "__main__":
    main()

"""
更新日志管理工具
支持按日期、游戏名称查询更新记录
"""
import json
from datetime import datetime
from pathlib import Path

class UpdateLogManager:
    """更新日志管理器"""

    def __init__(self):
        self.log_file = 'updates.json'
        self.logs = []
        self.load_logs()

    def load_logs(self):
        """加载更新日志"""
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                self.logs = json.load(f)
        except FileNotFoundError:
            print(f"[ERROR] 日志文件不存在: {self.log_file}")
            self.logs = []

    def save_logs(self):
        """保存更新日志"""
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(self.logs, f, ensure_ascii=False, indent=2)

    def show_all_logs(self, limit=None):
        """显示所有更新日志"""
        if not self.logs:
            print("[INFO] 暂无更新记录")
            return

        logs_to_show = self.logs[:limit] if limit else self.logs

        print("\n" + "="*80)
        print(f"[UPDATE LOG] 所有更新记录 (共 {len(logs_to_show)} 条)")
        print("="*80)

        for i, log in enumerate(logs_to_show, 1):
            print(f"\n[{i}] {log['time']} - {log['game']}")
            print("-"*80)
            for key, value in log['updates'].items():
                # 如果是带编号的key（如"枪皮_1"），只显示值
                if '_' in key and key.split('_')[-1].isdigit():
                    print(f"  - {value}")
                else:
                    print(f"  - {key}: {value}")
        print("\n" + "="*80)

    def search_by_game(self, game_name):
        """按游戏名称查询"""
        results = [log for log in self.logs if log['game'] == game_name]

        if not results:
            print(f"[INFO] 未找到游戏 '{game_name}' 的更新记录")
            return

        print("\n" + "="*80)
        print(f"[SEARCH] 游戏 '{game_name}' 的更新记录 (共 {len(results)} 条)")
        print("="*80)

        for i, log in enumerate(results, 1):
            print(f"\n[{i}] {log['time']}")
            print("-"*80)
            for key, value in log['updates'].items():
                if '_' in key and key.split('_')[-1].isdigit():
                    print(f"  - {value}")
                else:
                    print(f"  - {key}: {value}")
        print("\n" + "="*80)

    def search_by_date(self, date_str):
        """按日期查询（格式：YYYY-MM-DD 或 YYYY-MM-DD HH:MM:SS）"""
        results = []

        for log in self.logs:
            # 支持部分匹配日期
            if date_str in log['time']:
                results.append(log)

        if not results:
            print(f"[INFO] 未找到日期 '{date_str}' 的更新记录")
            return

        print("\n" + "="*80)
        print(f"[SEARCH] 日期 '{date_str}' 的更新记录 (共 {len(results)} 条)")
        print("="*80)

        for i, log in enumerate(results, 1):
            print(f"\n[{i}] {log['time']} - {log['game']}")
            print("-"*80)
            for key, value in log['updates'].items():
                if '_' in key and key.split('_')[-1].isdigit():
                    print(f"  - {value}")
                else:
                    print(f"  - {key}: {value}")
        print("\n" + "="*80)

    def search_by_keyword(self, keyword):
        """按关键词搜索（在更新内容中搜索）"""
        results = []

        for log in self.logs:
            # 在游戏名或更新内容中搜索
            if keyword in log['game']:
                results.append(log)
                continue

            # 在更新内容中搜索
            for key, value in log['updates'].items():
                if keyword in str(value) or keyword in key:
                    results.append(log)
                    break

        if not results:
            print(f"[INFO] 未找到包含关键词 '{keyword}' 的更新记录")
            return

        print("\n" + "="*80)
        print(f"[SEARCH] 关键词 '{keyword}' 的更新记录 (共 {len(results)} 条)")
        print("="*80)

        for i, log in enumerate(results, 1):
            print(f"\n[{i}] {log['time']} - {log['game']}")
            print("-"*80)
            for key, value in log['updates'].items():
                if '_' in key and key.split('_')[-1].isdigit():
                    print(f"  - {value}")
                else:
                    print(f"  - {key}: {value}")
        print("\n" + "="*80)

    def get_statistics(self):
        """获取统计信息"""
        if not self.logs:
            print("[INFO] 暂无更新记录")
            return

        # 统计每个游戏的更新次数
        game_counts = {}
        for log in self.logs:
            game = log['game']
            game_counts[game] = game_counts.get(game, 0) + 1

        # 统计最近更新日期
        if self.logs:
            latest_update = self.logs[0]['time']
            print(f"\n[STATISTICS] 更新日志统计")
            print("="*80)
            print(f"总更新记录数: {len(self.logs)}")
            print(f"最近更新时间: {latest_update}")
            print(f"\n各游戏更新次数:")
            print("-"*80)

            # 按更新次数排序
            sorted_games = sorted(game_counts.items(), key=lambda x: x[1], reverse=True)
            for game, count in sorted_games:
                print(f"  {game:30s} : {count:3d} 次")
            print("="*80)

    def export_to_text(self, output_file='update_log.txt'):
        """导出更新日志到文本文件"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("游戏数据库更新日志\n")
            f.write("="*80 + "\n\n")

            for i, log in enumerate(self.logs, 1):
                f.write(f"[{i}] {log['time']} - {log['game']}\n")
                f.write("-"*80 + "\n")
                for key, value in log['updates'].items():
                    if '_' in key and key.split('_')[-1].isdigit():
                        f.write(f"  - {value}\n")
                    else:
                        f.write(f"  - {key}: {value}\n")
                f.write("\n")

        print(f"[OK] 更新日志已导出到: {output_file}")


def main():
    """主函数"""
    import sys

    if len(sys.argv) < 2:
        print("更新日志管理工具")
        print("\n用法:")
        print("  查看所有日志:       python updateLogManager.py all [数量]")
        print("  按游戏查询:         python updateLogManager.py game <游戏名>")
        print("  按日期查询:         python updateLogManager.py date <日期>")
        print("  按关键词搜索:       python updateLogManager.py search <关键词>")
        print("  查看统计信息:       python updateLogManager.py stats")
        print("  导出到文本文件:     python updateLogManager.py export [文件名]")
        print("\n示例:")
        print('  python updateLogManager.py all 20')
        print('  python updateLogManager.py game "火影忍者"')
        print('  python updateLogManager.py date "2026-02-04"')
        print('  python updateLogManager.py search "暗星"')
        print('  python updateLogManager.py stats')
        print('  python updateLogManager.py export')
        return

    manager = UpdateLogManager()
    command = sys.argv[1].lower()

    if command == 'all':
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
        manager.show_all_logs(limit)

    elif command == 'game':
        if len(sys.argv) < 3:
            print("[ERROR] 请指定游戏名称")
            return
        game_name = ' '.join(sys.argv[2:])
        manager.search_by_game(game_name)

    elif command == 'date':
        if len(sys.argv) < 3:
            print("[ERROR] 请指定日期")
            return
        date_str = sys.argv[2]
        manager.search_by_date(date_str)

    elif command == 'search':
        if len(sys.argv) < 3:
            print("[ERROR] 请指定搜索关键词")
            return
        keyword = ' '.join(sys.argv[2:])
        manager.search_by_keyword(keyword)

    elif command == 'stats':
        manager.get_statistics()

    elif command == 'export':
        output_file = sys.argv[2] if len(sys.argv) > 2 else 'update_log.txt'
        manager.export_to_text(output_file)

    else:
        print(f"[ERROR] 未知命令: {command}")


if __name__ == "__main__":
    main()

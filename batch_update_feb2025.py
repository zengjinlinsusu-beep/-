"""
批量游戏数据更新脚本 - 2025年2月更新
"""
import json
from datetime import datetime

def batch_update(game_name, field_name, items):
    """批量添加数据"""
    json_file = f"{game_name}.json"

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {json_file}")
        return 0

    if field_name not in data:
        data[field_name] = []

    added = 0
    for item in items:
        item = item.strip()
        if item and item not in data[field_name]:
            data[field_name].append(item)
            added += 1
            print(f"[OK] {game_name} - {field_name}: {item}")
        elif item in data[field_name]:
            pass  # 跳过已存在的项

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return added

def log_update(updates_dict):
    """记录所有更新到日志"""
    logs = []
    try:
        with open('updates.json', 'r', encoding='utf-8') as f:
            logs = json.load(f)
    except:
        logs = []

    # 为每个游戏创建一条更新记录
    for game, updates in updates_dict.items():
        update_log = {
            "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "game": game,
            "updates": updates
        }
        logs.insert(0, update_log)

    with open('updates.json', 'w', encoding='utf-8') as f:
        json.dump(logs[:100], f, ensure_ascii=False, indent=2)

print("=" * 60)
print("批量游戏数据更新 - 2025年2月")
print("=" * 60)

all_updates = {}

# 1. QQ飞车
print("\n[1/25] 更新QQ飞车...")
batch_update("QQ飞车", "座椅", ["软爪萌虎"])
all_updates["QQ飞车_1"] = {"座椅": "软爪萌虎"}

# 2. 超自然行动
print("\n[2/25] 更新超自然行动...")
batch_update("超自然行动", "皮肤", ["青岚"])
batch_update("超自然行动", "挂饰", ["不朽的今夜"])
items = ["腰包-红运福虎", "专业手电-花束般的告白", "喷气背包-星棱幻翼"]
batch_update("超自然行动", "道具", items)
items = ["企鹅舞", "豪华定制烟花", "好运烟花"]
batch_update("超自然行动", "动作", items)
all_updates["超自然行动"] = {"更新": "皮肤、挂饰、道具3个、动作3个"}

# 3. 火影忍者
print("\n[3/25] 更新火影忍者...")
items = ["小南「神驹佑将」", "猿飞阿斯玛「神驹佑将」"]
batch_update("火影忍者", "A忍", items)
items = ["团圆之杯", "妙木山木碗"]
batch_update("火影忍者", "替身", items)
batch_update("火影忍者", "奥义", ["破阵"])
all_updates["火影忍者"] = {"更新": "A忍2个、替身2个、奥义1个"}

# 4. 暗区突围
print("\n[4/25] 更新暗区突围...")
items = ["顶级外设·MK14", "顶级外设·MP5", "顶级外设·RPK16", "顶级外设·AUG", "顶级外设·MP133", "顶级外设·F2000", "顶级外设·AX50", "顶级外设·CPW"]
batch_update("暗区突围", "武器", items)
all_updates["暗区突围"] = {"武器_1": "顶级外设系列8个"}

# 5. 第五人格
print("\n[5/25] 更新第五人格...")
batch_update("第五人格", "随身奇珍", ["鲸落"])
all_updates["第五人格_1"] = {"随身奇珍": "鲸落"}

# 6. 部落冲突
print("\n[6/25] 更新部落冲突...")
batch_update("部落冲突", "皮肤", ["红孩儿战神"])
all_updates["部落冲突"] = {"皮肤": "红孩儿战神"}

# 7. QQ飞车（第二批）
print("\n[7/25] 更新QQ飞车（第二批）...")
batch_update("QQ飞车", "A车皮肤", ["弦音", "星璃"])
batch_update("QQ飞车", "宠物", ["小脑虎"])
all_updates["QQ飞车_2"] = {"更新": "A车皮肤2个、宠物1个"}

# 8. 金铲铲之战
print("\n[8/25] 更新金铲铲之战...")
batch_update("掌上金铲铲", "小小英雄", ["一马当先", "羽饰骑士"])
all_updates["金铲铲之战"] = {"小小英雄": "一马当先、羽饰骑士"}

# 9. 蛋仔派对
print("\n[9/25] 更新蛋仔派对...")
batch_update("蛋仔派对", "盲盒", ["糖炒栗子", "咸鱼蛋"])
all_updates["蛋仔派对"] = {"盲盒": "糖炒栗子、咸鱼蛋"}

# 10. 王牌竞速
print("\n[10/25] 更新王牌竞速...")
batch_update("王牌竞速", "轮毂", ["喵动光速"])
batch_update("王牌竞速", "赛车", ["兰博基尼-Revuelto"])
batch_update("王牌竞速", "涂装", ["雷霆主宰", "即刻出发 ZR1"])
batch_update("王牌竞速", "女套装", ["恩典甜心套装", "迷幻节拍套装"])
all_updates["王牌竞速_1"] = {"更新": "轮毂、赛车、涂装2个、女套装2个"}

# 王牌竞速（第二批）
batch_update("王牌竞速", "女套装", ["绛紫夜上海套装"])
all_updates["王牌竞速_2"] = {"女套装": "绛紫夜上海套装"}

# 11. 三角洲行动
print("\n[11/25] 更新三角洲行动...")
items = ["SMG-45冲锋枪-精英特工", "KC17突击步枪-精英特工"]
batch_update("三角洲行动", "枪皮", items)
all_updates["三角洲行动"] = {"枪皮": "SMG-45冲锋枪-精英特工、KC17突击步枪-精英特工"}

# 12. 斗罗大陆：猎魂世界
print("\n[12/25] 更新斗罗大陆：猎魂世界...")
batch_update("斗罗大陆猎魂世界", "SP+魂师", ["光黯·千仞雪"])
all_updates["斗罗大陆猎魂世界"] = {"SP+魂师": "光黯·千仞雪"}

# 13. 尘白禁区
print("\n[13/25] 更新尘白禁区...")
batch_update("尘白禁区", "橙色武器", ["星渊月刃"])
all_updates["尘白禁区"] = {"橙色武器": "星渊月刃"}

# 14. 美职篮全明星
print("\n[14/25] 更新美职篮全明星...")
items = [
    "凯德.坎宁安-星耀洛城", "杰伦.布伦森-星耀洛城", "杰伦.布朗-星耀洛城",
    "扬尼斯.安特托昆博-星耀洛城", "卢卡.东契奇-星耀洛城", "尼古拉.约基奇-星耀洛城",
    "S.G.亚历山大-星耀洛城", "斯蒂芬.库里-星耀洛城", "泰雷塞.马克西-星耀洛城",
    "维克托.文班亚马-星耀洛城"
]
batch_update("美职篮全明星", "球星时刻", items)
all_updates["美职篮全明星"] = {"球星时刻_1": f"{len(items)}位NBA球星"}

# 15. 燕云十六声
print("\n[15/25] 更新燕云十六声...")
items = ["青锋映雪", "丹渊寰宇", "龙腾岁宴", "鸣鹿寻春"]
batch_update("燕云十六声", "套装", items)
batch_update("燕云十六声", "奇术特效", ["燃花庆夜"])
items = ["青锋映雪", "鸣鹿寻春", "龙腾岁宴", "轻霞"]
batch_update("燕云十六声", "发型", items)
items = ["鸣鹿寻春", "隐面", "小莓好", "青锋映雪", "傩面", "龙腾岁宴", "流光簌簌", "丹瑛坠", "玉砌寒枝", "剪雪裁冰"]
batch_update("燕云十六声", "首饰", items)
items = ["拂光烁金", "龙腾岁宴"]
batch_update("燕云十六声", "披挂", items)
items = ["墨韵青荷", "武德司令", "鸣鹿寻春", "墨者问天", "朱明承夜", "宋行桶", "富贵有鱼", "好杯杯", "赤霞佑", "木莲台", "簪花喵乌纱", "离思萦", "青锋映雪", "金络脑", "龙腾岁宴", "金枝玉叶", "冰魄凝", "岁华灼", "御池红", "一鹿生花", "齐天乐", "流华结叶", "鎏金荷", "撷芳意"]
batch_update("燕云十六声", "配饰", items)
batch_update("燕云十六声", "帽子", ["鸣鹿寻春"])
batch_update("燕云十六声", "武器皮肤", ["大道通明"])
all_updates["燕云十六声"] = {"更新": "套装4个、奇术特效、发型4个、首饰10个、披挂2个、配饰23个、帽子、武器皮肤"}

print("\n" + "=" * 60)
print("更新完成！正在保存更新日志...")
print("=" * 60)

log_update(all_updates)

print("\n[SUCCESS] 所有更新已完成!")
print("请运行以下命令同步到GitHub:")
print("  git add -A")
print('  git commit -m "Batch update: Feb 2025 game data updates"')
print("  git push")

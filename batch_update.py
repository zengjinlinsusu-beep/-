"""
批量游戏数据更新脚本
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

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return added

def log_update(updates_list):
    """记录所有更新到日志"""
    logs = []
    try:
        with open('updates.json', 'r', encoding='utf-8') as f:
            logs = json.load(f)
    except:
        pass

    # 为每个游戏创建一条更新记录
    for game, updates in updates_list.items():
        update_log = {
            "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "game": game,
            "updates": updates
        }
        logs.insert(0, update_log)

    with open('updates.json', 'w', encoding='utf-8') as f:
        json.dump(logs[:100], f, ensure_ascii=False, indent=2)

print("=" * 60)
print("批量游戏数据更新")
print("=" * 60)

all_updates = {}

# 1. 火影忍者
print("\n[1/20] 更新火影忍者...")
added = batch_update("火影忍者", "替身", ["神戟"])
if added > 0:
    all_updates["火影忍者"] = {"替身": "神戟"}

# 2. 超自然行动
print("\n[2/20] 更新超自然行动...")
items = ["拂云仙", "传送按钮-浮生一梦", "折扇-赴此良宵", "牛啤背包"]
added = batch_update("超自然行动", "挂饰", items)
if added > 0:
    all_updates["超自然行动"] = {f"挂饰_{i+1}": v for i, v in enumerate(items)}

added = batch_update("超自然行动", "工牌动作", ["轻躯鹤立"])
added = batch_update("超自然行动", "动作", ["金城舞"])
added = batch_update("超自然行动", "皮肤", ["瑶台梦"])

# 3. 三角洲行动
print("\n[3/20] 更新三角洲行动...")
items = ["暗星", "处刑者"]
added = batch_update("三角洲行动", "近战武器", items)
if added > 0:
    all_updates["三角洲行动_近战武器"] = {f"近战武器_{i+1}": v for i, v in enumerate(items)}

added = batch_update("三角洲行动", "干员皮肤", ["荒原猎手"])
if added > 0:
    all_updates["三角洲行动"] = {"干员皮肤": "荒原猎手"}

items = ["挂饰-非洲之心", "挂饰-暗星", "财神到", "摇钱树", "三足蟾", "狻猊", "祥龙", "福禄", "聚宝盆", "麻将", "挂饰-卡皮巴拉"]
added = batch_update("三角洲行动", "挂饰", items)

items = ["M1A4坦克-酒红", "M1A4坦克-巅峰竞赛", "M1A4坦克-流星", "步战车-建造", "步战车-巅峰竞赛", "突击车-酒红", "突击车-赤色军团", "突击车-变速", "突击车-巅峰竞赛", "突击车-流星", "突击车-赤骅", "防空车-建造", "轮式突击炮-青铁", "轮式突击炮-建造", "轮式突击炮-流星", "突击直升机-青铁", "突击直升机-流星", "突击直升机-火焰", "侦察直升机-青铁", "侦察直升机-酒红", "侦察直升机-黄蜂", "侦察直升机-流星", "全地形车-青铁", "全地形车-赤色军团", "全地形车-酒红", "全地形车-变速", "全地形车-巅峰竞赛", "GTQ35坦克-流星", "GTQ35坦克-凌云骏影", "F45A战斗机-航天飞机", "F45A战斗机-流星", "F45A战斗机-建造", "AAV两栖装甲运输车"]
added = batch_update("三角洲行动", "载具皮肤", items)

# 4. 燕云十六声
print("\n[4/20] 更新燕云十六声...")
batch_update("燕云十六声", "发型", ["赤心一寸"])
batch_update("燕云十六声", "套装", ["赤心一寸"])
all_updates["燕云十六声"] = {"发型": "赤心一寸", "套装": "赤心一寸"}

# 5. 无限暖暖
print("\n[5/20] 更新无限暖暖...")
items = ["妖夜鉴影", "尘外羽歌", "叙火长诗", "九色亦尘心", "翩月飞仙", "裁佳期", "帷幕与星色", "晴夏行"]
added = batch_update("无限暖暖", "套装", items)
if added > 0:
    all_updates["无限暖暖"] = {f"套装_{i+1}": v for i, v in enumerate(items)}

# 6. 第五人格
print("\n[6/20] 更新第五人格...")
batch_update("第五人格", "时装-稀世", ["前锋-群首"])
all_updates["第五人格_1"] = {"时装-稀世": "前锋-群首"}

# 7. 永劫无间手游
print("\n[7/20] 更新永劫无间手游...")
items = ["时装塔罗序·恶魔", "时装狩梦净魇", "时装天祀傩祝", "时装蝶恋衣", "时装寒绛点梅", "时装探海裙"]
batch_update("永劫无间手游", "时装", items)

items = ["发型塔罗序·烬星", "发型【挑染】安梦使", "发型方相氏", "发型幽梦", "发型落梅", "发型【挑染】清威"]
batch_update("永劫无间手游", "发型", items)

items = ["头部塔罗序·圣堕欲棱", "头部挨揍水饺", "头部软萌元宵", "头部夜巡灵羽", "头部夜巡灵羽·盛翼", "头部封厄傩面"]
batch_update("永劫无间手游", "头部", items)

items = ["腰部塔罗序·狱罂尾", "腰部唤神铃", "腰部碎傩面"]
batch_update("永劫无间手游", "腰部", items)

items = ["背部塔罗序·狱焰翼", "背部天祀滩祝", "背部梦蝶羽", "背部栖寒华"]
batch_update("永劫无间手游", "背部", items)

items = ["溯光寒", "劫烬·炼"]
batch_update("永劫无间手游", "长剑", items)

items = ["镇殃", "断昼吟"]
batch_update("永劫无间手游", "链剑", items)

items = ["战旗·宝莲", "跃鲤"]
batch_update("永劫无间手游", "枪", items)

items = ["月尺刀"]
batch_update("永劫无间手游", "棍", items)

items = ["饸锋藏"]
batch_update("永劫无间手游", "匕首", items)

items = ["炸裂"]
batch_update("永劫无间手游", "双截棍", items)

all_updates["永劫无间手游"] = {"更新": "时装、发型、头部、腰部、背部、武器等"}

# 8. 无畏契约：源能行动
print("\n[8/20] 更新无畏契约：源能行动...")
items = ["魄月玄兔", "狂徒", "全息波普//2.0", "幻影"]
batch_update("无畏契约源能行动", "武器", items)
all_updates["无畏契约源能行动"] = {f"武器_{i+1}": v for i, v in enumerate(items)}

# 9. QQ飞车
print("\n[9/20] 更新QQ飞车...")
items = ["幻星", "金龙沐泉"]
batch_update("QQ飞车", "A车皮", items)
all_updates["QQ飞车"] = {f"A车皮_{i+1}": v for i, v in enumerate(items)}

# 10. 使命召唤
print("\n[10/20] 更新使命召唤...")
batch_update("使命召唤", "传说角色", ["重德-豪鬼"])
all_updates["使命召唤"] = {"传说角色": "重德-豪鬼"}

# 11. 王牌竞速
print("\n[11/20] 更新王牌竞速...")
items = ["蝠翼破月·初", "蝠翼破月·进"]
batch_update("王牌竞速", "轮毂", items)
batch_update("王牌竞速", "男套装", ["悟空套装"])
all_updates["王牌竞速_1"] = {"轮毂": "蝠翼破月系列", "男套装": "悟空套装"}

# 12. 斗罗大陆：猎魂世界
print("\n[12/20] 更新斗罗大陆：猎魂世界...")
batch_update("斗罗大陆猎魂世界", "武魂", ["六翼天使"])
all_updates["斗罗大陆猎魂世界"] = {"武魂": "六翼天使"}

# 13. 原神
print("\n[13/20] 更新原神...")
batch_update("原神", "新五星角色", ["兹白"])
batch_update("原神", "新四星角色", ["叶洛亚"])
batch_update("原神", "新五星武器", ["朏魄含光"])
all_updates["原神"] = {"新五星角色": "兹白", "新四星角色": "叶洛亚", "新五星武器": "朏魄含光"}

# 14. 壮志雄心
print("\n[14/20] 更新壮志雄心...")
batch_update("壮志雄心", "角色", ["日奈"])
all_updates["壮志雄心"] = {"角色": "日奈"}

# 15. 鸣潮
print("\n[15/20] 更新鸣潮...")
batch_update("鸣潮", "五星角色", ["爱弥斯"])
batch_update("鸣潮", "五星武器", ["永远的启明星"])
all_updates["鸣潮"] = {"五星角色": "爱弥斯", "五星武器": "永远的启明星"}

# 16. 龙族卡塞尔之门
print("\n[16/20] 更新龙族卡塞尔之门...")
batch_update("龙族卡塞尔之门", "伙伴", ["刘昴星"])
all_updates["龙族卡塞尔之门"] = {"伙伴": "刘昴星"}

# 17. 王牌竞速 (第二批)
print("\n[17/20] 更新王牌竞速 (第二批)...")
items = ["机巧甜心套装"]
batch_update("王牌竞速", "女套装", items)
items = ["幼稚园套装", "风纪委员套装"]
batch_update("王牌竞速", "男套装", items)

# 18. 第五人格 (第二批)
print("\n[18/20] 更新第五人格 (第二批)...")
items = ["咒术师-夜之商籁", "园丁-长夏永不凋落", "斗牛士-此在无栖", "佣兵-致万千无言者", "守夜人-此刻万籁俱寂"]
batch_update("第五人格", "时装-稀世", items)

items = ["台球手-幽夜终章", "祭司-白焰初照", "园丁-暖冬记忆"]
batch_update("第五人格", "时装-奇珍", items)

batch_update("第五人格", "求生者", ["斗牛士"])

# 19. 永劫无间PC
print("\n[19/20] 更新永劫无间PC...")
items = ["朱嵌", "羿之影", "福鱼刀", "渊见", "问仙", "糖衣甜心", "五行相", "谪星·澄明", "饸锋藏"]
batch_update("PC永劫无间", "武器", items)

items = ["墨染千秋·青玉案", "谪星·西溟重岳", "倒反阴阳·狐踪", "墨染千秋·剪春漪", "玉漱冰骢", "狂虎", "倒反阴阳·天道", "墨染千秋·钟鼎光", "镇渊", "灵弓镇厄"]
batch_update("PC永劫无间", "时装", items)

items = ["墨染千秋·采薇", "【挑染】鎏渊", "倒反阴阳·恣意", "墨染千秋·春霁", "桀骜", "倒反阴阳·绝尘", "墨染千秋·青痕", "【挑染】焚光", "灵翎"]
batch_update("PC永劫无间", "发型", items)

items = ["软萌元宵", "萌萌芋饺", "耍酷菜饺", "害羞虾饺", "聪明煎饺", "挨揍水饺", "隐星索", "云笈青简", "双极悟", "倒反阴阳·赤狐尾", "倒反阴阳·赤狐耳", "墨染千秋·远黛", "倒反阴阳·玄玉冠", "辰龙坠", "雷云敕雨令", "古龙江湖·断飞枪", "灵弓镇厄", "同归", "重明木雕", "冥昭光相", "灵猴坠", "明心束带"]
batch_update("PC永劫无间", "挂饰", items)

batch_update("PC永劫无间", "战旗", ["战旗·宝莲"])

all_updates["PC永劫无间"] = {"更新": "武器、时装、发型、挂饰等"}

# 20. 王牌竞速 (第三批)
print("\n[20/20] 更新王牌竞速 (第三批)...")
items = ["逐风青骥", "奥迪-RS-3"]
batch_update("王牌竞速", "赛车", items)
batch_update("王牌竞速", "轮毂", ["电竞小咪"])

# 21. 第五人格 (第三批)
print("\n[21/21] 更新第五人格 (第三批)...")
batch_update("第五人格", "随身物品-稀世", ["龙之歌"])

print("\n" + "=" * 60)
print("更新完成！正在保存更新日志...")
print("=" * 60)

# 保存更新日志
log_update(all_updates)

print("\n[SUCCESS] 所有更新已完成！")
print("请运行以下命令同步到GitHub:")
print("  git add -A")
print('  git commit -m "Batch update game data"')
print("  git push")

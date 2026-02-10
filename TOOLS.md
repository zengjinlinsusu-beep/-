# 游戏数据管理工具使用说明

本目录提供多种游戏数据管理方式：**网页管理界面**（推荐）和Python脚本工具。

---

## 🌐 网页管理界面（推荐）⭐

### admin.html - 数据管理后台

打开 [admin.html](admin.html) 即可使用网页界面进行数据管理，无需运行Python脚本。

#### 功能特点
- 📝 **添加数据**：通过表单添加游戏数据，支持批量添加
- 👁️ **实时预览**：查看更新前后的数据变化
- 📥 **一键下载**：下载更新后的JSON文件或Python脚本
- 💻 **自动生成命令**：生成Git提交命令
- 🎮 **游戏选择**：下拉菜单选择游戏，显示现有字段

#### 使用流程
1. 打开 `admin.html`
2. 选择要更新的游戏
3. 输入字段名称（如：S忍、武器、皮肤等）
4. 输入要添加的值（每行一个，支持多个）
5. 点击"添加数据"预览
6. 下载更新后的JSON文件或Python脚本
7. 运行提供的Git命令提交到GitHub

#### 优势
- ✅ 无需安装Python环境
- ✅ 无需记住命令行参数
- ✅ 可视化操作更直观
- ✅ 支持预览和撤销
- ✅ 自动生成提交命令

---

## 🐍 Python脚本工具

---

## 1. `updateLogManager.py` - 更新日志管理工具 ⭐ 新增

### 查看所有更新记录
```bash
# 查看最近10条更新
python updateLogManager.py all

# 查看最近50条更新
python updateLogManager.py all 50
```

### 按游戏查询
```bash
# 查看某个游戏的所有更新记录
python updateLogManager.py game "火影忍者"
python updateLogManager.py game "三角洲行动"
```

### 按日期查询
```bash
# 查看特定日期的更新
python updateLogManager.py date "2026-02-06"

# 查看特定时间的更新
python updateLogManager.py date "2026-02-06 16:21"
```

### 按关键词搜索
```bash
# 在所有更新内容中搜索关键词
python updateLogManager.py search "暗星"
python updateLogManager.py search "宇智波斑"
```

### 查看统计信息
```bash
# 查看更新日志统计（各游戏更新次数等）
python updateLogManager.py stats
```

### 导出更新日志
```bash
# 导出到文本文件
python updateLogManager.py export

# 导出到指定文件
python updateLogManager.py export my_updates.txt
```

---

## 2. `add_update.py` - 批量添加更新

### 使用方法
```bash
python add_update.py "游戏名称" "字段1:值1" "字段2:值2" "字段3:值3"
```

### 示例
```bash
python add_update.py "火影忍者" "S忍:宇智波斑「神驹佑将」" "A忍:旗木卡卡西「神威对决」" "B忍:雨乃"
```

### 功能
- 批量添加多个字段值
- 自动创建不存在的字段
- 自动记录更新日志到 `updates.json`

---

## 3. `gameDataManager.py` - 完整数据管理工具

### 交互模式（推荐新手使用）
```bash
python gameDataManager.py
```

进入交互式菜单后，按提示选择操作：
1. 查看所有游戏
2. 查看游戏字段
3. 查看字段值
4. 添加值
5. 修改值
6. 删除值
0. 退出

### 命令行模式（快速操作）

#### 查看游戏的所有字段
```bash
python gameDataManager.py list 游戏名称
```

#### 查看某个字段的所有值
```bash
python gameDataManager.py list 游戏名称 字段名
```

#### 添加值
```bash
python gameDataManager.py add 游戏名称 字段名 值
```

#### 修改值
```bash
python gameDataManager.py update 游戏名称 字段名 旧值 新值
```

#### 删除值
```bash
python gameDataManager.py delete 游戏名称 字段名 值
```

### 示例
```bash
# 查看火影忍者所有字段
python gameDataManager.py list 火影忍者

# 查看S忍字段的所有值
python gameDataManager.py list 火影忍者 S忍

# 添加新S忍
python gameDataManager.py add 火影忍者 S忍 "新角色名"

# 修改S忍的值
python gameDataManager.py update 火影忍者 S忍 "旧角色名" "新角色名"

# 删除某个S忍
python gameDataManager.py delete 火影忍者 S忍 "要删除的角色名"
```

---

## 4. `quick_update.py` - 快速更新脚本

### 使用方法
直接编辑 `quick_update.py` 文件底部的代码：

```python
# 在这里编辑你的更新内容
quick_update("火影忍者", {
    "S忍": "宇智波斑「神驹佑将」",
    "A忍": "旗木卡卡西「神威对决」"
})
```

然后运行：
```bash
python quick_update.py
```

### 适用场景
- 需要频繁添加相同格式的更新
- 想保存常用更新模板
- 不想每次输入命令行参数

---

## 5. 网站功能

### 主页 (index.html)
- 🎮 游戏列表展示
- 🔍 游戏名称搜索
- 📊 点击查看游戏详细数据
- 📄 导出Excel和JSON格式
- 🔗 导航链接到更新日志页面

### 更新日志页面 (updates.html)
独立的更新日志管理页面，提供：
- 📊 **统计信息**：总更新记录、更新游戏数、今日更新
- 🎮 **游戏筛选**：支持模糊搜索所有69个游戏
- 🔍 **关键词搜索**：在更新内容中搜索
- 📅 **日期范围筛选**：查看特定时间段的更新
- ⚡ **快速过滤**：全部、今天、最近7天
- 📄 **导出功能**：导出更新日志为Excel文件

### 游戏数据搜索
- 游戏列表支持实时搜索
- 查看游戏数据时可搜索具体属性值
- 支持导出Excel和JSON格式

---

## 6. 更新到GitHub

执行任何数据更新后，运行以下命令同步到GitHub：

```bash
git add -A
git commit -m "Update game data"
git push
```

或使用部署脚本：
```bash
# Windows
deploy.bat

# Linux/Mac
./deploy.sh
```

---

## 注意事项

1. 所有脚本会自动记录更新到 `updates.json`
2. 网站会自动显示最近10条更新记录（可通过"全部"按钮查看所有记录）
3. 修改和删除操作不会记录到更新日志（只有添加操作会记录）
4. 建议先使用 `list` 命令查看现有数据再进行操作
5. 所有值会自动去重，重复添加相同值会被跳过
6. 更新日志保留最近100条记录，超出会自动删除最早的记录

---

## 更新日志管理

### 查询更新历史
```bash
# 查看某个游戏的所有更新
python updateLogManager.py game "三角洲行动"

# 查看今天的所有更新
python updateLogManager.py date "2026-02-06"

# 搜索包含特定内容的更新
python updateLogManager.py search "暗星"

# 查看统计信息
python updateLogManager.py stats
```

---

## 常见问题

### Q: 如何查看某个游戏有哪些字段？
```bash
python gameDataManager.py list 游戏名称
```

### Q: 如何批量添加多个值？
使用 `add_update.py` 或编辑 `quick_update.py`

### Q: 修改错了怎么办？
可以再次使用 `update` 命令改回来，或者手动编辑JSON文件

### Q: Windows控制台显示乱码？
这是Windows控制台编码问题，不影响实际数据。数据文件正常保存为UTF-8格式。

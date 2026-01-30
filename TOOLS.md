# 游戏数据管理工具使用说明

本目录包含三个用于管理游戏数据的Python脚本。

---

## 1. `add_update.py` - 批量添加更新

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

## 2. `gameDataManager.py` - 完整数据管理工具

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

## 3. `quick_update.py` - 快速更新脚本

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

## 4. 更新到GitHub

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
2. 网站会自动显示最近10条更新记录
3. 修改和删除操作不会记录到更新日志（只有添加操作会记录）
4. 建议先使用 `list` 命令查看现有数据再进行操作
5. 所有值会自动去重，重复添加相同值会被跳过

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

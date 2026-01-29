# 游戏数据库

这是一个展示游戏数据的在线网站，使用 GitHub Pages 托管。

## 📁 文件说明

- `index.html` - 主页面，展示所有游戏数据
- `*.json` - 各个游戏的JSON数据文件

## 🚀 如何部署到 GitHub Pages

### 方法一：通过 GitHub 网页界面（最简单）

1. **创建 GitHub 仓库**
   - 访问 [GitHub](https://github.com)
   - 点击右上角 "+" → "New repository"
   - 仓库名称：例如 `game-database`（或任意名称）
   - 设置为 **Public**（公开仓库才能使用免费的 GitHub Pages）
   - 点击 "Create repository"

2. **上传文件**
   - 在新创建的仓库页面，点击 "uploading an existing file"
   - 将 `index.html` 和所有 `*.json` 文件拖拽上传
   - 在页面底部的 "Commit changes" 输入提交信息（如 "Initial commit"）
   - 点击 "Commit changes"

3. **启用 GitHub Pages**
   - 进入仓库的 "Settings"（设置）页面
   - 在左侧菜单找到 "Pages"
   - 在 "Source" 下拉菜单中选择：
     - Branch: `main` 或 `master`
     - Folder: `/ (root)`
   - 点击 "Save"

4. **访问网站**
   - 等待约 1-2 分钟
   - 刷新 Pages 页面，会显示您的网站地址
   - 格式通常是：`https://您的用户名.github.io/仓库名/`

### 方法二：使用 Git 命令行（推荐）

```bash
# 1. 初始化 Git 仓库
git init

# 2. 添加所有文件
git add .

# 3. 提交更改
git commit -m "Initial commit"

# 4. 创建 GitHub 仓库后，添加远程仓库
git remote add origin https://github.com/您的用户名/仓库名.git

# 5. 推送到 GitHub
git branch -M main
git push -u origin main
```

## 🔄 如何更新数据

### 更新现有数据

1. 修改对应的 JSON 文件
2. 如果只修改了 `index.html`，只需重新提交该文件
3. Git 提交并推送：
```bash
git add .
git commit -m "更新数据"
git push
```

GitHub Pages 会自动重新部署，通常 1-2 分钟后生效。

### 添加新游戏数据

1. 将新的 JSON 文件放入仓库
2. 在 `index.html` 的 `games` 数组中添加新游戏：
```javascript
const games = [
    // ... 现有游戏
    { name: '新游戏名称', file: '新游戏.json', icon: '🎮' }
];
```
3. 提交并推送更改

## 🛠️ 自定义设置

### 自定义域名

1. 在仓库根目录创建名为 `CNAME` 的文件（无扩展名）
2. 文件内容填入您的域名（如 `www.example.com`）
3. 在域名提供商处添加 DNS 记录：
   - 类型：CNAME
   - 名称：www（或 @）
   - 值：`您的用户名.github.io`

### 修改样式

直接编辑 `index.html` 中的 `<style>` 部分，修改颜色、布局等。

## 📊 数据格式说明

每个 JSON 文件应遵循以下格式：

```json
{
  "字段名1": ["数据1", "数据2", "数据3"],
  "字段名2": ["数据1", "数据2", "数据3"]
}
```

## 🌐 部署到其他平台

### Netlify
1. 访问 [Netlify Drop](https://app.netlify.com/drop)
2. 将整个文件夹拖拽到页面上
3. 几秒钟后即可获得网站链接

### Vercel
1. 访问 [Vercel](https://vercel.com)
2. 导入项目或使用 Vercel CLI
3. 自动部署完成

## ❓ 常见问题

**Q: 网站显示 404 错误？**
A: 检查 GitHub Pages 是否已启用，等待 1-2 分钟后刷新。

**Q: 数据更新后没有变化？**
A: 清除浏览器缓存（Ctrl+F5）或等待 GitHub Pages 重新部署。

**Q: 如何查看访问统计？**
A: 在仓库页面点击 "Insights" → "Traffic" 可查看访问数据。

## 📝 许可证

本项目内容仅供学习交流使用。

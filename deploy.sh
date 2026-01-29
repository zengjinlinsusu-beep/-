#!/bin/bash

# GitHub Pages 部署脚本
# 使用方法：./deploy.sh https://github.com/你的用户名/仓库名.git

REPO_URL=$1

if [ -z "$REPO_URL" ]; then
    echo "❌ 错误：请提供 GitHub 仓库地址"
    echo "使用方法: ./deploy.sh https://github.com/你的用户名/仓库名.git"
    exit 1
fi

echo "🚀 开始部署到 GitHub Pages..."

# 初始化 Git 仓库（如果还没有）
if [ ! -d ".git" ]; then
    git init
    echo "✅ Git 仓库初始化完成"
fi

# 添加所有文件
git add .

# 提交更改
echo "📝 提交更改..."
git commit -m "Update game data - $(date '+%Y-%m-%d %H:%M:%S')"

# 添加远程仓库（如果还没有）
if ! git remote get-url origin > /dev/null 2>&1; then
    git remote add origin $REPO_URL
    echo "✅ 远程仓库添加完成"
fi

# 推送到 GitHub
echo "📤 推送到 GitHub..."
git branch -M main
git push -u origin main --force

echo "✅ 部署完成！"
echo ""
echo "📌 后续步骤："
echo "1. 访问你的 GitHub 仓库"
echo "2. 进入 Settings → Pages"
echo "3. Source 选择: Branch: main, Folder: /(root)"
echo "4. 点击 Save"
echo "5. 等待 1-2 分钟，你的网站就可以访问了！"

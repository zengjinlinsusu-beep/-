@echo off
REM GitHub Pages 部署脚本 (Windows版本)
REM 使用方法：deploy.bat "https://github.com/你的用户名/仓库名.git"

set REPO_URL=%1

if "%REPO_URL%"=="" (
    echo ❌ 错误：请提供 GitHub 仓库地址
    echo 使用方法: deploy.bat "https://github.com/你的用户名/仓库名.git"
    pause
    exit /b 1
)

echo 🚀 开始部署到 GitHub Pages...

REM 检查是否已初始化 Git
if not exist ".git" (
    git init
    echo ✅ Git 仓库初始化完成
)

REM 添加所有文件
echo 📝 添加文件...
git add .

REM 提交更改
echo 📝 提交更改...
git commit -m "Update game data - %date% %time%"

REM 检查远程仓库是否存在
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    git remote add origin %REPO_URL%
    echo ✅ 远程仓库添加完成
)

REM 推送到 GitHub
echo 📤 推送到 GitHub...
git branch -M main
git push -u origin main --force

echo.
echo ✅ 部署完成！
echo.
echo 📌 后续步骤：
echo 1. 访问你的 GitHub 仓库
echo 2. 进入 Settings ^> Pages
echo 3. Source 选择: Branch: main, Folder: /(root)
echo 4. 点击 Save
echo 5. 等待 1-2 分钟，你的网站就可以访问了！
echo.
pause

@echo off
echo ========================================
echo UI自动化测试启动中...
echo ========================================

cd /d %~dp0

echo 安装依赖...
pip install -r requirements.txt

echo 运行测试...
python tests\test_baidu.py

pause
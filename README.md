# UI 自动化测试框架

## 项目简介

基于 Python + Selenium + Pytest 的 Web UI 自动化测试框架采用Page Object Model (POM)设计模式。
实现了百度搜索的自动化测试，并通过手机版 User-Agent 成功绕过反爬机制。


## 技术栈

- Python 3.8+
- Selenium 4.x
- Pytest 7.x
- Page Object Model

## 1. 安装依赖
```bash
pip install -r requirements.txt

## 2.测试运行
```bash
# 方式一：直接运行
python tests/test_baidu.py

# 方式二：使用 pytest
pytest tests/test_baidu.py -v -s

# 方式三：生成 HTML 报告
pytest tests/test_baidu.py --html=reports/report.html --self-contained-html

# 方式四：双击 run_test.bat (Windows)

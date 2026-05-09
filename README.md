# UI自动化测试项目

## 项目简介
基于 Python + Selenium + Pytest 的 Web UI 自动化测试框架,实现了百度搜索的自动化测试，并通过手机版 User-Agent 成功绕过反爬机制。

## 技术栈
- Python 3.8+
- Selenium 4.x
- Pytest 7.x
-  pytest-html 4.1.1

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```
---
### 2.运行测试

```bash
# 方式一：直接运行
python tests/test_baidu.py

# 方式二：使用 pytest
pytest tests/test_baidu.py -v -s

# 方式三：生成 HTML 报告
pytest tests/test_baidu.py --html=reports/report.html --self-contained-html

# 方式四：双击 run_test.bat (Windows)
```
---

测试用例说明

测试用例 描述
test_search_valid_keyword 测试有效关键词搜索（参数化）
test_search_long_keyword 测试超长关键词搜索
test_search_empty_keyword 测试空搜索/无效搜索
test_multiple_searches 测试连续搜索

---


1自动截图

测试执行后自动保存截图，方便问题定位

2.HTML 测试报告

自动生成美观的测试报告，包含执行结果和截图

3.完整日志

控制台实时输出 + 文件持久化存储

---

解决的问题

百度反爬验证 使用手机版 User-Agent (https://m.baidu.com)
元素不可交互 使用 WebDriverWait 显式等待
弹窗遮挡 添加弹窗关闭逻辑

---

后续扩展建议

· 集成 CI/CD (GitHub Actions)
· 添加 Allure 报告
· 支持多浏览器 (Firefox, Edge)
· 添加邮件通知功能
· 分布式并行执行

---

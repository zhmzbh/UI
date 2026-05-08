#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
运行所有测试并生成报告
"""

import subprocess
import sys
import os


def run_pytest_tests():
    """运行pytest测试"""
    print("=" * 60)
    print("运行 pytest 测试套件")
    print("=" * 60)

    # 运行测试并生成报告
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/test_baidu.py",
        "-v", "-s",
        "--html=reports/pytest_report.html",
        "--self-contained-html",
        "--reruns", "2",  # 失败重试2次
        "-n", "auto"  # 并行运行
    ]

    result = subprocess.run(cmd)
    return result.returncode


def run_main_test():
    """运行主测试"""
    print("=" * 60)
    print("运行主测试入口")
    print("=" * 60)

    # 导入并运行
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from tests.test_baidu import TestBaidu
    from utils.driver import DriverManager
    from config import Config
    import time

    driver = DriverManager.get_driver()

    try:
        test = TestBaidu()
        test.test_search_valid_keyword(driver, "Selenium自动化测试")
        test.test_multiple_searches(driver)
        print("\n✅ 所有测试通过！")
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
    finally:
        time.sleep(2)
        driver.quit()

    return 0


if __name__ == "__main__":
    print("\n🚀 UI自动化测试执行器")
    print("1 - 运行主测试")
    print("2 - 运行pytest测试（含报告）")

    choice = input("请选择 (1/2): ").strip()

    if choice == "2":
        exit_code = run_pytest_tests()
    else:
        exit_code = run_main_test()

    sys.exit(exit_code)

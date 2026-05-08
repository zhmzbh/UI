import pytest
from utils.driver import DriverManager


@pytest.fixture(scope="function")
def driver():
    """每个测试用例前创建driver，测试结束后关闭"""
    print("\n启动浏览器...")
    driver = DriverManager.get_driver()
    yield driver
    print("\n关闭浏览器...")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试失败时自动截图"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            import os
            screenshot_dir = "reports/screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            driver.save_screenshot(f"{screenshot_dir}/{item.name}.png")
            print(f"\n截图已保存: {screenshot_dir}/{item.name}.png")

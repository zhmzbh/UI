import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

print("=" * 50)
print("手机版百度搜索测试")
print("=" * 50)

service = Service('./chromedriver.exe')
options = webdriver.ChromeOptions()

# 模拟手机浏览器
options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1')

driver = webdriver.Chrome(service=service, options=options)

try:
    print("1. 访问手机版百度")
    driver.get("https://m.baidu.com")
    time.sleep(2)
    driver.save_screenshot("mobile_baidu.png")
    print(f"当前标题: {driver.title}")

    # 手机版百度的搜索框
    print("2. 输入搜索词...")
    search_input = driver.find_element(By.ID, "index-kw")
    search_input.send_keys("Selenium自动化测试")
    time.sleep(0.5)
    print("输入完成")

    print("3. 点击搜索")
    search_btn = driver.find_element(By.ID, "index-bn")
    search_btn.click()
    time.sleep(3)
    print("搜索完成")

    print(f"4. 结果标题: {driver.title}")

    if "Selenium" in driver.title or "百度" in driver.title:
        print("测试通过！")

    driver.save_screenshot("mobile_result.png")
    print("5. 截图已保存: mobile_result.png")

except Exception as e:
    print(f"错误: {e}")

finally:
    time.sleep(2)
    driver.quit()

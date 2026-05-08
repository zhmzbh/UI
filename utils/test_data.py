# 测试数据
class TestData:
    # 搜索关键词列表
    SEARCH_KEYWORDS = [
        "Selenium自动化测试",
        "Python教程",
        "Pytest框架",
        "Web自动化"
    ]

    # 预期结果关键词
    EXPECTED_WORDS = [
        "Selenium",
        "Python",
        "Pytest",
        "自动化"
    ]

    # 无效搜索测试数据
    INVALID_DATA = [
        "",
        "@#$%",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ]
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    
    browser.get('https://shimo.im/login')

    # 输入邮箱
    browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('test@gmail.com')
    
    # 输入密码
    browser.find_element_by_xpath('//*[@name="password"]').send_keys('test')

    # 点击登录按钮
    browser.find_element_by_xpath('//button[contains(@class,"submit")]').click()

    # 获取cookies
    cookies = browser.get_cookies()
    print(cookies)

except Exception as e:
    print(e)
finally:    
    browser.close()
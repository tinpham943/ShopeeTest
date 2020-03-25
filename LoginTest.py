from selenium import webdriver


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2  # 1:allow, 2:block
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)  # seconds

    # Go to facebook.com
    driver.get("http://newtours.demoaut.com/")
    userName = driver.find_element_by_name('userName')
    passWord = driver.find_element_by_name('password')
    signIn = driver.find_element_by_name('login')

    userName.send_keys('shopeetest')
    passWord.send_keys('Shopee@2020')
    signIn.click()
    assert (driver.find_element_by_xpath(
        '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/img').is_displayed() == True)
    print('Passed')


if __name__ == '__main__':
    main()

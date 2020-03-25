from selenium import webdriver


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)  # seconds

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
    driver.close()


if __name__ == '__main__':
    main()

# import pickle
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import undetected_chromedriver as chromedriver
#
# def cookie_file(url):
#     driver_path = '/Users/arpithirani/Documents/chromedriver'
#     chrome_options = Options()
#     chrome_options.add_experimental_option('debuggerAddress', '172.16.20.206:4059')
#     driver = webdriver.Chrome(options= chrome_options, executable_path= driver_path)
#     driver.get(url)
#     pickle.dump(driver.get_cookies(), open("cookies.pk1", "wb"))
#
# cookie_file("https://buffalo.navigate.eab.com/app/#/my/priority-feed/")
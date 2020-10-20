from selenium import webdriver

# set path to chrome webdriver in OS
PATH = "C:\Program Files (x86)\chrome driver\chromedriver.exe"

# call driver with path
driver: object = webdriver.Chrome(PATH)

# get website
driver.get("https://www.youtube.com")

# print title
print(driver.title)

# quit
driver.quit()

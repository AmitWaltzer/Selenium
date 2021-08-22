# Selenium short course code:
# link: https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&index=1

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# choosing Chrome for what we'll be working on and inserting the path to the chrome web drive


# search_by_name - searching for an element, pressing "test" + Enter
def search_by_name(name):
    search = driver.find_element_by_name(name) # find the search element in the tab
    search.clear()              # clear the text field
    search.send_keys("test")    # insert word "test" to search tab
    search.send_keys(Keys.RETURN)   # press ENTER (RETURN)


def method_1():

    driver.get("https://www.techwithtim.net/")  # opening a website
    # choosing Chrome for what we'll be working on and inserting the path to the chrome web drive
    # print(driver.page_source)   # print the entire page source code
    # time.sleep(5)
    # driver.close()      # close current tab
    # print(driver.title)        # get the title
    # driver.quit()       # close the browser

    # explicit wait: loads main
    # dont use this! - can cause error if main not loaded yet
    # main = driver.find_element_by_id("main")
    # waits for 'main' to load before continuing on
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
        # print(main.text)  # print all the text inside main
        articles = main.find_elements_by_tag_name("article")
        for article in articles:
            header = article.find_element_by_class_name("entry-summary")
            print(header.text)
    finally:
        driver.quit()


def method_2():

    driver.get("https://www.techwithtim.net/")  # opening a website
    # choosing Chrome for what we'll be working on and inserting the path to the chrome web drive
    # get the link which shows as "Python Programming"
    link = driver.find_element_by_link_text("Python Programming")
    link.click()    # click on the link

    # wait for link named "Begginer Python Tutorial" to load
    try:
        # element holds the "Begginer Python Tutorial" on success
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
        )
        time.sleep(1)
        element.click()  # click on the link

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sow-button-19310003"))
        )
        element.click()

        driver.back() # navigates to previous page
        driver.back()
        driver.back()
    except:     # quits if try fails
        driver.quit()

def method_3():
    # action chains: https://selenium-python.readthedocs.io/api.html
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    actions = ActionChains(driver) # create an action chains object instance


"C:\Program Files\Git\git-bash.exe" --cd-to-home



if __name__ == '__main__':

    # method_1()
    # method_2()
    # automating cookie clicker
    method_3()




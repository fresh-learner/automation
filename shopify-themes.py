# from os import wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

themes = pd.read_csv('theme_names.csv')
service_obj = Service("C:/Users/ashis/OneDrive/Desktop/Automation/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

def shopify_themes(theme_name):
    driver.get("https://themes.shopify.com/")
    driver.implicitly_wait(5)

    search_icon = driver.find_element(By.XPATH,"//button[@aria-label='Search the Theme Store']//*[name()='svg']")
    search_icon.click()
    search_box = driver.find_element(By.CSS_SELECTOR,'#q')
    search_box.clear()
    search_box.send_keys(theme_name)
    search_box.send_keys(Keys.ENTER)
    theme_page = driver.find_element(By.XPATH,"//div[@class = 'style-images  tw-relative tw-max-h-80 tw-overflow-hidden lg:tw-max-h-96']/child::img[2]")
    theme_page.click()
    # print('clicked')
    # Waitforelement = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.tw-w-full tw-h-auto')))
    # theme_page = driver.find_element(By.CSS_SELECTOR,'.tw-w-full tw-h-auto')
    # try:
    #     theme_page = driver.find_element(By.XPATH,"//div[@class = 'style-images  tw-relative tw-max-h-80 tw-overflow-hidden lg:tw-max-h-96']/child::img[1]")
    #     theme_page.click()



    viewDemoStore = driver.find_element(By.XPATH,"//a[@class='marketing-button marketing-button--secondary theme-preview-link tw-text-body-md tw-link-base tw-link-inverted tw-link-md tw-border-t-0 tw-border-r-0 tw-border-l-0 tw-rounded-none tw-p-0 !tw-ml-0 hover:tw-bg-transparent']//span[@class='theme-listing-cta-desktop-label'][normalize-space()='View demo store']")
    viewDemoStore.click()
    DemoStore = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body')))
    # main_element = driver.find_element(By.ID,'MainContent')
    # sections = main_element.find_elements(By.XPATH,'./*')
    # section_ids = [section.get_attribute('id') for section in sections if section.get_attribute('id')]
            
    # print(f"Theme Name: {'Baseline'}, Section IDs: {section_ids}")

    try:
        main_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'main'))
        )
        sections = main_element.find_elements(By.XPATH, './*')
        
        section_ids = [(section.get_attribute('id'), section.get_attribute('class')) 
                for section in sections 
                if section.get_attribute('id') or section.get_attribute('class')]

        print(f"Theme Name: {theme_name}, Section IDs and Classes: {section_ids}")


    except Exception as e:
        print(f"Error processing theme '{theme_name}': {str(e)}")


final_output = []
for theme_name in themes['Theme Name']:
    result = shopify_themes(theme_name)
    final_output.append({'Theme Name': theme_name,'Result':result})

df = pd.DataFrame(final_output)
df.to_csv('output.csv',index = False)

driver.quit()
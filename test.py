from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}



def get_source_html(sku):
    
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()

    driver.maximize_window()
    url =   f"https://www.wildberries.ru/catalog/{sku}/feedbacks"
    stars = ['star1','star2','star3','star4','star5']
    true_stars =['( * ) ','( ** )','( *** )','( **** )','( ***** )'] 
    driver.get(url)
    time.sleep(3)

    initial_html = driver.page_source
    initial_soup = BeautifulSoup(initial_html, 'html.parser')
    nameof = initial_soup.find('a',class_='product-line__name').text
    score = initial_soup.find('span', class_='address-rate-mini').text
    initial_quotes = initial_soup.find_all('li', class_='comments__item')
    counter = initial_soup.find('span', class_='product-feedbacks__count')
    driver.find_element(By.LINK_TEXT, "Оценке").click()
    driver.find_element(By.LINK_TEXT, "Оценке").click()
    prev_height = -1
    block_list = []
    toremuve="\xa0"
    for s in toremuve:
        text = counter.text.replace(s, "")
    scroll_count = 1
    max_scrolls= int(text) // 30
    summer = []
    
    
    
    while scroll_count < max_scrolls: 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


        WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'comments__item')))


        scroll_html = driver.page_source
        scroll_soup = BeautifulSoup(scroll_html, 'html.parser')
        scroll_quotes  = scroll_soup.find_all('li', class_='comments__item')
       
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height
        scroll_count += 1


    review_text = '' 
    obj_star = ''
    for quo in scroll_quotes:
        review_text = quo.find('p', class_='feedback__text')
        if review_text == None:
            review_text = "Комментария нет"
        else:
            review_text = review_text.text.replace('ещё', '')
        for star in range(len(stars)):
            if stars[star] in str(quo):
                obj_star = true_stars[star]
            else:
                pass

        block_list = [
            sku, nameof, score, obj_star, review_text
        ]
        summer.append(block_list)
           
    return summer


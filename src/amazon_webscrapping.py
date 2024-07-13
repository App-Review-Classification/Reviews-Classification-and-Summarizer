from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

class Amazon:

    def __init__(self, url):
        self.url = url
        self.driver = None
        self.review_page_url = None
    
    def open_link(self):
        options = Options()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.url)
    
    def get_reviewpage(self):
        try: 
            self.open_link()

            review_footer_xpath = "//*[@id='reviews-medley-footer']"
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, review_footer_xpath))
            )
            
            review_footer = self.driver.find_element(By.XPATH, review_footer_xpath)
            review_link = None
            if review_footer:
                review_url_xpath = "//*[@id='reviews-medley-footer']/div[2]/a"
                review_tag = review_footer.find_element(By.XPATH, review_url_xpath)
                review_link = review_tag.get_attribute("href")

                if review_link:
                    print(f"Review Link found : {review_link}")
                    self.review_page_url = review_link
                    print(f"Opening Review page.\n")
                    self.driver.get(self.review_page_url)
                else:
                    print("Review Link not found")
            else:
                print("Review footer not found")
        except Exception as e:
            print(f"Review footer not found \n Error : {e}")
    
    def close(self):
        if self.driver:
            self.driver.quit()

    def extract_reviews(self):
        try:
            self.open_link()
            # Wait until reviews are loaded
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.review'))
            )
            
            reviews = self.driver.find_elements(By.CSS_SELECTOR, '.review')
            review_texts = [review.text for review in reviews]
            return review_texts

        except TimeoutException:
            print("Timed out waiting for page to load")
            return []

        finally:
            self.close()


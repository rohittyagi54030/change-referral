import os

os.system("pip3 install -r requirements.txt")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
from urllib.parse import urlparse
from pyvirtualdisplay import Display
import time

options = webdriver.ChromeOptions()
options.add_argument("----start-maximized")
options.add_argument("--window-size=1440,789")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
autocontrol = 'no'
if autocontrol == 'yes':
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1420,1080")
    display = Display(visible=0, size=(1420, 1080))
    display.start()

count = 100
run = 0

page_view = 4
sleep_time = 50

referral_url = "https://www.google.com/"
final_url = "https://superadme.com/tracker/click.php?key=7n4fabc4m1tp97g6hr8e"

while True:
    if run >= count:
        break
    try:

        try:
            uas = []
            import csv

            with open("./DesktopUserAgent.csv", "r") as csvfile:
                reader_variable = csv.reader(csvfile, delimiter=",")
                for row in reader_variable:
                    uas.append(row)
            ua = random.choice(uas)
            print('ua', ua)
            options.add_argument(f"user-agent={ua[0]}")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            action = webdriver.ActionChains(driver)
            driver.implicitly_wait(30)

            driver.get(referral_url)
            time.sleep(10)
            driver.execute_script(
                f"var link = document.createElement('a');link.href = '{final_url}';link.id = 'tmp_link';document.body.appendChild(link);document.getElementById('tmp_link').click();")
            time.sleep(10)

            current_url = urlparse(driver.current_url)

            i = 0

            while i < page_view:
                try:
                    links = []
                    for link in driver.find_elements(By.TAG_NAME, "a"):
                        link_url = urlparse(link.get_attribute("href"))
                        if link_url.netloc == current_url.netloc and link_url.path != current_url.path:
                            links.append(link)
                    link = random.choice(links)
                    action.move_to_element(link)
                    action.perform()
                    link.click()
                    driver.execute_script(f"window.scrollTo(0, {random.randint(100, 1000)})")
                    time.sleep(2)
                    driver.execute_script(f"window.scrollTo({random.randint(100, 1000)}, 0)")
                    time.sleep(5)
                    driver.execute_script(f"window.scrollTo(0, {random.randint(100, 1000)})")
                    print(f"Sleeping for {sleep_time - 7} seconds")
                    time.sleep(sleep_time)
                    i += 1
                except:
                    pass

            # url = "https://click.trackaboutme.xyz/tracker/click.php?key=wf17p3ow55td98gkib1b"
            # time.sleep(1000)

            driver.quit()
            run += 1
        except Exception as e:
            print(e)
            try:
                driver.quit()
            except:
                pass
    except Exception as e:
        print(e)
        try:
            driver.quit()
        except:
            pass

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import overload
from secret import secret
from datetime import datetime
import_ = os.path.join(os.path.dirname(__file__), 'Selenium')
sys.path.append(import_)
from github_automation  import create_repository_on_github



def create_auto_comment(update=False):
    comment='Initial comment'
    if update:
        comment='Update {}'.format(datetime.today().strftime('%Y-%m-%d'),1)
    return str(comment)

def define_name(path):
    name = path.split("\\")[-1]
    return name

def create_repository_on_github(user='user',password='123',repo_name='test',public=True):
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://github.com/new')
    search_box = driver.find_element(By.ID, "login_field").send_keys(user)
    search_box = driver.find_element(By.ID, "password").send_keys(password)
    search_box = driver.find_element(By.CLASS_NAME, "btn")
    search_box.submit() 
    search_box = driver.find_element(By.ID, "react-aria-2").send_keys(repo_name)
    time.sleep(2)
    if not public:
        search_box = driver.find_element(By.ID, "react-aria-6").click()
    search_box = driver.find_element(By.ID, "react-aria-8").click()
    search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/react-app/div/form/div[3]/div[1]/div[1]/div[2]/button").submit()
    driver.quit()


def create_repository(path, update=False):
    name = define_name(path)
    comment=create_auto_comment(update=update)
    user='AleksanderDmowski'
    create_repository_on_github(user=user, password=secret(), repo_name=name)
    link = 'https://github.com/{}/{}.git'.format(user, name)
    repo = os.chdir(path)
    repo = os.system("git init {}".format(path))
    repo = os.system("git remote add origin {}".format(link))
    repo = os.system("git pull origin main")
    repo = os.system("git add {}".format(path))
    repo = os.system("git commit -m \"{}\" {}".format(comment, path))
    repo = os.system("git branch -m main")
    repo = os.system("git push --set-upstream origin main")
    return repo



repo = create_repository(r"C:\Users\Aleksander\Desktop\test_{}".format(21))

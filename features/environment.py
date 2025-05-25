import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import  Options as SafariOptions
import allure
from dotenv import load_dotenv
import os

load_dotenv()


def before_scenario(context,scenario):
    navegador=""
    print(scenario.tags)
    if "firefox" in scenario.tags:
        navegador=FirefoxOptions()
    elif "@edge" in scenario.tags:
        navegador=EdgeOptions()
    elif "@safari" in scenario.tags:
        navegador=SafariOptions()
    else:
        navegador=ChromeOptions()

    tipo_ejecucion=os.getenv("TIPO_EJECUCION")
    if tipo_ejecucion=="grid":
        grid_url=os.getenv("GRID_URL")
        context.browser= webdriver.Remote(command_executor=grid_url,options=navegador)
    elif tipo_ejecucion=="jenkins":
        navegador.add_argument('--headless')
        navegador.add_argument('--no-sandbox')
        navegador.add_argument('--disable-dev-shm-usage')
    else:
        if "firefox" in scenario.tags:
            context.browser = webdriver.Firefox(options=navegador)
        elif "edge" in scenario.tags:
            context.browser = webdriver.Edge(options=navegador)
        elif "safari" in scenario.tags:
            context.browser = webdriver.Safari(options=navegador)
        else:
            context.browser = webdriver.Chrome(options=navegador)
    context.browser.implicitly_wait(5)
    context.browser.maximize_window()


def after_scenario(context,scenario):
    print("escenario finalizado -----")
    context.browser.quit()

def after_step(context,step):
    if step.status == "failed" or step.status == "passed":
        screenshot = context.browser.get_screenshot_as_png()
        screenshotb64 = context.browser.get_screenshot_as_base64()
        setattr(step,"screenshot",screenshotb64)

        allure.attach(screenshot, name=step.name, attachment_type=allure.attachment_type.PNG)

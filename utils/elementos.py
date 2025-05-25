from selenium.webdriver.common.by import By


def buscar_por_xpath(context,xpath):
    return context.browser.find_element(by=By.XPATH,value=xpath)

def buscar_por_id(context,id):
    return context.browser.find_element(by=By.ID,value=id)
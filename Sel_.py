import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class FormSubmit :
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.mayoclinic.org/symptom-checker/abdominal-pain-in-adults-adult/related-factors/itt-20009075')

    def Checkbox_select(self, id, button):
        try:
            for x in id :
                checkboxes = self.driver.find_element(By.ID, x).click()
            submit = self.driver.find_element(By.ID, button).click()
            diseases = self.driver.find_element(By.CSS_SELECTOR, "div.check").get_attribute('innerHTML')
        except Exception as err:
            print(err)
        finally:
            self.driver.quit()
        return diseases
    


#p = FormSubmit()
#lst = ["main_0_maincontent_1_QualifierRepeater_FactorRepeater_0_CheckBoxQualifier_0", "main_0_maincontent_1_QualifierRepeater_FactorRepeater_4_CheckBoxQualifier_6"]
#p.Checkbox_select("main_0_maincontent_1_QualifierRepeater_FactorRepeater_0_CheckBoxQualifier_0","FindCause")
#k = p.Checkbox_select(lst,"FindCause")
#print(k)


#Locate the checkbox element




# Select the checkbox=
#checkbox.click()


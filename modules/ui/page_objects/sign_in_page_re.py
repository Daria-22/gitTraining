from modules.ui.page_objects.base_page_re import BasePageRE
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#SignInPage - inherited class of BasePageRE
class SignInPageRE(BasePageRE):
    #declare Class attribute URL
    URL = 'https://readingeggs.com.au/'
    
    #initialisation of inherited class with additional changes
    def __init__(self) -> None:
        super().__init__()
    
    # method to go to a necessary url    
    def go_to_link(self):
        self.driver.get(SignInPageRE.URL)
        
       
    #method for fiding the button "Log in"   and clicking it
    def find_and_click_login_button (self):
        login_button = self.driver.find_element(By.XPATH, "//a[@href='https://app.readingeggs.com/login']")
        login_button.click()
        
       
    #method for finding the login box
    def find_password_element(self):
        self.driver.get("https://app.readingeggs.com/login")
        
    #method to get elements from canvas
    def get_canvas_elements(self):
        self.login_field = self.driver.find_element(By.NAME, "username")
        self.pswd_field = self.driver.find_element(By.NAME, "password")
    
    #method for finding the password box
    
    #method for filling in the login box
    
    #method for filling in the password box
    
    #method for confirming the input of login and password
    
        
    
    #By.XPATH /html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/h1        
    
    #input wrong name or wrong email
    #    login_elem.send_keys(username)
        
        #find field to which the wrong password will be input
        #pass_elem = self.driver.find_element(By.role, "password")
        
        #input the wrong password
        #pass_elem.send_keys(password)
        
        #find button sign in
        #btn_elem = self.driver.find_element(By.XPATH, "commit")
        
        #emulation of left button click
        #btn_elem.click()
        
    #def check_title(self,expected_title):
    #    return self.driver.title == expected_title
        
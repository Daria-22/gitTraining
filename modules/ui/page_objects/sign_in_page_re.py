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
        
       
    #method for fiding the button "Log in"   and clicking it -works
    def find_and_click_login_button (self):
        login_button = self.driver.find_element(By.XPATH, "//a[@href='https://app.readingeggs.com/login']")
        login_button.click()
        
       
    #method for opening the login page 
    def open_login_page(self):
        self.driver.get("https://app.readingeggs.com/login")
        
    #method to get login element from the page 
    def get_login_element(self):
        login_field = self.driver.find_element(By.ID, "username") # works, my mistake - not makign the test complately independent
        return login_field
    
   #method to get password element from the page
    def get_password_element(self):
        password_field = self.driver.find_element(By.ID,"password") #worked
        return password_field
       
    
      
    
    #method for typing correct form of password student
    
    
    #method for typing orrect from of password teacher
    
       
       
       
       
       
       
       
       
       
        #self.pswd_field = self.driver.find_element(By.NAME, "password") #doesn't work
    
#name="username" id="username" 

    #method for finding the password box
    
    #method for filling in the login box
    
    #method for filling in the password box
    
    #method for confirming the input of login and password
    
        
   
    #return self.driver.title == expected_title
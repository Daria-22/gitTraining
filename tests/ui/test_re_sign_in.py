from modules.ui.page_objects.sign_in_page_re import SignInPageRE
import time
from selenium.webdriver.common.action_chains import ActionChains
import pytest

@pytest.mark.ui_mine
def test_the_button_for_login_is_found():
    #create an instance of page
    sign_in_pageRE = SignInPageRE()
    
    #opens the necessary page
    sign_in_pageRE.go_to_link()
    time.sleep(3)
    
    #find the button, click the login button:
    link= sign_in_pageRE.find_and_click_login_button() 
    time.sleep(10)
    
@pytest.mark.ui_mine
def test_correct_login_wrong_pswd():
    sign_in_pageRE = SignInPageRE()
    sign_in_pageRE.get_canvas_elements()
    print("The password and login boxes test is over")


#def test_correct_login():
#    SignInPageRE.find_password_element()
    
    #input wrong login and correct password
    
    #input correct login and wrong password
    
    #validate that empty input is not accepted
    
    
    #close the object
    sign_in_pageRE.close()
    
#I don't uderstand how to work with canvas, I need help
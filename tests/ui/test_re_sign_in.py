from modules.ui.page_objects.sign_in_page_re import SignInPageRE
import time
from selenium.webdriver.common.action_chains import ActionChains
import pytest

#test1 - finds Login button and clicks it
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
    print("Test 1 is completed")
 
#test 2 - try login with correct credentials   
@pytest.mark.ui_mine
def test_correct_login_correct_pswd():
    sign_in_pageRE = SignInPageRE()
    sign_in_pageRE.open_login_page()
    l = sign_in_pageRE.get_login_element()#trying to find box for login
    p = sign_in_pageRE.get_password_element() #trying to find box for password
    #How do I know that l and p went correctly and the command was successful? 
    l.send_keys('daria.kozak@mailinator.com') 
    p.send_keys('ClassesObjectsMay2023')
    
    print("Test 2 is completed")


#def test_correct_login():
    #SignInPageRE.get_login_elements()
    
    #input wrong login and correct password
    
    #input correct login and wrong password
    
    #validate that empty input is not accepted
    
    
    #close the object
    sign_in_pageRE.close()
    
#I don't uderstand how to work with canvas, I need help
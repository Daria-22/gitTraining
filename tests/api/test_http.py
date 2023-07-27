#test which will send HTTP request to git hub site

import pytest #pytest will do the job
import requests #request is the modile for sending requests 

@pytest.mark.http  #this mark should be added to pytest.ini
def test_first_request():
    r= requests.get('https://api.github.com/zen')
    print(r.text)
    
# the command to give ot pytest: pytest -m http -s (whatever it means)
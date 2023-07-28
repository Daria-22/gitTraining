from modules.api.clients.github import GitHub

import pytest

#point instead of a slash - a way to indicate path in Python 

@pytest.mark.api
def test_user_exists():
    api = GitHub() #instance of GitHub
    user = api.get_user_defunkt()  # pass the instance to function get_user_defunk() which will return th body of response
    assert user['login'] == 'defunk' #compare that login in body equals to 'defunk'
    
#this will be invoked by $pytest -m api
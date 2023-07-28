import pytest

from modules.api.clients.github import GitHub
#why not slash if it is address??
@pytest.mark.api
def test_user_exists():
    api = GitHub()
    user = api.get_user_defunkt() #for example here we use dot notation for passing instance
    #api to function(or method) get_user_defunkt, right???
    assert user['login'] == 'defunk'
    
#this will be invoked by $pytest -m api
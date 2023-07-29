import pytest

from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exists(github_api):
    #api = GitHib() #moved to fixture
    #user = api.get_user('defunkt')
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api): #from fixture, instance of user
    #api = GitHib() #moved to fixture
    #user = api.get_user('butenkosergii')
    r = github_api.get_user('butenkosergii') #gets from instance the body of response
    assert r['message'] == 'Not Found' #analyses the response message to see "Not found"
    
#pytest -s -m api 
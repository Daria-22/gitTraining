import pytest

from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exists(github_api):
    #api = GitHib() #moved to fixture
    #user = api.get_user('defunkt')
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api): #from fixture,  response for instance of a particular github user
    #api = GitHib() #moved to fixture
    #user = api.get_user('butenkosergii')
    r = github_api.get_user('butenkosergii') #gets from instance the body of response
    assert r['message'] == 'Not Found' #analyses the response message to see "Not found"

@pytest.mark.api
def test_repo_can_be_found(github_api): #use of fixture
    r = github_api.search_repo('become-qa-auto')
    #print(r)
    assert r['total_count'] == 42
    assert 'become-qa-auto' in r ['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    print(r)
    assert r['total_count'] == 0

@pytest.mark.api    
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('t')
    assert r['total_count'] != 0
           
#pytest -s -m api 
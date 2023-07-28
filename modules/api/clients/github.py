#all requests for GIT which we will use for testing
import requests

class GitHub:
     
     def get_user_defunkt(self):
         r = requests.get('https://api.github.com/users/defunkt')
         body = r.json()
         
         return body
     

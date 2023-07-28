import requests

class GitHub:
     
     def get_user_defunkt(self):
         r = requests.get('https://api.github.com/users/defunkt')
         body = r.json()
         
         return body
     
'''api = GitHub()
user = api.get_user_defunkt()
print(user)'''
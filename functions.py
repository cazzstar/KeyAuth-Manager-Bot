import requests


def app_info(sellerkey):
    
    url = f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=appdetails"
    resp = requests.get(url, headers = {'accept': 'application/json'})
    
    if resp.json()['success'] == True:
        
        appName = resp.json()['appdetails']['name']
        return appName
    
    else:
        
        return False
    
    


def reset_hwid(user, sellerkey):
        
    url = f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=resetuser&user={user}"
    resp = requests.post(url, headers = {'accept': 'application/'})
    
    return resp.json()['message']
    


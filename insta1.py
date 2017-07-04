import requests

BASE_URL = "https://api.instagram.com/v1/"
ACCESS_TOKEN = "1710907001.dfca125.4ebb054d26db41e380c1581ac7445cac"

def my_info():
    requested_url = (BASE_URL +"users/self/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url:%s" %(requested_url)
    access_my_info = requests.get(requested_url).json()
    print access_my_info


    if access_my_info['meta']['code'] == 200:
        if len(access_my_info['data']):
            print "Username of the user:%s" %(access_my_info['data']['username'])
            print "Full name of the user:%s" %(access_my_info['data']['full_name'])
            print "Followers:%d" %(access_my_info['data']['counts']['followed_by'])
            print "following:%d" %(access_my_info['data']['counts']['follows'])

        else:
            print "No user exists!!!"

    else:
        print "something is majorly wrong!!!"

my_info()

def get_user_id(insta_username):
    requested_url = (BASE_URL +"users/search?q=%s&access_token=%s") %(insta_username, ACCESS_TOKEN)
    print "Requested url is:%s" %(requested_url)
    user_info = requests.get(requested_url).json()
    print user_info


insta_username = raw_input("enter the username of the user")
get_user_id(insta_username)






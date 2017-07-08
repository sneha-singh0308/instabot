import requests
import urllib
import time


BASE_URL = "https://api.instagram.com/v1/"
ACCESS_TOKEN = "1710907001.dfca125.4ebb054d26db41e380c1581ac7445cac"

def my_info():
    requested_url = (BASE_URL +"users/self/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url:%s" %(requested_url)
    access_my_info = requests.get(requested_url).json()
    #print access_my_info


    if access_my_info['meta']['code'] == 200:
        if len(access_my_info['data']):
            print "Username:%s" %(access_my_info['data']['username'])
            print "Full name of the user:%s" %(access_my_info['data']['full_name'])
            print "Followers:%d" %(access_my_info['data']['counts']['followed_by'])
            print "following:%d" %(access_my_info['data']['counts']['follows'])

        else:
            print "No user exists!!!"

    else:
        print "Status code other than 200!!!"

    time.sleep(2)

#my_info()

def get_user_id(insta_username):
    requested_url = (BASE_URL +"users/search?q=%s&access_token=%s") %(insta_username, ACCESS_TOKEN)
    print "Requested url is:%s" %(requested_url)
    user_info = requests.get(requested_url).json()
    #print user_info

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']

        else:
            return None

    else:
        print "status code other than 200 received"
        exit()
    time.sleep(2)

#insta_username = raw_input("enter the username of the user")
#get_user_id(insta_username)


def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "No user exists"


    requested_url = (BASE_URL + "users/%s?access_token=%s") % (user_id, ACCESS_TOKEN)
    print "Requested url is:%s" % (requested_url)
    user_info = requests.get(requested_url).json()
    #print user_info

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print "Username:%s" %(user_info['data']['username'])
            print "Full name of the user:%s" %(user_info['data']['full_name'])
            print "Followers:%d" %(user_info['data']['counts']['followed_by'])
            print "following:%d" %(user_info['data']['counts']['follows'])

        else:
            print "No user exists!!!"

    else:
        print "Status code other than 200!!!"
    time.sleep(2)

#get_user_info(insta_username)

def get_own_media():
    requested_url = (BASE_URL +"users/self/media/recent/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url is:%s" %(requested_url)
    own_media = requests.get(requested_url).json()
    #print own_media

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            return own_media['data'][0]['id']

        else:
            print "No media exists"
    else:
        print "status code other than 200 returned."

    time.sleep(2)


#get_own_media()


def get_user_media(insta_username):

    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User does not exist"

    else:

        requested_url = (BASE_URL +"users/%s/media/recent/?access_token=%s") %(user_id, ACCESS_TOKEN)
        print "Requested url is:%s" %(requested_url)
        user_media = requests.get(requested_url).json()
        #print user_media

        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                return user_media['data'][0]['id']


            else:
                print "No media exists"
        else:
            print "status code other than 200 returned."

        time.sleep(2)

#get_user_media()

def download_own_media():
    requested_url = (BASE_URL +"users/self/media/recent/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url is:%s" %(requested_url)
    own_media = requests.get(requested_url).json()
    #print own_media

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name =  own_media['data'][0]['id'] +".jpeg"
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print "Your image has been downloaded"

        else:
            print "Post doesn't exist"
    else:
        print "status code other than 200 returned."

    time.sleep(2)

#download_own_media()

def download_user_media(insta_username):

    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User does not exist"

    else:
        requested_url = (BASE_URL +"users/%s/media/recent/?access_token=%s") %(user_id,ACCESS_TOKEN)
        print "Requested url is:%s" %(requested_url)
        user_media = requests.get(requested_url).json()
        #print user_media

        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                image_name =  user_media['data'][0]['id'] +".jpeg"
                image_url = user_media['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url,image_name)
                print "User's image has been downloaded"

            else:
                print "Post doesn't exist"
        else:
            print "status code other than 200 returned."
        time.sleep(2)

#download_user_media()

def get_media_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User does not exist"

    else:

        requested_url = (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, ACCESS_TOKEN)
        print "Requested url is:%s" % (requested_url)
        user_media = requests.get(requested_url).json()
        # print user_media

        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                return user_media['data'][0]['id']


            else:
                print "No media exists"
        else:
            print "status code other than 200 returned."

        time.sleep(2)

#get_media_id(insta_username)


def set_like(insta_username):
    post_id = get_media_id(insta_username)
    requested_url = (BASE_URL +"media/%s/likes") %(post_id)
    payload = {'access_token' : ACCESS_TOKEN}
    print "Post url is : %s" %(requested_url)
    post_like = requests.post(requested_url, payload).json()

    if post_like['meta']['code'] == 200:
        print "Photo has been liked by you!!!"

    else:
        print "Try Again"
    time.sleep(2)

#set_like(insta_username)


def post_comment(insta_username):
    media_id = get_media_id(insta_username)
    requested_url = (BASE_URL +"media/%s/comments") %(media_id)
    payload = { 'access_token' : ACCESS_TOKEN,
                'text' :"nice"}
    print "Post url is : %s" %(requested_url)
    set_comment = requests.post(requested_url, payload).json()

    if set_comment['meta']['code'] == 200:
        print "Your comment has been successfully posted!!"

    else:
        print "Try again!!"
    time.sleep(2)

#post_comment()























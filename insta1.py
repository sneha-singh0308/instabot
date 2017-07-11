import requests
import urllib
import time
from termcolor import colored

# declaring global variables i.e. BASE_URL and ACCESS_TOKEN(generated)
BASE_URL = "https://api.instagram.com/v1/"
ACCESS_TOKEN = "1710907001.dfca125.4ebb054d26db41e380c1581ac7445cac"

#declaring function to access own information.
def my_info():
    requested_url = (BASE_URL +"users/self/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url:%s" %(requested_url)
    access_my_info = requests.get(requested_url).json()

    #specifying that the function runs only when the status code is 200.
    if access_my_info['meta']['code'] == 200:
        if len(access_my_info['data']):
            print colored("Username:","blue") +" %s" %(access_my_info['data']['username'])
            print colored("Full name of the user:","blue") +" %s" %(access_my_info['data']['full_name'])
            print colored("Followers:","blue") +" %d" %(access_my_info['data']['counts']['followed_by'])
            print colored("following:","blue") +" %d" %(access_my_info['data']['counts']['follows'])

        else:
            print "No user exists!!!"

    else:
        print "Status code other than 200!!!"


#declaring function to get sandbox user's id.
def get_user_id(insta_username):
    requested_url = (BASE_URL +"users/search?q=%s&access_token=%s") %(insta_username, ACCESS_TOKEN)
    print "Requested url is:%s" %(requested_url)
    user_info = requests.get(requested_url).json()


    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']

        else:
            return None

    else:
        print "status code other than 200 received"
        exit()


#declaring function to display user's information on the screen.
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "No user exists"


    requested_url = (BASE_URL + "users/%s?access_token=%s") % (user_id, ACCESS_TOKEN)
    print "Requested url is:%s" % (requested_url)
    user_info = requests.get(requested_url).json()


    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print colored("Username:", "blue") + " %s" % (user_info['data']['username'])
            print colored("Full name of the user:", "blue") + " %s" % (user_info['data']['full_name'])
            print colored("Followers:", "blue") + " %d" % (user_info['data']['counts']['followed_by'])
            print colored("following:", "blue") + " %d" % (user_info['data']['counts']['follows'])


        else:
            print "No user exists!!!"

    else:
        print "Status code other than 200!!!"


#defining function to get access of own media
def get_own_media():
    requested_url = (BASE_URL +"users/self/media/recent/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url is:%s" %(requested_url)
    own_media = requests.get(requested_url).json()


    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            return own_media['data'][0]['id']

        else:
            print "No media exists"
    else:
        print "status code other than 200 returned."


#defining function to get user's media.
def get_user_media(insta_username):

    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User does not exist"

    else:

        requested_url = (BASE_URL +"users/%s/media/recent/?access_token=%s") %(user_id, ACCESS_TOKEN)
        print "Requested url is:%s" %(requested_url)
        user_media = requests.get(requested_url).json()


        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                return user_media['data'][0]['id']


            else:
                print "No media exists"
        else:
            print "status code other than 200 returned."


#declaring function for downloading own media
def download_own_media():
    requested_url = (BASE_URL +"users/self/media/recent/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url is:%s" %(requested_url)
    own_media = requests.get(requested_url).json()


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



#defining function to download user's media.
def download_user_media(insta_username):

    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User does not exist"

    else:
        requested_url = (BASE_URL +"users/%s/media/recent/?access_token=%s") %(user_id,ACCESS_TOKEN)
        print "Requested url is:%s" %(requested_url)
        user_media = requests.get(requested_url).json()


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


#defining function to get media ID(user's).
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



#declaring function to post like on user's media.
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


#declaring function to comment on user's post.
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


#defining function for fetching natural calamity images in a certain area by specifying latitude and longitude of the area.
def geo_fencing(latitude,longitude):

    if latitude == "" or longitude == "":
        print "Enter a valid latitude and longitude"

    else:

        requested_url = (BASE_URL +"media/search?lat=%s&lng=%s&access_token=%s") %(latitude,longitude,ACCESS_TOKEN)
        print "Requested url is:%s" %(requested_url)
        access_image = requests.get(requested_url).json()
        print access_image

        if access_image['meta']['code'] == 200:
            if len(access_image['data']):
                i=0
                k=0
                length = len(access_image['data'])
                while(length):
                    if access_image['data'][i]['type'] == "image" and (access_image['data'][i]['caption']
                                                                       ['text'] == "#flood" or access_image['data'][i]
                    ['caption']['text'] == "#earthquake"):
                        image_name = access_image['data'][i]['id'] +'.jpeg'
                        image_url = access_image['data'][i]['images']['standard_resolution']['url']
                        urllib.urlretrieve(image_url,image_name)
                        print "Your image has been downloaded!!! with ID : %s" %(access_image['data'][i]['id'])
                        k=k+1

                    else:
                        print "No image found of calamity"
                    length = length-1
                    i=i+1

            else:
                print "No media found in the mentioned location"

        else:
            print "Status code other than 200"




#CALLING OF THE FUNCTIONS IN OTHER FILE i.e. START.PY

























from termcolor import colored
from insta1 import*

print colored("Welcome to the instabot!!!","red")

def start_bot():
    while(True):

        print colored("Tell us what would you like to do here?","red")
        time.sleep(2)
        choice = raw_input("Enter your choice here \n1)Access your own information. \n2)Retrieve sanbox user's ID. \n3)Access"
                           " user's information. \n4)Getting own media. \n5)Getting user's media. \n6)Download own media. "
                           "\n7)Download user's media. \n8)Getting Media ID. \n9)Posting a like on user's media. \n10)Posting "
                           "comment on user's media. \n11)Finding disaster images in certain area. ")

        if choice == "1":
            my_info()
            time.sleep(2)

        elif choice == "2":
            insta_username = raw_input("enter the username of the user")
            get_user_id(insta_username)
            time.sleep(2)

        elif choice == "3":
            insta_username = raw_input("enter the username of the user")
            get_user_info(insta_username)
            time.sleep(2)

        elif choice == "4":
            get_own_media()
            time.sleep(2)

        elif choice == "5":
            insta_username = raw_input("enter the username of the user")
            get_user_media(insta_username)
            time.sleep(2)

        elif choice == "6":
            download_own_media()
            time.sleep(2)

        elif choice == "7":
            insta_username = raw_input("enter the username of the user")
            download_user_media(insta_username)
            time.sleep(2)

        elif choice == "8":
            insta_username = raw_input("enter the username of the user")
            get_media_id(insta_username)
            time.sleep(2)

        elif choice == "9":
            insta_username = raw_input("enter the username of the user")
            set_like(insta_username)
            time.sleep(2)

        elif choice == "10":
            insta_username = raw_input("enter the username of the user")
            post_comment(insta_username)
            time.sleep(2)

        elif choice == "11":
            latitude = raw_input("Enter the latitude")
            longitude = raw_input("Enter the longitude")
            geo_fencing(latitude, longitude)
            exit()

        else :
            print colored("INVALID CHOICE.Choose from the options only","red")

start_bot()








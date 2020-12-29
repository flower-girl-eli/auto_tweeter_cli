import tweepy
from twitter_codes import *
from os import uname

auth = tweepy.OAuthHandler(my_api_key, my_api_secret)
auth.set_access_token(my_access_token, my_access_token_sec)

api = tweepy.API(auth)
retry_counter = 0
while True: 
    if retry_counter < 4: #If it fails, just try it multiple times in order to be sure lol. 
        try: 
            api.verify_credentials()
            print("auth ok")
            allGood = True #this code is shit lol
        except:
            print("Auth error")
            allGood = False

        if allGood == True:
            sys_inf = uname() #Generates system information. You can then call and print them by using their specific codes - sysname(Linux, Win or other), nodename (name of your machine), release (of kernel), version (idk. Some dump of nums) and machine (processor architecture)
            while True:
                txt_input = input("Write down your tweet here: ")
                if len(txt_input) <= 200: #it needs some space for the sys info. Idk how much.
                    break
                else: 
                    print("Sorry, tweet too long. Please write it shorter.")
                    continue

            my_tweet = f"{txt_input}\n{sys_inf.machine} {sys_inf.nodename}"
            api.update_status(my_tweet)
            break
        elif allGood == False: 
            retry_counter = retry_counter + 1 
            continue
    else: 
        print("Yeah, the code is f-ed. Sorry, but you need to rewrite it.")
        break
        
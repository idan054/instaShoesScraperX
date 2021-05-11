## This func gives contact data of profiles based other profiles

from datetime import datetime
from itertools import dropwhile, takewhile
from datetime import date, timedelta
import instaloader
from color_printer import printGreen, printYellow


def insta_filter(users_min_followers, users_max_followers,
                 limit_per_session, selected_user):
    print("Start")
    L = instaloader.Instaloader()

    try:
        # Saved session to /Users/biton/.config/instaloader/session-sycho_shoes.il.
        L.load_session_from_file("sycho_shoes.il")
        print("Session Succeed")
    except:
        # L.login(user="3deal.com_", passwd="3deal3252")
        L.login(user="sycho_shoes.il", passwd="shoes325245")
        print("L.login() Done")


    user = instaloader.Profile.from_username(L.context, selected_user).get_similar_accounts()
    print(user)

    # matched_users = {
    #     "spider_modelsx"  : {
    #         "followers" : 90,
    #         "external_link" : "https://spider3d.co.il",
    #         "insta_link" : "https://instagram.com/spider_modelsx"
    #     }
    # }

    matched_users = {}
    print(len(matched_users))
    forIndex = 0
    # while len(matched_users) != 1:
    for current_user in user:
        # print(current_user.username)
        print(forIndex)
        if forIndex / 10 == forIndex // 10:  # Divide exactly
            printYellow("------------------------")
            printYellow(f"{len(matched_users)} found")
            print(matched_users)
            printYellow("------------------------")

        username = current_user.username
        # print(username)
        followers = current_user.followers
        # print(followers)
        external_url = current_user.external_url
        # print(external_url)

        if users_min_followers < followers < users_max_followers \
                and external_url is not None:
            matched_users.update({
                username: {
                    "followers": followers,
                    "external_link": external_url,
                    "insta_link": f"https://instagram.com/{username}"
                }
            })
            printGreen(username)
            printGreen(f"https://instagram.com/{username}")
            printGreen(str(f"{followers // 1000}K"))
            printGreen(external_url)
        else:
            print(username)
            print(f"https://instagram.com/{username}")
            print("------------------------")

        forIndex += 1

        ## Limits
        if len(matched_users) == limit_per_session:
            print(len(matched_users), "found")
            print(matched_users)
            return matched_users

        elif forIndex == 70: # Max limit before "Too many queries in the last time. Need to wait 427 seconds"
            print("forIndex is already", forIndex)
            print(matched_users)
            print(len(matched_users), "found")
            return matched_users


# print()
# print(matched_users)

# for u in user:
#     print(forIndex)
#     print(u.username)
#     print(u.external_url)
#     print(u.followers)
#     # forIndex += 1
#     break
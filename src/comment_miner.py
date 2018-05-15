#!/usr/bin/env python
# -*- coding: utf-8 -*-
#1350224639301548675
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
import pickle
username = str(input("username:"))
password = str(input("passwors:"))
api = InstagramAPI(username, password)
if (api.login()):
    #api.getSelfUserFeed()  # get self user feed
    #   print(api.LastJson)  # print last response JSON
    print("Login succes!")
else:
    print("Can't login!")


#friendly_comment_file = open("friendly_comments", "w")
#celebrity_comment_file = open("celebrity_comments", "w")
#my user id is : 474059646


FOLLOWING_COUNT_CELEBRITY_THRESHOLD = 2000
MAX_FOLLOWING_COUNT = 30
MAX_MEDIA_COUNT = 20
MAX_COMMENT_COUNT = 20
TOTAL_USER_COUNT = 1000
SAVE_BACKUP_PERIOD_USER_COUNT = 10

def readMediaComments(media_id, target_comments):
    has_more_comments = True
    max_id = ''
    comment_count = 0
    while has_more_comments and comment_count < MAX_COMMENT_COUNT:
        _ = api.getMediaComments(media_id, max_id=max_id)
        comments =api.LastJson['comments']
        for comment in comments:
            comment_count += 1
            target_comments.append(comment['text'])
        has_more_comments = api.LastJson.get('has_more_comments', False)
        if has_more_comments:
            max_id = api.LastJson.get('next_max_id', '')

def getFollowingsPk(user_id):
    next_max_id = True
    followings_pk = set()
    following_count = 0
    while next_max_id and following_count < MAX_FOLLOWING_COUNT:
        print("following found")
        print (next_max_id)
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''
        api.getUserFollowings(user_id, maxid=next_max_id)
        for user in api.LastJson['users']:
            if user['is_private'] == False :
                followings_pk.add(user['pk'])
                following_count += 1
                if following_count > MAX_FOLLOWING_COUNT:
                    break
        next_max_id = api.LastJson.get('next_max_id', '')
    return followings_pk

def getLimitedUserFeed(usernameId):
    user_feed = []
    next_max_id = ''
    feed_count = 0
    while feed_count < MAX_MEDIA_COUNT:
        api.getUserFeed(usernameId, next_max_id)
        temp = api.LastJson
        for item in temp["items"]:
            user_feed.append(item)
            feed_count += 1
        if temp["more_available"] is False:
            return user_feed
        next_max_id = temp["next_max_id"]
    return user_feed
all_users_pk = set()
all_users_pk.add("474059646")

all_friendly_comments = []

all_celebrity_comments = []

checked_user = [] #just for check that already checked pr not
total_user_count = 0
celebrity_user_count = 0
normal_user_count = 0

while total_user_count < TOTAL_USER_COUNT:
    media_count = 0
    user_id = all_users_pk.pop()
    if user_id in checked_user:
        print("user already checked")
        continue
    else:
        checked_user.append(user_id)
    total_user_count += 1
    all_users_pk = all_users_pk.union(getFollowingsPk(user_id))
    api.getUsernameInfo(user_id)
    user = api.LastJson['user']
    print("username :", user['username'])

    user_feed = getLimitedUserFeed(user_id)
    if user['follower_count'] > FOLLOWING_COUNT_CELEBRITY_THRESHOLD :
        celebrity_user_count += 1
        for item in user_feed:
            media_count += 2 #celebrities media should be half of normal peoples/
            print("media count is :" , media_count)
            if media_count > MAX_MEDIA_COUNT:
                break
            readMediaComments(str(item['pk']), all_celebrity_comments)
    else:
        normal_user_count += 1
        for item in user_feed:
            media_count += 1
            print("media count is :" , media_count)
            if media_count > MAX_MEDIA_COUNT:
                break
            readMediaComments(str(item['pk']), all_friendly_comments)

    print("normal users : " , normal_user_count)
    print("celebrity users : ", celebrity_user_count)
#saving to file
    if(total_user_count % SAVE_BACKUP_PERIOD_USER_COUNT == 0):
        print("total_user_count is :", total_user_count)
    print("friendly comments :", all_friendly_comments, file=open("friendly_comments", "w"))
    print("celeb comments :", all_celebrity_comments, file=open("celebrity_comments", "w"))
        #pickle.dump(all_celebrity_comments, celebrity_comment_file)
#pickle.dump(all_friendly_comments, friendly_comment_file)



print("celeb comments :", all_celebrity_comments)
print("\n\n\n\n\n\n\n\n\n\n\n\n")
print("friendly comments :", all_friendly_comments)
print("normal users : " , normal_user_count)
print("celebrity users : ", celebrity_user_count)
                   # print(api.LastJson)
#get following
#api.getUsernameInfo("474059646")
#user = api.LastJson['user']
#follower_count = user['follower_count']
#print(follower_count)
#
#followings_pk = []
#next_max_id = True
#def getFollowingsPk(user_id):
#    followings_pk = set()
#    following_count = 0
#    while next_max_id and following_count < MAX_FOLLOWING_COUNT:
#        print (next_max_id)
#        # first iteration hack
#        if next_max_id is True:
#            next_max_id = ''
#        api.getUserFollowings(user_id, maxid=next_max_id)
#        for user in api.LastJson['users']:
#            followings_pk.append(user['pk'])
#            following_count += 1
#            if following_count > MAX_FOLLOWING_COUNT:
#                break
#        next_max_id = api.LastJson.get('next_max_id', '')

#print(followings_pk)
#print(len(followings_pk))

#api.getTotalUserFeed(user_id)
#print(api.LastJson)







#!/usr/bin/env python
# -*- coding: utf-8 -*-
#1350224639301548675
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
api = InstagramAPI("miladmohammadrezaei", "joejoe")
if (api.login()):
    #api.getSelfUserFeed()  # get self user feed
    #   print(api.LastJson)  # print last response JSON
    print("Login succes!")
else:
    print("Can't login!")

#my user id is : 474059646



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
            time.sleep(2)

def getFollowingsPk(user_id):
    next_max_id = True
    followings_pk = set()
    following_count = 0
    while next_max_id and following_count < MAX_FOLLOWING_COUNT:
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


FOLLOWING_COUNT_CELEBRITY_THRESHOLD = 2000
MAX_FOLLOWING_COUNT = 60
MAX_MEDIA_COUNT = 10
MAX_COMMENT_COUNT = 20
TOTAL_USER_COUNT = 7
all_users_pk = set()
all_users_pk.add("474059646")

all_friendly_comments = []

all_celebrity_comments = []

total_user_count = 0
celebrity_user_count = 0
normal_user_count = 0

while total_user_count < TOTAL_USER_COUNT:
    media_count = 0
    total_user_count += 1
    user_id = all_users_pk.pop()
    all_users_pk = all_users_pk.union(getFollowingsPk(user_id))
    api.getUsernameInfo(user_id)
    
    user = api.LastJson['user']
    print("username :", user['username'])
    api.getTotalUserFeed(user_id)
    if user['follower_count'] > FOLLOWING_COUNT_CELEBRITY_THRESHOLD :
        celebrity_user_count += 1
        for item in api.LastJson['items']:
            media_count += 2 #celebrities media should be half of normal peoples/
            print("media count is :" , media_count)
            if media_count > MAX_MEDIA_COUNT:
                break
            readMediaComments(str(item['pk']), all_celebrity_comments)
    else:
        normal_user_count += 1
        for item in api.LastJson['items']:
            media_count += 1
            print("media count is :" , media_count)
            if media_count > MAX_MEDIA_COUNT:
                break
            readMediaComments(str(item['pk']), all_friendly_comments)

    print("normal users : " , normal_user_count)
    print("celebrity users : ", celebrity_user_count)

print("celeb comments :", all_celebrity_comments)
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







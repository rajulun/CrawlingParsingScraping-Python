# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from jobparser.items import KontachItem

AccesToken = 'a9513eb06e1b38dadaee6cc78aec2b9e444bd4f234618b51b87b51b5dfee0d9cc57554d8184e48f20272a'
authentication = {'Authorization': 'token ' + AccesToken}

class KontachSpider(scrapy.Spider):
    name = 'kontach'
    allowed_domains = ['vk.com']
    users_id1 = '457242326'
    # users_id2 = '292243967'
    start_urls = [
        'https://api.vk.com/method/users.getFollowers?user_id=' + users_id1 + '&v=5.52&access_token=' + AccesToken]
        # 'https://api.vk.com/method/users.getFollowers?user_id=' + users_id2 + '&v=5.52&access_token=' + AccesToken]

    def parse(self, response):

        x = json.loads(response.text)
        without_response = (x["response"])
        friends1_1 = (without_response["items"])
        yield KontachItem(friends=friends1_1, user='user_1', deep='1')

        friends1_2 = self.get_friends(friends1_1, AccesToken)
        yield KontachItem(friends=friends1_2, user='user_1', deep='2')


        friends1_3 = self.get_friends(friends1_2, AccesToken)
        yield KontachItem(friends=friends1_3, user='user_1', deep='3')



        fff3 = '2'

    # def mutual_friends(self, user1, user2):
    #     mutual_f = []
    #     for aa in user1:
    #         if (aa in user2) and (aa not in mutual_f):
    #             mutual_f += [aa]
    #     return mutual_f
        # print(tmp)

    def get_friends(self, users, AccesToken):
        friends = []
        for i in range(len(users)):
            next_url = 'https://api.vk.com/method/users.getFollowers?user_id=' + str(
                users[i]) + '&v=5.52&access_token=' + AccesToken
            response = requests.get(next_url)
            x = json.loads(response.text)
            try:
                without_response = (x["response"])
            except:
                continue
            for i in range(len(without_response["items"])):
                friends.append(without_response["items"][i])
        return friends




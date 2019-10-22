from os.path import join, dirname
from dotenv import load_dotenv
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import json
from jobparser import settings
from jobparser.spiders.kontach import KontachSpider
from jobparser.spiders.kontach_2 import Kontach2Spider
from pymongo import MongoClient

do_env = join(dirname(__file__), '.env')
load_dotenv(do_env)

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(KontachSpider)
    process.crawl(Kontach2Spider)
    process.start()


client = MongoClient('localhost', 27017)
db = client.vkfriends

def mutual_friends(user1, user2):
    mutual_f = []
    for aa in user1:
        if (aa in user2) and (aa not in mutual_f):
            mutual_f += [aa]
    return mutual_f


friends1_1 = db.kontach.find({'deep':'1'}).distinct("friends")
friends2_1 = db.kontach_2.find({'deep':'1'}).distinct("friends")
if mutual_friends(friends1_1, friends2_1) != []:
    print("Глубина 2го порядка. Найдены общие друзья, при сравнении друзей 1го порядка первого человека "
                              "с друзьями 1го порядка второго человека")
else:
    print("Глубина 2го порядка, при сравнении друзей 1го порядка первого человека "
                              "с друзьями 1го порядка второго человека, общих друзей нет")
    friends1_2 = db.kontach.find({'deep': '2'}).distinct("friends")
    if mutual_friends(friends1_2, friends2_1) != []:
        print("Глубина 3го порядка. Найдены общие друзья, при сравнении друзей 2го порядка первого человека "
                              "с друзьями 1го порядка второго человека")
    else:
        print("Глубина 3го порядка, при сравнении друзей 2го порядка первого человека "
                              "с друзьями 1го порядка второго человека, общих друзей нет")
        friends2_2 = db.kontach_2.find({'deep': '2'}).distinct("friends")
        if mutual_friends(friends1_1, friends2_2) != []:
            print("Глубина 3го порядка. Найдены общие друзья, при сравнении друзей 1го порядка первого человека "
                              "с друзьями 2го порядка второго человека")
        else:
            print("Глубина 3го порядка, при сравнении друзей 1го порядка первого человека "
                              "с друзьями 2го порядка второго человека, общих друзей нет")
            if mutual_friends(friends1_2, friends2_2) != []:
                print("Глубина 4го порядка Найдены общие друзья, при сравнении друзей 2го порядка первого человека "
                              "с друзьями 2го порядка второго человека")
            else:
                print("Глубина 4го порядка при сравнении друзей 2го порядка первого человека "
                              "с друзьями 2го порядка второго человека, общих друзей нет")
                friends1_3 = db.kontach.find({'deep': '3'}).distinct("friends")
                if mutual_friends(friends1_3, friends2_1) != []:
                    print("Глубина 4го порядка. Найдены общие друзья, при сравнении друзей 3го порядка первого человека "
                              "с друзьями 1го порядка второго человека", mutual_friends(friends1_3, friends2_2))
                else:
                    print("Глубина-4, при сравнении друзей 3го порядка первого человека "
                              "с друзьями 1го порядка второго человека, общих друзей нет")
                    if mutual_friends(friends1_3, friends2_2) != []:
                        print("Глубина 5го порядка. Найдены общие друзья, при сравнении друзей 3го порядка первого человека "
                              "с друзьями 2го порядка второго человека", mutual_friends(friends1_3, friends2_2))
                    else:
                        print("Глубина 5го порядка. При сравнении друзей 3го порядка первого человека "
                            "с друзьями 2го порядка второго человека, общих друзей не найдено")
                        friends2_3 = db.kontach_2.find({'deep': '3'}).distinct("friends")
                        if mutual_friends(friends1_1, friends2_3) != []:
                            print("Глубина 4го порядка. Найдены общие друзья, при сравнении друзей 1го порядка первого человека "
                              "с друзьями 3го порядка второго человека", mutual_friends(friends1_3, friends2_2))
                        else:
                            print("Глубина 4го порядка. При сравнении друзей 1го порядка первого человека "
                                "с друзьями 3го порядка второго человека, общих друзей не найдено")
                            if mutual_friends(friends1_2, friends2_3) != []:
                                print("Глубина 5го порядка. Найдены общие друзья, при сравнении друзей 2го порядка первого человека "
                                        "с друзьями 3го порядка второго человека", mutual_friends(friends1_2, friends2_3))
                            else:
                                print("Глубина 5го порядка. При сравнении друзей 2го порядка первого человека "
                                        "с друзьями 3го порядка второго человека, общих друзей не найдено")
                                if mutual_friends(friends1_3, friends2_3) != []:
                                    print("Глубина 6го порядка, Найдены общие друзья, при сравнении друзей 3го порядка первого человека "
                                            "с друзьями 3го порядка второго человека", mutual_friends(friends1_3, friends2_3))
                                else:
                                    print("Глубина 6го порядка, При сравнении друзей 3го порядка первого человека "
                                                "с друзьями 3го порядка второго человека, общих друзей не найдено")


f = 'fff'
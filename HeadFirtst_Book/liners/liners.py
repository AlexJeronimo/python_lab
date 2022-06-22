# import os
#
# os.chdir('E:\Projects\python_lab\HeadFirtst_Book\generator')
#
# with open('buzzdata.csv') as raw_data:
#     print(raw_data.read())


# import csv

# with open('buzzdata.csv') as data:
#     for line in csv.reader(data):
#         print(line)


# with open('buzzdata.csv') as data:
#     for line in csv.DictReader(data):
#         print(line)


# with open('buzzdata.csv') as data:
#     ignore = data.readline()
#     flights = {}
#     for line in data:
#         k, v = line.strip().split(',')
#         flights[k] = v

# print(flights)

# import pprint

# pprint.pprint(flights)
#
# print(type(flights))
# print(flights)
# from datetime import datetime
#
#
# def convert2ampm(time24: str) -> str:
#     return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')
#
#
# flights2 = {}
# for k, v in flights.items():
#     # k = convert2ampm(k)
#     # v = v.title()
#     # flights2[k] = v
#     flights2[convert2ampm(k)] = v.title()
# # pprint.pprint(flights2)
#
# more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}
# # pprint.pprint(more_flights)
#
# destinations = []
# for dest in flights.values():
#     destinations.append(dest.title())
#
# more_dests = [dest.title() for dest in flights.values()]
#
# just_freeport = {}
# for k, v in flights.items():
#     if v == 'FREEPORT':
#         just_freeport[convert2ampm(k)] = v.title()
#
# just_freeport2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == "FREEPORT"}
#
# # print(just_freeport)
# # print(just_freeport2)
#
#
# # print(destinations)
# # print(more_dests)
#
# flight_times = []
# for ft in flights.keys():
#     flight_times.append(convert2ampm(ft))
#
# fts2 = [convert2ampm(ft) for ft in flights.keys()]
#
# # print(flight_times)
# # print(fts2)
#
#
# fts = {convert2ampm(k): v.title() for k, v in flights.items()}
# # pprint.pprint(fts)
#
# dests = set(fts.values())
# # print(dests)

# wests = []
# for k,v in fts.items():
#     if v == 'West End':
#         wests.append(k)
# # print(wests)
#
# wests2 = [k for k, v in fts.items() if v == 'West End']
# # print(wests2)
#
#
# for dest in set(fts.values()):
#     print(dest, '->', [k for k,v in fts.items() if v == dest])
#
# when = {}
# for dest in set(fts.values()):
#     when[dest] = [k for k, v in fts.items() if v == dest]
# # pprint.pprint(when)
#
#
# when2 ={dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
# print(when2)

# vowels = {'a', 'e', 'i', 'o', 'u'}
# message = "Don't forget to pack your towel."
#
# found = set()
# for v in vowels:
#     if v in message:
#         found.add(v)
# print(found)
#
# found2 = {v for v in vowels if v in message}
# print(found2)


# import requests

# urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')

# for resp in [requests.get(url) for url in urls]:
#     print(len(resp.content), '->', resp.status_code, '->', resp.url)

# for resp in (requests.get(url) for url in urls):
#     print(len(resp.content), '->', resp.status_code, '->', resp.url)


from url_utils import gen_from_urls

urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com', 'https://habr.com')

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)


urls_res = {url: size for size, _, url in gen_from_urls(urls)}
import pprint
pprint.pprint(urls_res)
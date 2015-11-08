# test
import requests
import twitter
import time
from datetime import datetime, timedelta
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('kd2718', 'qlrq59nuu4')

api = twitter.Api(consumer_key='W75oAzPKpf3h8htqNVUGE9alx',
                      consumer_secret='8XdFVuUflEVyrge6irnfJE2JHJlrF6Cri4W6ezzeKfiKBVuGO9',
                      access_token_key='3192491525-PFRsu8qEjKKxY7yChILd9fUNm5WkLaSFAyIyyfJ',
                      access_token_secret='bKMWw5InXgTnkNj6ozz90qYuMrBa0Z2Qkv2t9KrSbbBfy')

# print api.VerifyCredentials()

k = api.GetStreamFilter(track=['#TheForceAwakens', '#StarWars'])
# k = api.GetStreamFilter(track='jsjklfkasfjdjhashdfj;lkasfd')

trace1 = Scatter(
        x=[],
        y=[],
        stream=dict(token='a4ko2otwjm',
        maxpoints=24
        )
    )
data = Data([trace1])
py.plot(data)
s = py.Stream('a4ko2otwjm')
s.open()


start = datetime.now()
count = 0
try:
    while True:
        next(k)
        count += 1
        if datetime.now() - start > timedelta(seconds=5):
            s.write(dict(x=start, y=count))
            # print count
            count=0
            start = datetime.now()
finally:
    s.close()



# for a in k:
#     print a
#     print
#     print
#     # time.sleep(2)

import time
import redis

client = redis.Redis(host='172.28.7.40', port='6379', password='123456')
while True:
    data = client.lpop('example:swarm:spider')
    if not data:
        print("here")
        break
    print(f'我现在获取的数据为：{data.decode()}')
    time.sleep(10)

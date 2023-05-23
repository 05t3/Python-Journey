from fake_useragent import UserAgent

ua = UserAgent()

for _ in range(500):
    random_useragent = ua.random
    print(random_useragent)

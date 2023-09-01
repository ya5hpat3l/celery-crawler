from tasks import fetch

urllist = [
]

with open("./top500.csv", "r") as file:
    lines = file.read().split("\n")[1:]
    [urllist.append("https://"+url.split(",")[1].strip('"')) for url in lines if len(url) > 0]


# print(urllist)

[fetch.delay(i) for i in urllist if print(f"queued: {i}")]
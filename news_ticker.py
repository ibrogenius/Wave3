headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = list()

for headline in headlines:
    if len(str(news_ticker)) >= 140:
        break
    else:
        news_ticker.append(headline)

print(news_ticker)

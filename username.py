names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = [item.lower().replace(" ", "_") for item in names]
print(usernames)
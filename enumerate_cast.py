cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, j in enumerate(cast):
    #cast[i] = j, str(heights[i])
    cast[i] = j + " " + str(heights[i])
print(cast)
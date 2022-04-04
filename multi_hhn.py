import json
import sys
from PIL import Image
from place_bot import Placer, Color

placer = Placer()
X = int(sys.argv[1])
Y = int(sys.argv[2])
filename = sys.argv[3]

img = Image.open(filename)
W = img.width
H = img.height
img.close()

users = json.load(open("users.json", "r"))
for user in users:
    print("logging in:",user["username"])
    placer.login(user["username"], user["password"])


placer.maintain_image(X, Y, filename, (H, W))

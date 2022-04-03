import sys
from place_bot import Placer, Color
from PIL import Image



if len(sys.argv) <= 5:
    print("usage: python3 place_tile.py [reddit username] [reddit password] [X] [y] [filename]")
    exit()

username = sys.argv[1]
password = sys.argv[2]
X = int(sys.argv[3])
Y = int(sys.argv[4])
filename = sys.argv[5]

placer = Placer()
placer.login(username, password)

while True:
    try:
        print("starting maintain_image")
        placer.maintain_image(X, Y, filename, (3, 10))
    except:
        print("!!!Something went wrong when maintaining, restarting!!!")


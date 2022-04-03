import sys
from place_bot import Placer, Color
from PIL import Image



if len(sys.argv) <= 4:
    print("usage: python3 place_tile.py [reddit username] [reddit password] [X] [y]")
    exit()

username = sys.argv[1]
password = sys.argv[2]
X = int(sys.argv[3])
Y = int(sys.argv[4])

placer = Placer()
placer.login(username, password)


placer.maintain_image(X, Y, 'HHN-3x10.png', (3, 10))


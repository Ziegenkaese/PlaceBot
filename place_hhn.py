import sys
from place_bot import Placer, Color
from PIL import Image



#if len(sys.argv) != 3:
#    print("usage: python3 place_tile.py [reddit username] [reddit password]")
#    exit()

username = "hhn-test"
password = "INSERT PASSWORT HERE"

placer = Placer()
placer.login(username, password)


placer.maintain_image(1812, 826, 'HHN-3x10.png', (3, 10))


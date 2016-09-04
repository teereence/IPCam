import math
from PIL import Image, ImageChops
import io

from src.controller import ImageOperations
from src.controller.Config import Config
from src.controller.ImageOperations import ImageDifference
from src.controller.Snapshot import Snapshot
from src.controller.Storage import Storage

config = Config()
storage = Storage()

snapshot = Snapshot(config, storage)

img1_data = io.BytesIO(snapshot.get(False))
img2_data = io.BytesIO(snapshot.get(False))

diff = ImageDifference(img1_data, img2_data).difference()
print(diff)





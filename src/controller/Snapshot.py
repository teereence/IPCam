from PIL import Image, ImageDraw, ImageFont
import io
import os
import urllib3
import datetime


def add_overlay(img_data):
    overlay_text = datetime.datetime.now()
    stream = io.BytesIO(img_data)
    img = Image.open(stream)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 14)
    draw.text((10, 10), str(overlay_text), (255, 255, 255), font=font)
    draw = ImageDraw.Draw(img)

    io_byte_array = io.BytesIO()
    img.save(io_byte_array, format='JPEG')
    return io_byte_array.getvalue()


class Snapshot():
    def __init__(self, config, storage, verbose=False, start=0):
        self.snapshot = None
        self.verbose = verbose
        self.config = config
        self.storage = storage
        self.iteration = start

    def get(self, date=True):
        base_url = self.config.baseUrl
        values = self.config.userSettings
        data = '&'.join((k + '=' + values.get(k) for k in values.keys()))
        req = base_url + '?' + data
        http = urllib3.PoolManager()
        response = http.request('GET', req)

        snap = response.data
        if date:
            snap = add_overlay(snap)
        self.snapshot = snap
        return snap

    def export(self):
        directory = self.storage.directory()
        file_name = str(self.iteration) + self.storage.snap_extension
        full_path = os.path.join(directory, file_name)
        writer = open(full_path, 'wb')
        self.iteration +=1
        snap = self.get()
        writer.write(snap)
        writer.close()

        if self.verbose:
            print ('wrote snap in ' + full_path)

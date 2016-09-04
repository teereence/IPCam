import urllib3

class Snapshot() :
    def __init__(self, config, storage, verbose = False, start=0) :
        self.snapshot = None
        self.verbose = verbose
        self.config = config
        self.storage = storage
        self.iteration = start

    def get(self, date=True) :
        baseUrl = self.config.baseUrl
        values = self.config.userSettings
        data = '&'.join(( k + '='+ values.get(k) for k in values.keys()))
        req = baseUrl+ '?' + data
        response = urllib3. .urlopen(req)
        snap = response.read()
        if date:
            snap = self.add_overlay(snap)
        self.iteration = self.iteration + 1
        self.snapshot = snap
        return snap

    def add_overlay(self, img_data):
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

    def export(self):
        directory = self.storage.directory()
        fileName = str(self.iteration) + storage.extension
        fullPath = os.path.join(directory, fileName)
        writer = open(fullPath, 'w')
        self.iteration = self.iteration + 1
        snap = self.get()
        writer.write(snap)
        writer.close()

        if self.verbose:
            print
            'wrote snap in ' + fullPath



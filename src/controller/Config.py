import os


class Config():
    def __init__(self, base_path='.'):
        self.basePath = base_path
        self.baseUrl = 'http://192.168.1.55/snapshot.cgi'
        self.userSettings = {'user': 'admin', 'pwd': ''}
        if not (self.check_path()):
            print('Directory ' + self.basePath + ' does not exist. Creating it in ' + os.path.abspath(os.curdir))
            os.makedirs(os.path.join(os.curdir, base_path))

    def check_path(self):
        return os.path.exists(self.basePath)

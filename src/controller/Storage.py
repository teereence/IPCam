

class Storage() :
    def __init__(self) :
        self.extension = '.jpg'
        self.date = datetime.datetime.now()
        self.currentDirectory = self.createDirectory()

    def createDirectory(self) :
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day

        dirName = '-'.join((str(year), str(month), str(day)))
        baseDir = config.basePath
        storageDir = os.path.join(baseDir, dirName)
        if not os.path.exists(storageDir) :
            os.mkdir(storageDir)
        return storageDir

    def last_file_number(self) :
        last_iteration_written = max(map(lambda x: int(x.split('.')[0]), os.listdir(storage.currentDirectory)))
        return last_iteration_written

    def directory(self) :
        now = datetime.datetime.now()
        day_now = now.day
        start_day = self.date.day
        delta = day_now - start_day
        if delta!= 0:
            directory = createDirectory(self)
            self.currentDirectory = directory
            self.date = datetime.datetime.now()

        return self.currentDirectory

    def fileName(self):
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        sec = now.second
        ms = now.microsecond / 100
        fileName = ':'.join((str(hour), str(minute), str(sec), str(ms))) + '.jpg'
        return fileName

    def writeFile(self, directory, fileName, snap):
        pipe = open(os.path.join(directory, fileName), 'w')
        pipe.write(snap)
        pipe.close()

    def makeVideo(self, source_directory=None, directory=None, file_name=None):
        if directory is None:
            export_dir = self.currentDirectory
        else:
            export_dir = directory

        if source_directory is None:
            source_dir = self.currentDirectory
        else:
            source_dir = source_directory

        if file_name is None:
            name = self.currentDirectory.split(os.path.sep)[-1] + '.avi'
        else:
            name = file_name
        command = 'avidemux --load ' + os.path.join(source_dir, '*') + ' --save ' + os.path.join(export_dir,
                                                                                                 name) + ' --output_format "AVI" --quit'
        print
        command


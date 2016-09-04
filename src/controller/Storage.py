import datetime
import os


def create_directory(config) :
    """

    :param config: Config() object
    :return:
    """
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if config is not None :
        base_dir = config.basePath
    else :
        base_dir = '.'

    dir_name = '-'.join((str(year), str(month), str(day)))
    storage_dir = os.path.join(base_dir, dir_name)
    if not os.path.exists(storage_dir) :
        os.mkdir(storage_dir)
    return storage_dir


def file_name():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    sec = now.second
    ms = now.microsecond / 100
    f_name = ':'.join((str(hour), str(minute), str(sec), str(ms))) + '.jpg'
    return f_name


def write_file(directory, file_name, snap):
    """
    :type file_name: string
    """
    pipe = open(os.path.join(directory, file_name), 'w')
    pipe.write(snap)
    pipe.close()


class Storage() :
    def __init__(self, config = None) :
        self.snap_extension = '.jpg'
        self.video_extension = '.avi'
        self.date = datetime.datetime.now()
        self.currentDirectory = create_directory(config)

    def last_file_number(self) :
        last_iteration_written = max(map(lambda x: int(x.split('.')[0]), os.listdir(self.currentDirectory)))
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

    def make_video(self, source_directory=None, directory=None, file_name=None):
        if directory is None:
            export_dir = self.currentDirectory
        else:
            export_dir = directory

        if source_directory is None:
            source_dir = self.currentDirectory
        else:
            source_dir = source_directory

        if file_name is None:
            name = self.currentDirectory.split(os.path.sep)[-1] + self.video_extension
        else:
            name = file_name
        command = 'avidemux --load ' \
                + os.path.join(source_dir, '*') + ' --save '\
                + os.path.join(export_dir, name) + ' --output_format "AVI" --quit'
        print(command)

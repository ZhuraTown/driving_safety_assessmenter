import os


DIR_FILES = "files"

TRACK_PICT = "track.png"
CAR_PICT = "tesla.png"


class Files:

    _BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def get_path_car_picture():
        return os.path.join(Files._BASE_DIR, DIR_FILES, CAR_PICT)

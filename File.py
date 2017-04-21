import json
import numpy


def delete_content(file_path):
    with open(file_path, "w") as file:
        file.seek(0)
        file.truncate()
        file.close()


def write_file(file_path, data):
    delete_content(file_path)

    with open(file_path, "w") as dataFile:
        dataFile.write(json.dumps(data, cls=Encoder))
        dataFile.close()


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.int64):
            return int(obj)
        else:
            return super(Encoder, self).default(obj)

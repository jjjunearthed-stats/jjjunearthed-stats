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
        dataFile.write(json.dumps(data, cls=MyEncoder))
        dataFile.close()


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.int64):
            return int(obj)
        elif isinstance(obj, numpy.float64):
            return float(obj)
        else:
            return super(MyEncoder, self).default(obj)

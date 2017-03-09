import json


def delete_content(file):
    file.seek(0)
    file.truncate()


def write_file(file_path, data):
    with open(file_path, "w") as dataFile:
        delete_content(dataFile)
        dataFile.write(json.dumps(data))
        dataFile.close()

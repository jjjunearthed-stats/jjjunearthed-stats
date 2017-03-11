import json


def delete_content(file_path):
    with open(file_path, "w") as file:
        file.seek(0)
        file.truncate()
        file.close()


def write_file(file_path, data):
    delete_content(file_path)

    with open(file_path, "w") as dataFile:
        dataFile.write(json.dumps(data))
        dataFile.close()

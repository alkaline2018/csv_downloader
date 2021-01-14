import datetime
import os

def get_today_ago_n_str(ago_day):
    today = datetime.datetime.today()
    today_ago_day = today - datetime.timedelta(days=ago_day)
    return today_ago_day.strftime("%Y%m%d")


def get_today_str():
    today = datetime.datetime.today()
    return today.strftime("%Y%m%d")


def write_file(file_content, file_path):
    try:
        csv_file = open(file_path, "wb")
        csv_file.write(file_content)
        csv_file.close()

    except Exception as e:
        print(f'Error: {e}')


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

# class Util:
#     def __init__(self):
#         pass




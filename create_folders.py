import os


def create_100_dir(root_path):
    for one_dir in range(100):
        if one_dir < 10:
            one_dir = f'0{str(one_dir)}'
        os.makedirs(f'{root_path}/{one_dir}')


def create_dir():

    create_100_dir('.')

    for current_dir in range(100):
        if current_dir < 10:
            current_dir = f'0{str(current_dir)}'

        create_100_dir(current_dir)


if __name__ == '__main__':
    create_dir()

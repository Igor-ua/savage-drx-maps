import glob


class _Context:
    MAPS_PATH = '../'


def print_repository_status():
    files_s2z = glob.glob(_Context.MAPS_PATH + '/*.s2z')
    files_jpg = glob.glob(_Context.MAPS_PATH + '/*.jpg')
    print(f's2z files amount: {len(files_s2z)}')
    print(f'jpg files amount: {len(files_jpg)}')

    files_s2z_name = [f.split('.s2z')[0] for f in files_s2z]
    files_jpg_name = [f.split('_overhead.jpg')[0] for f in files_jpg]

    files_s2z_without_headers = []
    files_jpg_without_s2z = []

    for file in files_s2z_name:
        if file not in files_jpg_name:
            files_s2z_without_headers.append(file)

    for file in files_jpg_name:
        if file not in files_s2z_name:
            files_jpg_without_s2z.append(file)

    files_s2z_without_headers.sort()
    files_jpg_without_s2z.sort()

    print(f'files_s2z_without_headers: {files_s2z_without_headers}')
    print(f'files_jpg_without_s2z: {files_jpg_without_s2z}')


print_repository_status()

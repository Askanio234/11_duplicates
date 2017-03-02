import os
import collections
import argparse


def find_all_files_in_folder(filepath):
    all_files = collections.defaultdict(list)
    for root, dirs, files in os.walk(filepath):
        for file_name in files:
            full_file_name = os.path.join(root, file_name)
            key = (os.path.getsize(full_file_name), file_name)
            all_files[key].append(full_file_name)
    return all_files


def find_duplicates(all_files):
    for size, file_name in sorted(all_files):
        list_of_filepaths = all_files[(size, file_name)]
        if len(list_of_filepaths) > 1:
            print(" {0} ({1}) bytes are duplicates "
                "({2} files):".format(file_name, size, len(list_of_filepaths)))
            for file_path in list_of_filepaths:
                print("\t{0}".format(file_path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Путь к папке")
    args = parser.parse_args()
    if os.path.exists(args.filepath):
        find_duplicates(find_all_files_in_folder(args.filepath))
    else:
        print("Некорректный путь до файла")

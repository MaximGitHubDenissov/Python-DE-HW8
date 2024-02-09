'''
2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

'''
from pathlib import Path

import os
import json
import csv
import pickle


def get_dir_size(start_path='.'):
    total_size = 0
    for dir_path, dir_names, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dir_path, f)
            total_size += os.path.getsize(fp)
        for d in dir_names:
            dp = os.path.join(dir_path, d)
            total_size += get_dir_size(dp)
    return total_size


def save_results_to_json(results, file_name):
    with open(file_name, 'w') as f:
        json.dump(results, f)


def save_results_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Type', 'Size'])
        for result in results:
            writer.writerow([result['Path'], result['Type'], result['Size']])


def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(results, f)


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results


if __name__ == '__main__':
    save_results_to_json(traverse_directory(r'C:\Users\77017\PycharmProjects\python_data_hw_8'), 'result.json')
    save_results_to_pickle(traverse_directory(r'C:\Users\77017\PycharmProjects\python_data_hw_8'), 'result.pickle')
    save_results_to_csv(traverse_directory(r'C:\Users\77017\PycharmProjects\python_data_hw_8'), 'result.csv')
    print(traverse_directory(r'C:\Users\77017\PycharmProjects\python_data_hw_8'))

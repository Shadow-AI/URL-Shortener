import random as rand
import requests
import csv
import pickle


class ParentValues:
    host_name = 'localhost:8000/a?i='
    # test=10
    try:
        with open('D:\\linkMapper.pickle', 'rb') as fp:
            linkMapper = pickle.load(fp)
    except FileNotFoundError:
        linkMapper = {}

    try:
        with open('D:\\ageMapper.pickle', 'rb') as fp:
            ageMapper = pickle.load(fp)
    except FileNotFoundError:
        ageMapper = {}

    try:
        with open('D:\\total.pickle', 'rb') as fp:
            total_count = pickle.load(fp)
            total_count = int(total_count['total_count'])
    except FileNotFoundError:
        total_count = 0

    try:
        with open('D:\\oldest.pickle', 'rb') as fp:
            oldest = pickle.load(fp)
            oldest = int(oldest['oldest'])
    except FileNotFoundError:
        oldest = 1

    maximum_entries = 52 * 52 * 52 * 52 * 10

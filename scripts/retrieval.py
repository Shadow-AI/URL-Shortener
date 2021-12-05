import pickle

from scripts.main import ParentValues
from scripts.gen import Generator


class Retrieve(ParentValues):
    def __init__(self, user_link):
        self.user_link = user_link

    def searchLink(self):
        # print(ParentValues.test)
        # with open('D:\linkMapper.pickle', 'rb') as fp:
        #     print(pickle.load(fp))
        try:
            m=self.linkMapper[self.user_link]
            return m
        except Exception as efgr:
            print(efgr)
            exit(1)
            # return 'bhai ye kya dale ho tum'

    def lol(self):
        return self.linkMapper

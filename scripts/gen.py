from scripts.main import ParentValues
import random as rand
import requests
import pickle


class Generator(ParentValues):
    def generateKey(self):
        positions = {}

        if self.total_count < self.maximum_entries:

            num_pos = rand.randint(0, 5)
            if not num_pos == 0:
                positions[num_pos] = rand.randint(0, 9)

            for i in range(1, 6):
                caps = False
                if i == num_pos:
                    continue
                if rand.randint(0, 1) == 1:
                    caps = True
                if caps:
                    positions[i] = chr(rand.randint(65, 90))
                else:
                    positions[i] = chr(rand.randint(97, 122))

            tlink = ''
            # print(f'{tlink} and {positions}')
            for i in range(1, 6):
                tlink = tlink + str(positions[i])
            if not self.keyPresent(tlink):
                fLink = self.host_name + tlink
            else:
                self.generateKey()

            self.total_count += 1
            self.ageMapper[self.total_count] = fLink

        else:

            fLink = self.ageMapper[self.oldest]
            # self.oldest+=1
            if self.oldest == self.maximum_entries:
                self.oldest = 1
            else:
                self.oldest += 1

        return fLink

    def keyPresent(self, key):
        f = self.linkMapper.get(key)
        if f == None:
            return False
        else:
            return True

    def validateURL(self, user_link):

        # Part where https:// is appended to the start of the URL string
        if user_link[:4] == 'http':
            if user_link[4:7] == '://':
                user_link = 'https://' + user_link[7:]

            elif user_link[4:8] == 's://':
                pass
            else:
                return('Invalid URL Syntax')

        else:
            user_link = 'https://' + user_link

        #     try:
        #         if user_link == 'https://':
        #             raise InvalidURLError
        #     except:
        #         print('No URL entered')

        emptyLink = False
        # print(user_link)
        try:

            if user_link == 'https://':
                emptyLink = True
            try:
                if emptyLink:
                    raise Exception('No URL Entered')
            except:
                return('No URL Entered')


            else:
                validator = requests.get(user_link)

                # print(f'{validator}')
                # validator=requests.get(user_link)
                f = True
                for i in range(400, 452):
                    if i == validator.status_code:
                        return(
                            f"Server Response Code: {validator.status_code}\nThis link can't be parsed due to a client error")
                        f = False
                        break
                for i in range(500, 512):
                    if i == validator.status_code:
                        return(
                            f"Server Response Code: {validator.status_code}\nThis link can't be parsed due to a server error")
                        f = False
                        break
                if f:
                    return self.addKey(user_link)
        except requests.ConnectionError:
            return('The site provided does not exist')
        # return 'lmao'

    def addKey(self, user_link):
        file = self.generateKey()
        dat = file.split('/a?i=')
        dat = str(dat[1])
        self.linkMapper[dat] = user_link
        self.writeValues()
        print(self.linkMapper)
        print(self.ageMapper)
        return file


    def writeValues(self):
        a = {'total_count': self.total_count}
        b = {'oldest': self.oldest}
        with open('D:\\oldest.pickle', 'wb') as fp:
            pickle.dump(b, fp, protocol=pickle.HIGHEST_PROTOCOL)
        with open('D:\\total.pickle', 'wb') as fp:
            pickle.dump(a, fp, protocol=pickle.HIGHEST_PROTOCOL)
        with open('D:\\linkMapper.pickle', 'wb') as fp:
            pickle.dump(self.linkMapper, fp, protocol=pickle.HIGHEST_PROTOCOL)
        with open('D:\\ageMapper.pickle', 'wb') as fp:
            pickle.dump(self.ageMapper, fp, protocol=pickle.HIGHEST_PROTOCOL)

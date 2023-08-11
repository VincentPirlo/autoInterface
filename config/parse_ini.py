import configparser


class ParseIni:
    def geturl(self, filename, sec, ops):
        conf = configparser.ConfigParser()
        conf.read(filename)
        s_url = conf.get(sec, ops)
        # print(s_url, type(s_url))
        return s_url

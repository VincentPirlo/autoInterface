import configparser


def geturl(filename, sec, opts):
    config = configparser.ConfigParser()
    config.read(filename)
    # s_url = config['url']['swagger_url']
    # print(s_url)
    s_url = config.get(sec, opts)
    return s_url

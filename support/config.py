import json
import typing
import sys
from collections import namedtuple
from urllib.parse import urlparse

from .password import (invalidPass, savePass, inputPass, checkPassLen)

Config = namedtuple('Config', 'serverAddr serverPort localAddr localPort password')


class InvalidURLError(Exception):
    """Invalid config URL"""
    #print ("Invalid config URL")


def loadURL(url):
    # url: str
    url_temp = urlparse(url, allow_fragments=True)
    url = url_temp
    serAddr_temp = url.hostname
    if serAddr_temp is not None:
        pass
    else:
        print ("No hostname")
        sys.exit()
    serverAddr = serAddr_temp
    serport_temp = url.port
    if serport_temp is not None:
        pass
    else:
        print ("No port open")
        sys.exit()
    serverPort = serport_temp
    pass_temp = url.fragment
    if serport_temp is not None:
        pass
    else:
        print ("No port open")
        sys.exit()
    password = pass_temp

    try:
        # Verify password validity
        pass_temp = inputPass(password)
        password = pass_temp
    except invalidPass:
        raise InvalidURLError

    if checkPassLen(password) is True:
        pass
    else:
        raise invalidPass
    return Config(serverAddr=serverAddr, serverPort=serverPort, localAddr='127.0.0.1', localPort=1080, password=password)


def dumpURL(config):
    # config: Config
    con = config._replace(password=savePass(config.password))
    if con is not None:
        pass
    else:
        raise invalidPass
    config = con

    try:
        url_temp = 'http://{serverAddr}:{serverPort}/#{password}'
        
        url = url_temp.format_map(config._asdict())
    except:
        print ("url error")
        raise InvalidURLError

    return url


def dumps(config) :
    # config: Config
    if config is not None:
        pass
    else:
        print ("empty config")
        sys.exit()
    config = config._replace(password=savePass(config.password))
    return json.dumps(config._asdict(), indent=2)


def loads(string):
    # string: str
    try:
        ss = json.load(string)
        if ss is not None:
            pass
        else:
            print("loads empty")
        data = ss
        conf = Config(**data)
        config = conf

        config = config._replace(password=inputPass(config.password))

        # Verify Addr validity
        # Verify Port validity
    except Exception:
        raise InvalidURLError

    return config


#!/usr/bin/python2.7


# general imports
from bson import json_util
from datetime import datetime, timedelta
import json
import logging
import os
import sys
from pymongo import MongoClient

# project-specific imports
import settings


# random, one-off helpers in the main namespace

mdb = MongoClient()[settings.get("api","mdb")]
ymd = "%Y-%m-%d"
hms = "%H:%M:%S"
ymdhms = "%Y-%m-%d %H:%M:%S"
thirty_days_ago = datetime.now() - timedelta(days=30)
recent_session_cutoff = datetime.now() - timedelta(hours=12)


# laziness and DRYness methods

def cli_dump(key, spacer, value):
    """ Returns a command line interface pretty string for use in admin scripts
    and other things that dump strings to CLI over STDOUT. """

    spaces = spacer - len(key)

    output = "%s:" % key
    output += " " * spaces
    output += "%s" % value

    print(output)

def seconds_to_hms(seconds):
    """ Converts seconds (expressed as int) to a h:m:s string. """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def search_dict(d, search_string, search_key="name"):
    """ Performs a case-insensitive search of all values for 'search_key'
    and returns d[search_key] if a match to search_string is found.

    Returns None otherwise. """

    search_string = search_string.upper()
    s = {}

    for asset_handle in d.keys():
        asset_dict = d[asset_handle]
        if search_key in asset_dict.keys():
            search_value = asset_dict[search_key].upper()
            s[search_value] = asset_dict


    if search_string in s.keys():
        return s[search_string]
    else:
        return None


# general usage methods

def get_logger(log_level=None, log_name=None):
    """ Initialize a logger, specifying a new file if necessary. """
    logger = logging.getLogger(__name__)

    if not len(logger.handlers):    # if it's not already open, open it

        # set the file name or default to the script asking for the logger
        log_file_name = log_name
        if log_name is None:
            log_file_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        log_handler_level = log_level

        # do the same for log level, defaulting to the server's 'log_level'
        if log_handler_level is None:
            logger.setLevel(settings.get("server","log_level"))
        elif type(log_handler_level) == str:
            exec 'log_level_obj = logging.%s' % log_level
            logger.setLevel(log_level_obj)
        else:
            logger.setLevel(log_handler_level)

        # now check the logging root, just as a precaution
        log_root_dir = settings.get("api","log_dir")
        if not os.path.isdir(log_root_dir):
            e = Exception("Logging root dir '%s' does not exist!" % log_root_dir)
            raise e

        # create the path and add it to the handler
        log_path = os.path.join(log_root_dir, log_file_name + ".log")
        logger_fh = logging.FileHandler(log_path)

        #   set the formatter and add it via addHandler()
        formatter =  logging.Formatter('[%(asctime)s] %(levelname)s:\t%(message)s', ymdhms)
        logger_fh.setFormatter(formatter)
        logger.addHandler(logger_fh)

    return logger


class AssetDict(dict):
    """ Creates a dictionary with additional attributes. """

    def __init__(self, d={}, attribs={}):
        """ Initialize with any dictionary and then use the 'attribs' kwarg as a
        dictionary of arbitry key/value pairs that will become attribs of the
        dictionary. """

        self.meta_attribs = attribs

        for k, v in self.meta_attribs.iteritems():
            if type(v) == str:
                exec "self.%s = '%s'" % (k,v)
            else:
                exec "self.%s = %s" % (k,v)

        self.update(d)
        self.add_vars_to_dict()

    def add_vars_to_dict(self):
        """ Adds the arbitrary attribs of the dictionary to each asset in the dict
        as an __whatever__ value. """

        for d in self.keys():
            self[d]["handle"] = d
            for k, v in self.meta_attribs.iteritems():
                key = "__%s__" % k
                self[d][key] = v


def asset_object_to_json(asset):
    """ Takes one of our asset objects and coerces it to json, stripping it of
    internal-use attributes, logger objects, etc. that is not serializeable or
    relevant to an object retrieval. """


    for banned_attrib in ["logger", "class_assets"]:
        if hasattr(asset, banned_attrib):
            delattr(asset, banned_attrib)

    return json.dumps(asset.__dict__, default=json_util.default)


# private exception classes

class AssetError(Exception):
    """ Handler for asset-based errors. """

    def __init__(self, message="Incorrect asset usage!"):
        self.logger = get_logger()
        self.logger.exception(message)
        Exception.__init__(self, message)

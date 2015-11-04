#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
#
# Config reader to read the configuration file
#
# Software is free software released under the "Modified BSD license"
#
# Copyright (c) 2014-2015 	Pieter-Jan Moreels - pieterjan.moreels@gmail.com

# imports
import sys
import os
runPath = os.path.dirname(os.path.realpath(__file__))

if sys.version_info >= (3, 0):
  import configparser
else:
  import ConfigParser as configparser

class Configuration():
  ConfigParser = configparser.ConfigParser()
  ConfigParser.read(os.path.join(runPath, "../etc/configuration.ini"))
  default = {'db':     "./NSS.lite", 'tables': ["HoneyTokens"],
             'action': "drop",       'actions': ["accept", "drop", "block"]}

  @classmethod
  def readSetting(cls, section, item, default):
    result = default
    try:
      if type(default) == bool:
        result = cls.ConfigParser.getboolean(section, item)
      elif type(default) == int:
        result = cls.ConfigParser.getint(section, item)
      else:
        result = cls.ConfigParser.get(section, item)
    except:
      pass
    return result

  # Defaults
  @classmethod
  def getDefaultAction(cls):
    return cls.readSetting("Defaults", "Action", cls.default['action'])
  @classmethod
  def getActions(cls):
    return cls.readSetting("Defaults", "Actions", cls.default['actions'])
  @classmethod
  def getTables(cls):
    return cls.readSetting("DB", "Tables", cls.default['tables'])
  @classmethod
  def getDB(cls):
    return cls.readSetting("DB", "Path", cls.default['db'])

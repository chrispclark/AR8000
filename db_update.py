#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 16:20:53 2018

@author: chrissy
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from db_create import Radio, Base
 
engine = create_engine('sqlite:///radio.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# Insert a Person in the person table
new_station = Radio(channel_name='LBC', channel_frequency ="97.3", channel_band = "LSB")
session.add(new_station)
session.commit()
new_station = Radio(channel_name='BBC', channel_frequency ="101.5", channel_band = "LSB")
session.add(new_station)
session.commit()

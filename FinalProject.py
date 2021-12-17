1#!/usr/bin/env python3
# Name: Siddhu Tedla
# Date: May 3rd, 2021
# Project: Final Project

import re

class Employee():
  def __init__(self, first = None, last = None, id_ = None, department = None, jobt = None):
      self.FIRST = first
      self.LAST = last
      self.ID = id_
      self.DEPARTMENT = department
      self.JOBT = jobt
  
  @property
  def First(self):
      return self.FIRST
  
  @First.setter
  def First(self, first) : #this is the setter for the firstname
    if first.isalpha(): #this checks that only alphabetical characters are in the string
      self.FIRST = first
    else:
      self.FIRST = False
  
  @First.deleter
  def First(self):
    del self.FIRST
      
  @property   
  def Last(self):
    return self.LAST       

  @Last.setter
  def Last(self, last) :#this is the setter for the lastname
    if last.isalpha():#this checks that only alphabetical characters are in the string
      self.LAST = last#string printed if only alphabetical characters
    else:
      self.LAST = False#string printed if non alphabetical characters
  
  @Last.deleter
  def Last(self):
    del self.LAST
      
  @property
  def id(self):
    return self.ID
  
  @id.setter  
  def id(self, id_) : #this is the setter for the middle initial
    regex = re.compile("^\d{5}$") 
    match = bool(regex.match(id_))
    if match == True:#This checks the string to make sure it is alphabetical and also only 1 character long
      self.ID = id_#this prints the middle initial if it is alphabetical and one character long
    else:
      self.ID = False
  
  @id.deleter
  def id(self):
    del self.ID
    
  @property
  def Department(self):
      return self.DEPARTMENT
  
  @Department.setter
  def Department(self, department) : #this is the setter for the firstname
    if department.isalpha(): #this checks that only alphabetical characters are in the string
      self.DEPARTMENT = department#string printed if only alphabetical characters
    else:
      self.DEPARTMENT = False

  @Department.deleter
  def Department(self):
    del self.DEPARTMENT
  
  
  @property
  def JobT(self):
      return self.JOBT
  
  @JobT.setter
  def JobT(self, jobt) : #this is the setter for the firstname
    if jobt.isalpha(): #this checks that only alphabetical characters are in the string
      self.JOBT = jobt #string printed if only alphabetical characters
    else:
      self.JOBT = False
  
  @JobT.deleter
  def JobT(self):
    del self.JOBT
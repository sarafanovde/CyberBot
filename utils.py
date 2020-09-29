#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import datetime


help_text = "Выбери один из интересующих тебя разделов:"
start_text = "Прежде чем приступить к расследованию, у тебя есть возможность проверить свои знания"
code_word = "1234"
alphabet = "авекмнорстухАВЕКМНОРСТУХ"




class simpleSession(object):
	"""docstring for simpleSession"""
	def __init__(self, id):
		self.points = 0
		self.start_wait = False
		self.name = ""
		self.id = id
		self.time = datetime.datetime.now().day
		self.first_test = True
		self.question_number = 0
		self.points_1 = []
		for i in range(8):
			self.points_1.append(0)
sessions = {}

time = []

def search(name, cel):
	s = 0
	temp = name
	temp = temp.lower()
	temp = temp.split(' ')
	#print(temp)
	n = cel.lower()
	n = n.split(' ')
	for k in n:
		for j in temp:
			if (k == j):
				s+=1
	if (s>=1):
		return True 
	else:
		return False

#getDashboard('тюшняков','22')



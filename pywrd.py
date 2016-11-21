#!/usr/bin/env python
from random import choice
from Crypto.Hash import SHA256
from Crypto.Hash import MD5

print ""
print "\033[1mPYWRD 0.00.1 SCATHACH"
print ""
print "\033[4mW3b: https://mkdirscathach.wordpress.com/"
print ""
print "\033[0m1. Easy password"
print "2. Medium password"
print "3. Hard password"

n = raw_input("Select mode (select number):") #number
m = "" #mode
e = "123456789" #easy
me = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #Medium
h = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&/()=" #Hard

if n == "1":
	print "You selected \033[92mEASY MODE\033[0m"
	m = e
	l = input("Select range: ")

if n == "2":
	print "You selected \033[94mMEDIUM MODE\033[0m"
	m = me
	l = input("Select range: ")

if n == "3":
	print "You selected \033[93mHARD MODE\033[0m"
	m = h
	l = input("Select range: ")

if n < "1":
	print "Select 1, 2 or 3"
	exit()
if n > "3":
	print "Select 1, 2 or 3"
	exit()

p = ""
p = p.join([choice(m) for i in range(l)])
print(p)
print ""

c = raw_input("\033[4mCrypt password? y/n:\033[0m ")

if c == "y":
	print ""
	print "\033[0mSelect mode"
	print ""
	print "1. SHA256"
	print "2. MD5"
	print ""
	n = raw_input("Select mode (select number): ")

	if n == "1":
		hp = SHA256.new()
		hp.update(p)
		print "\033[1m SHA256 >>>>>>>\033[92m " + hp.hexdigest()

	if n == "2":
		hp = MD5.new()
		hp.update(p)
		print "\033[1mMD5: >>>>>>\033[92m " + hp.hexdigest()

if c != "y":
	print "\033[0mSee ya!"
	exit()

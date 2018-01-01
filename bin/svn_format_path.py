#!/usr/bin/python

import sys
import os
import linecache
import re
import shutil

#arg1: r_start
#arg2: r_end
#arg3: target_folder


#check arg

r_start = 0
r_end = 0
target_folder = ""
abs_tmp_file = os.path.abspath("revision_list.willtmp")
special_char =['~','!','@','#','%','^','&','*','(',')','-','+','=','[',']','{','}',':',';',',','<','.','>','/','?','|','\\','`',' ', '\n']

def print_help():
	print "usage: svn_format_path.py [start rev] [end rev] [patch folder]"


def create_revlist(r_start, r_end):
#svn log -r 12108:16081 | grep 'r[0-9]* |.* |.* |.* lines'
	cmd= "svn log -r {0}:{1} | grep 'r[0-9]* |.* |.* |.* lines' > {2}".format(r_start, r_end, abs_tmp_file)
	#print "do '" + cmd + "'"
	os.system(cmd)

def gen_format_patch(out):
	with open(abs_tmp_file) as f:
		content = f.readlines()

	while not os.path.exists(".svn"):
		os.chdir("..")

	for i in range(0, len(content), 1):
		tokens = content[i].split("|")
		rev = tokens[0].rsplit()
		author = tokens[1].split()
		#print "svn log --diff -c {0} > patch.willtmp".format(rev[0])
		os.system("svn log --incremental --diff -c {0} > patch.willtmp".format(rev[0]))
		linecache.clearcache()
		msg = linecache.getline("patch.willtmp", 4)
		msg=msg[:48].split()
		msg=' '.join(msg)
		for c in special_char:
			msg=msg.replace(c, "_")
		format_num = '{:04d}'.format(i)
		patch_name = rev[0] + "_" + author[0] + "-" + msg + ".patch"
		shutil.move("patch.willtmp", os.path.join(out, patch_name))
		print patch_name

if len(sys.argv) != 4:
	print_help()
	exit()

if not sys.argv[1].isdigit() or not sys.argv[2].isdigit() or not os.path.isdir(sys.argv[3]):
	print_help()
	exit()

#create list
create_revlist(sys.argv[1], sys.argv[2])

#2 create patch folder
out_folder = os.path.join(sys.argv[3], "format_svn_patch")
if not os.path.isdir(out_folder):
	os.mkdir(out_folder)

#3 gen format patch
gen_format_patch(os.path.abspath(out_folder))

os.remove(abs_tmp_file)
print "Finish"






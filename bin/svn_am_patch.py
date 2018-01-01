#!/usr/bin/python

import sys
import os
import linecache
import re
import shutil

#arg1: r_start
#arg2: r_end
#arg3: target_folder

msg_file="svn_ci_msg.willtmp"
diff_file="svn_ci_diff.willtmp"


def split_msg_diff(patch_file):
	with open(patch_file) as f:
		lines = f.readlines()

	index_line = 0
	for i in range(0, len(lines), 1):
		line=lines[i]
		if (len(line) < len("Index:")):
			continue

		if( line[:6] == "Index:" ):
			index_line = i
			break

	fmsg = open(msg_file, 'w')
	fmsg.write ("Merge branch from BSP main line\n\n")
	fdiff = open(diff_file, 'w')
	for i in range(1, len(lines), 1):
		if i < index_line:
			fmsg.write(lines[i])
		else:
			fdiff.write(lines[i])

	fmsg.close()
	fdiff.close()


split_msg_diff(sys.argv[1])

#check arg
#
#r_start = 0
#r_end = 0
#target_folder = ""
#tmp_file = "revision_list.willtmp"
#csv_file = "patch_list.csv"
#special_char =['~','!','@','#','%','^','&','*','(',')','-','+','=','[',']','{','}',':',';',',','<','.','>','/','?','|','\\','`',' ', '\n']
#
#def print_help():
#	print "usage: svn_format_path.py [start rev] [end rev] [patch folder]"
#
#
#def create_revlist(r_start, r_end):
##svn log -r 12108:16081 | grep 'r[0-9]* |.* |.* |.* lines'
#	cmd= "svn log -r {0}:{1} | grep 'r[0-9]* |.* |.* |.* lines' > {2}".format(r_start, r_end, tmp_file)
#	#print "do '" + cmd + "'"
#	os.system(cmd)
#
#def gen_format_patch(out):
#	with open(tmp_file) as f:
#		content = f.readlines()
#
#	csv = open(os.path.join(out, csv_file), 'w')
#	csv.write("Revision,Author,Log Message\n")
#
#	for i in range(0, len(content), 1):
#		tokens = content[i].split("|")
#		rev = tokens[0].rsplit()
#		author = tokens[1].split()
#		#print "svn log --diff -c {0} > patch.willtmp".format(rev[0])
#		os.system("svn log --incremental --diff -c {0} > patch.willtmp".format(rev[0]))
#		linecache.clearcache()
#		msg = linecache.getline("patch.willtmp", 4)
#		msg=msg[:48].split()
#		msg=' '.join(msg)
#		for c in special_char:
#			msg=msg.replace(c, "_")
#		format_num = '{:04d}'.format(i)
#		patch_name = rev[0] + "_" + author[0] + "-" + msg + ".patch"
#		shutil.move("patch.willtmp", os.path.join(out, patch_name))
#		csv.write(rev[0] + "," + author[0] + "," + msg + "\n")
#		print patch_name
#
#	csv.close()
#
#if len(sys.argv) != 4:
#	print_help()
#	exit()
#
#if not sys.argv[1].isdigit() or not sys.argv[2].isdigit() or not os.path.isdir(sys.argv[3]):
#	print_help()
#	exit()
#
##create list
#create_revlist(sys.argv[1], sys.argv[2])
#
##2 create patch folder
#out_folder = os.path.join(sys.argv[3], "format_svn_patch")
#if not os.path.isdir(out_folder):
#	os.mkdir(out_folder)
#
##3 gen format patch
#gen_format_patch(out_folder)
#
#os.remove(tmp_file)
print "Finish"






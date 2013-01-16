#!/usr/bin/python
import sys,os

if len(sys.argv) < 2: 
  raise StandardError, "Syntax: invert_mtx.py filename"

ogfp=open(sys.argv[1],'r');
coorlist=[];
x_len=0;
y_len=0;
while True: 
	line=ogfp.readline().strip();
	if len(line) == 0:
		break;
	coorlist.append(line.split());
	if y_len==0: y_len=len(coorlist[0]);
	x_len=x_len+1;
	#print >> fpdr, line;
ogfp.close();

#print x_len, y_len;
tgfp=open(sys.argv[1]+".tmp",'w');

for j in range(y_len):
	for i in range(x_len):
		print >> tgfp, coorlist[i][j],
	print >> tgfp, "";
tgfp.close();

os.rename(sys.argv[1],sys.argv[1]+".bak");
os.rename(sys.argv[1]+".tmp",sys.argv[1]);




#!/usr/bin/python
import sys,os

ogfile="draw.gpl";
drawfile="drawprice.gpl";
pricefile="prices.dat";
fpog=open(ogfile,'r');
fpdr=open(drawfile, 'w');

linelist=[];
while True: 
	line=fpog.readline();
	if len(line) == 0:
		break;
	line=line.rstrip();
	linelist.append(line);
	#print >> fpdr, line;
fpog.close();

fppc=open(pricefile, 'r')
tagline=fppc.readline();
fppc.close();

itemlist=tagline.strip().split();
templen=len(itemlist);
index_pre=0;
index_i=0;
index_j=0;
index_len=len(itemlist[0]);
for i in range(index_len):
	if itemlist[0][i]=="(": index_i=i+1;
	if itemlist[0][i]==")": index_j=i;
unit_f=itemlist[0][index_i:index_j];
#print unit_f;

if templen<=1:
	print " error, no enough dat in: [", pricefile,"], please check it again...";
	fpdr.close();
	exit -1;

for i in range(len(linelist)):
	if len(linelist[i].strip())!=0 and linelist[i].strip()[0]!="#":  
		if linelist[i].strip() == "scale_width=0.8": 
			print >> fpdr, "scale_width=",3.2/float(templen);
		elif linelist[i].strip()=="dollar(i)='$'.sprintf(\"%d\",i)" and index_i!=0: 
			print >> fpdr, "dollar(i)='"+unit_f+"'.sprintf(\"%d\",i)";
		elif linelist[i].strip() == "reset": 
			print >> fpdr, "set out '"+itemlist[0][1:len(itemlist[0])]+".eps'";
		elif linelist[i].strip() == "set multiplot": 
			print >> fpdr, "set ylabel '"+itemlist[0][1:len(itemlist[0])]+"'";
		else: 
			print >> fpdr, linelist[i];

colorlist=["#2F4F4F","#68228B","#8B1A1A","#000000","#003366","#333300","#663366","#FF6666","#003399","#666666"];
incr=10000;
shift=1.0/float(templen);
#print shift;
flag=False;
print >> fpdr, "plot",
for i in range(templen):
	if i!=templen-1:
		if i == (templen-1)/2 and flag == False:
			print >> fpdr, "dtflname u "+str(i+2)+":xticlabels(1) t \""+itemlist[i+1]+"\" lc rgb \""+colorlist[i]+"\", '' using ($0+"+str(shift*(float(i+0.5)-float(templen-1)/2.0))+"):($"+str(i+2)+"):(($"+str(i+2)+")) with labels notitle font ftszstring rotate by",75,#-15-templen*5,
			flag=True;
		else: print >> fpdr, "dtflname u",i+2,"t \""+itemlist[i+1]+"\" lc rgb \""+colorlist[i]+"\", '' using ($0+"+str(shift*(float(i+0.5)-float(templen-1)/2.0))+"):($"+str(i+2)+"):(($"+str(i+2)+")) with labels notitle font ftszstring rotate by",75,#-15-templen*5,
	if i<templen-2:
		print >> fpdr, ",\\";
print >> fpdr, "";
print >> fpdr, "unset multiplot";
fpdr.close();

os.system("gnuplot < drawprice.gpl");





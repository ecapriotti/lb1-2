#!/usr/bin/env python
import sys


def read_aln(filename):
	d={}
	f=open(filename)
	c=0
	for line in f:
		c+=1
		v=line.rstrip().split()
		k=v[0]
		aln=v[1]
		d[k]=d.get(k,'')
		d[k]+=aln
	return d


def get_ids(col_aln):
	ids=False
	s=set(col_aln)
	if (len(s)==1): ids=True
	return ids


def get_spc(col_aln):
	spc=0
	n=len(col_aln)
	for i in range(n):
		for j in range(i+1,n):
			if col_aln[i]==col_aln[j] and col_aln[i]!='-': spc+=1
	return spc


def get_tc_sp(d_aln):
	tc=0
	sp=0
	list_aln=d_aln.values()
	n=len(list_aln[0])
	m=len(list_aln)
	for i in range(n):
		col_aln=[]
		for j in range(m): 
			col_aln.append(list_aln[j][i])
		#col_aln=[s[i] for s in list_aln]
		ids=get_ids(col_aln)
		sp=sp+get_spc(col_aln)
		if ids: tc+=1
	return tc,sp,n



if __name__ == "__main__":
	filename=sys.argv[1]
	d=read_aln(filename)
	tc,sp,n=get_tc_sp(d)
	print 'Conserved Residues:',tc
	print 'Identical Substitutions:',sp
	print 'Alignment length:',n

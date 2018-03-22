#!/usr/bin/python
import sys
from Bio.SVDSuperimposer import SVDSuperimposer
import numpy as np


def get_atoms(pdbfile,chain,res=[],atom='CA'):
	vres=[]
	fh=open(pdbfile,'r')
	for line in fh:
		if line[0:4]!='ATOM': continue
		at=line[12:16].strip()
		pos=int(line[22:26].strip())
		ch=line[21]
		if (len(res)>0 and (pos not in res) ): continue
		if (line[16]!='A' and line[16]!=' '): continue
		if (at==atom and ch==chain):
				coord=[ float(line[31:38].strip()),\
					float(line[39:46].strip()), \
					float(line[47:54].strip()) ]
				vres.append(coord)
	return vres

			
def super_pdb(coords1,coords2):
	if len(coords1)!=len(coords2):
		print >> sys.stderr,'ERROR: Structures with different length'
		sys.exit(1)
	svd=SVDSuperimposer()
	svd.set(np.array(coords1),np.array(coords2))
	svd.run()
	rot,tran=svd.get_rotran()
	rmsd=svd.get_rms()
	return rmsd


def get_range(rset):
	vset=[]
	lim=rset.split('-')
	if len(lim)==2: vset=range(int(lim[0]),int(lim[1])+1)
	return vset


if __name__ == '__main__':
	if len(sys.argv)>6:
		pdb1=sys.argv[1]
		pdb2=sys.argv[2]
		ch1=sys.argv[3]
		ch2=sys.argv[4]
		set1=sys.argv[5]
		set2=sys.argv[6]
		vset1=get_range(set1)
		vset2=get_range(set2)
		vres1=get_atoms(pdb1,ch1,vset1)
		vres2=get_atoms(pdb2,ch2,vset2)
		print super_pdb(vres1,vres2)
	else:
		print 'Program syntax:\npython',sys.argv[0],\
			'pdb1 pdb2 chain1 chain2 set1 set2'

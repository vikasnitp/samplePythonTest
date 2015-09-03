def FS(lim):
	n1=1
	n2=1
	if lim == 1:
		return [n1]
	elif lim == 2:
		return [n1,n2]
	else:
		flist=[1,1]
		for i in range(2, lim):
			n3=n1+n2
			flist.append(n3)
			n1=n2
			n2=n3
		return flist
	







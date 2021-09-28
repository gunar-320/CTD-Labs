n=int(input())
for i in range(n):
	z=int(input("Enter Secondary Load "))
	vs = float(input("Enter Value of Source Voltage "))
	iS = float(input("Enter Value of Source Input "))
	vp = float(input("Enter value of Primary Voltage "))
	ip = float(input("Enter value of Primary Current "))
	ps = vs*iS/1000
	pp = vp*ip/1000
	vl = float(input("Enter Load Voltage "))
	il = float(input("Enter Load Current "))
	pl = vl*il/1000
	et = (pl/pp)*100
	ep = (pl/ps)*100
	print("Power of source is ",ps)
	print("Power of Primary is ",pp)
	print("Power of Load is ",pl)
	print("Efficiency of Transformer is ",et)
	print("Efficiency of Power Source is ",ep)
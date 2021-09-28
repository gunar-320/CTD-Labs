n=int(input("Enter Number of Observations "))
for i in range(n):
	r=int(input("Enter Secondary Load Value "))
	vs = float(input("Enter Value of Input Voltage "))
	iS=float(input("Enter Value of Input Current "))
	vl = float(input("Enter value of Output Voltage "))
	il = float(input("Enter Value of Output Current "))
	ps = (vs)*iS
	pl = vl*il
	print("Input Power Source is ",ps)
	print("Output Power Source is ",pl)
	eff = (pl/ps)*100
	print("Efficiency is ",eff)
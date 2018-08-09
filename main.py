import os

def beri_vpn(fajl = None):
	if fajl == None:
		fajl = os.getenv('APPDATA')+"\\Microsoft\\Network\\Connections\\Pbk\\rasphone.pbk"
	vpn = {}
	current_vpn = "[]"
	for line in open(fajl).read().splitlines():
		if not line:
			continue
		if "[" in line and "]" in line:
			vpn[line] = []
			current_vpn = line
		else:
			vpn[current_vpn].append(line)
	return vpn

def dodaj_vpn(name, lines):
	fajl = os.getenv('APPDATA')+"\\Microsoft\\Network\\Connections\\Pbk\\rasphone.pbk"
	with open(fajl, 'a') as f:
		f.write('\n'.join(["", name]+lines))

if __name__ == '__main__':
	moji_vpn = beri_vpn(os.getcwd()+"\\rasphone.pbk")
	win_vpn = beri_vpn()
	for key in moji_vpn:
		if key not in win_vpn:
			print key+" manjka! dodam ?"
			choice = raw_input('Da/Ne?')
			if choice.upper() in ["DA","YES","D","Y"]: 
				dodaj_vpn(key, moji_vpn[key])
				print "dodano."

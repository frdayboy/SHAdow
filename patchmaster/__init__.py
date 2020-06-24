#THIS FILE IS PART OF Project SHAdow
#patchmaster v0.0.6

exported_patches = []
current_stage = 0

class Patchset:
    def __init__(self, path, tag):
        self.path = path
        self.tag = tag
        with open(self.path, "rb") as f:
            self.bin = f.read()
        f.close()

    def log(self, message):
        print(self.tag + message)

def initialize_all_patches(sn):
    exported_patches.append(Patchset("patchmaster/bin/SHAtter-shellcode.bin", "[Stage1] "))
    if "CPID:8930" in sn:
    	if "BDID:08" in sn:
		exported_patches.append(Patchset("patchmaster/bin/LLB.n81ap.PATCHED.RELEASE.img3", "[Stage2] "))
	elif "BDID:02" in sn:
		pass
	elif "BDID:0" in sn:
		pass
	elif "BDID:04" in sn:
		pass
	elif "BDID:06" in sn:
		pass
	elif "BDID:10" in sn:
		pass    
    else:
        print("[SHAdow] Device is not compatible.")
        sys.exit(1)

#THIS FILE IS PART OF Project SHAdow
import sys

exported_patches = []
current_stage = 0

class Patchset:

    def log(self, message):
        print(self.tag + message)

    def __init__(self, path, tag):
        self.path = path
        self.tag = tag
        try:
            with open(self.path, "rb") as f:
                self.bin = f.read()
        except FileNotFoundError:
            print("[SHAdow] Make sure to read the setup section of the README!")
            sys.exit(1)
        self.log("Length : {}".format(len(self.bin)))
        f.close()

def initialize_all_patches(sn):
    exported_patches.append(Patchset("patchmaster/bin/SHAtter-shellcode.bin", "[Stage1] "))
    exported_patches.append(Patchset("patchmaster/bin/LLB.PATCHED.img3", "[Stage2] "))
    if "CPID:8930" in sn:
        exported_patches.append(Patchset("patchmaster/bin/LLB-shellcode.bin", "[iBoot Patches] "))
    else:
        print("[SHAdow] Device is not compatible.")
        sys.exit(1)

# Project SHAdow

****Logo Soon****

****How to:****

  Due to DMCA concerns and shid, I can't include Apple code in the project, so you'll need to do some stuff on your part.
  1. Download your IPSW file from https://ipsw.me
  2. Extract the LLB bootloader from Firware/all_flash/all_flash.(device).production/LLB.(device).RELEASE.img3
  3. Head over to https://www.theiphonewiki.com/wiki/Firmware_Keys and find your iOS version/build for your device, and scroll to the LLB keys section
  4. Download and compile xpwntool-lite from https://github.com/sektioneins/xpwntool-lite
  5. Use it to decrypt LLB with the key and IV found in The iPhone Wiki
  6. Download and compile iBoot32Patcher from https://github.com/iH8sn0w/iBoot32Patcher
  6. Pass the decrypted LLB and specify a path to the patched LLB
  7. run SHAdow -p (path to patched LLB from step 6)
  8. Jailbreak with SHAdow -j!


****The goal:****

  The goal of Project SHAdow is to help beginners like myself gain experience with jailbreaking and the exploitation of vulnerabilities. Jailbreaking can be frustrating to start, but I hope to mirror an actual, maintainable jailbreak that you can dive into, poke around, and give you a feel for this stuff.

****The exploit:****

  Based on SHAtter exploit (segment overflow) by posixninja and pod2g
  A very good presentation for understanding the underlying bug is here:

  http://conference.hitb.org/hitbsecconf2013kul/materials/D2T1%20-%20Joshua%20%27p0sixninja%27%20Hill%20-%20SHAttered%20Dreams.pdf

****My device:****

  The end goal is to make a complete jailbreak for all A4 devices, but my only A4 device is an iPod 4g, so that's what I'm starting with. First tests were done on iOS 6.1.6

****Resources:****

  For patches:
    https://www.theiphonewiki.com/wiki/Vm_map_protect_Patch
    https://www.theiphonewiki.com/wiki/AMFI_Binary_Trust_Cache_Patch
    https://www.theiphonewiki.com/wiki/Sandbox_Patch
    https://www.theiphonewiki.com/wiki/PE_i_can_has_debugger_Patch
    https://www.theiphonewiki.com/wiki/Vm_map_enter_Patch
    https://www.theiphonewiki.com/wiki/Signature_Check_Patch

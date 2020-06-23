-The Plan:

We will first patch patch LLB once the device is pwned in pwned DFU mode. The patch will be at it's boot trampoline to instead
jump to another patchset, which will in turn patch iBoot since it is loaded in memory. iBoot's trampoline will also
be patched to jump to a final patchset that will patch the kernel and do some hax magic to allow a jailbreak.

-Baby Steps:

This is all very complex, so I will instead try to write to the framebuffer while iBoot is attempting to boot.
My assembly skills are not that great, so mastering the manipulation of bootloader memory space and all that with my assembly skillset, will definitely prepare me for the jailbreak.

Log:
5/8/20

I'm still unsure of my method of delivering the patches, do I upload it all as one combined binary and just jump to that from ROM and follow my planned patch routine, or upload them separately? Can I upload all the patches at once, or do I not have enough RAM? If I upload separately, should I try to accept data over usb from each stage, then have that loaded in memory, then patch the current stage? Or should I try to store the patches in NOR?

I also just realized that I'll have to find the function for a NOR boot (fsboot, I think).Once that finishes THEN the next stage will be loaded in RAM then I can patch.

5/9/20

I found most function addresses in the BootROM. Still looking for malloc.

5/22/20

I'm taking a step back and looking at the whole picture. Maybe I can just use axi0mx's ipwndfu SHAtter exploit to send a patched LLB, which will do some magic. Not sure how I'm going from there. Some options are to have it load iBoot from NOR, send it back to the host for patches, and sent back to boot, or send a completely new and patched iBoot by entering LLB dfu, or just having LLB do patches on loaded iBoot. To ensure the first part works, I might just send a normal LLB and just see if the device even boots. Fingers crossed.

Part2:
IT BOOTS!! I sent an unpatched LLB, and I had my doubts for whatever reason, but it does boot!

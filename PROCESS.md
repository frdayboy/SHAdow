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


5/23/20

I've just realised it might be a bit cumbersome in the final jailbreak to need to send an LLB based on the matching iOS version and device. Dynamic patching or sending the alreaded loaded firmware in NOR
to the host for patching there, and sending back.

5/26/20

It would be so cool to have patches done on the device. I'm not sure how
I'd do it though. My shellcode would have to somehow invoke the boot sequence,
then do patches on the next stage. Keeping the patches at a good size and
preserving them across stages is something I could figure out, but what the
hard part is is actually starting the boot sequence. Instead of trying to rewrite
the branch target in ROM to patches, I can just do the sequence myself?
I'd find symbols for NOR, get the next stage, load it in memory, then do
patches, then jump. That sounds reasonable.

5/29/20

Might just invoke boot process from shellcode (boot from NOR). Then, before jump, accept image over USB from shellcode and execute. This would be an easier way to patch the next stage, then return to the shellcode and boot the next stage. Boom. Only thing that would be problematic is what LLB jumps to to patch iBoot. I was thinking jumping to shellcode uploaded from LLB DFU, but then I have to do more RE to continue boot. I think storing iBoot's patch shellcode in load address would be easy for LLB to jump to, but I'm not sure if that gets memset over when boot happens. If it doesn't,then my plan of action is as follows:
-RE ROM to find how boot sequence starts.
-Start boot sequence from shellcode, but patch LLB right before jump
-LLB will just be patched to jump to patch shellcode before iBoot is executed.
-iBoot will just patch kernel
Note: If the patches are small enough, I can just include them in the code section of the next stage. So patches for iBoot are with LLB.

5/30/30

RE might be harder than I thought. Maybe finding image3_load_signature_check type-function might help me in finding the beginning of the jump sequence.
Might just be better to stick to my original method of accepting an image over usb. This seems to be the method used by Greenpois0n as found in SHAttered dreams.

6/3/20

Now it's time to RE LLB, I have to look for a function that loads iBoot then patch the end of it to a custom function that patches iBoot.

6/5/20

Had some USB issues during the exploit. Not sure why, but adding time delays between
ctrl_transfers seems to fix it.

iPod is not booting when sending patched and unpatched LLB on 6.1.6.

I was unable to get my iPod to 6.1.6 which is sad because it's currently on 4.1.
I'm going to redo my reverse engineering for 4.1 LLB, patch it, and hope for the
boot. I'll keep my research on 6.1.6 and support that however because it's
better to have the latest signed firmware and support all A4 devices.

6/10/20

I just realized that the reason the 6.1.6 patched LLB is not booting is probably because it's not encrypted. Also turns out that 6.1.6 is the only LLB that will boot, so I'm not gonna redo RE for 4.1.

6/15/20

I'm making a tool that allows to overwrite the DATA tag in an IMG3 firmware file.
This will allow the shellcode code to properly load the unsigned code and jump to it.

6/21/20

I'm preparing for my initial barebones release, which is enabling verbose boot. I have reverse engineered iBoot (4.1, easier to find symbols). My plan is to patch the standard boot args string with "-v" and BOOM! verbose mode.

6/25/20

I'm doing some digging in the iBoot32Patcher source to see how they patched the kernel's command line. The iBoot patchset that will be added to the patched LLB will just do what iBoot32Patcher -b does.

Looks like the desired boot args are just strcpy-ed over the hardcoded boot args string. I can achieve the same effect by either putting my RE skills to the test on LLB and finding strcpy, or implementing it myself in shellcode that gets added to the patched LLB.

6/29/20

I've just realized it may be easier to patch iBSS and iBoot to achieve verbose (and a jb) rather than patching LLB and patching iBoot from LLB. All my work on LLB may be to waste, but this is a learning process.

I might be able to also achieve verbose boot with just a simple environment variable from LLB.

I GOT VERBOSE BOOT! It was super cool! Now I just have to work on making the process super easy for the user

all: armv7

armv7:
	arm-none-eabi-as -mthumb --fatal-warnings -o ./bin/SHAtter-shellcode.o ./src/SHAtter-shellcode.S
	arm-none-eabi-objcopy -O binary ./bin/SHAtter-shellcode.o ./bin/SHAtter-shellcode.bin
	rm ./bin/SHAtter-shellcode.o

# example script to lock PLL to freq

import pll
import time 
import argparse

p = pll.PLL()

p.set_LED_mode(pll.LED_MODE_LOCK_DETECT)

p.power_on()
p.enable_output()


def main():
	parser = argparse.ArgumentParser(description="Set up PLL at freq in MHz (multiple of 10MHz)")
	parser.add_argument("--freq", required=True, type=int, help="Frequency (multiple of 10MHz)")

	args = parser.parse_args()
	freq = args.freq
	print(f"Frequency {freq}MHz")

	assert freq%10==0, "Frequency should be a muliple of 10MHz"

	p.frequency(freq)
	
	print("locking")
	while not p.locked():
		print(".", endl="")
		time.sleep(0.5)
	
	print("\nLocked")

if __name__ == "__main__":
    main()

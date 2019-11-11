#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program shows all rgb colour combinations


def main():
    # This function Calculates all RGB combinations
    red = 0
    blue = 0
    green = 0

    # process and output
    for red in range(254, 256):
        for green in range(0, 256):
            for blue in range(0, 256):
                print("RGB value is: {0}, {1}, {2}".format(red, green,
                                                           blue))


if __name__ == "__main__":
    main()

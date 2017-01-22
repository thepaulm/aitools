#!/usr/bin/env python

import sys
import os
import shutil
import glob
import random
import argparse


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('-vs', '--valid_size', help="how many images per category to validate with",
                    type=int)
    ap.add_argument('-s', '--source', help="path to source directory "
                    "(where the categories live)")
    ap.add_argument('-T', '--test', help="copy the files, don't move them. This is for [T]esting",
                    action="store_true")
    args = ap.parse_args()
    if not args.valid_size or not args.source:
        print("Need all parameters (-h for help)")
        sys.exit(-1)
    return args


def main():
    args = parse_args()
    valid = args.valid_size
    source = args.source
    target = source + '/../'

    os.mkdir(target + "/valid")

    it = os.scandir(source)
    for d in it:
        g = glob.glob(source + "/" + d.name + "/*.jpg")
        files = random.sample(g, valid)
        category = target + "/valid/" + d.name
        os.mkdir(category)
        for f in files:
            print("%s -> %s" % (f, category))
            if args.test:
                shutil.copy(f, category)
            else:
                shutil.move(f, category)

    print("valid: %d\n" % valid)


if __name__ == '__main__':
    main()

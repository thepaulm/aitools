#!/usr/bin/env python

import sys
import os
import shutil
import glob
import random
import argparse


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('-ts', '--train_size', help="how many images per category to train with",
                    type=int)
    ap.add_argument('-vs', '--valid_size', help="how many images per category to validate with",
                    type=int)
    ap.add_argument('-s', '--source', help="path to source directory "
                    "(where the categories live)")
    ap.add_argument('-t', '--target', help="path to target directory "
                    "(where the categories will be created)")
    args = ap.parse_args()
    if not args.train_size or not args.valid_size or not args.source or not args.target:
        print("Need all parameters (-h for help)")
        sys.exit(-1)
    return args


def main():
    args = parse_args()
    train = args.train_size
    valid = args.valid_size
    source = args.source
    target = args.target

    shutil.rmtree(target, ignore_errors=True)
    os.mkdir(target)
    os.mkdir(target + "/train")
    os.mkdir(target + "/valid")

    for what in ['train', 'valid']:
        it = os.scandir(source)
        for d in it:
            g = glob.glob(source + d.name + "/*.jpg")
            if what == "train":
                count = train
            elif what == "valid":
                count = valid
            files = random.sample(g, count)
            category = target + "/" + what + "/" + d.name
            os.mkdir(category)
            for f in files:
                shutil.copy(f, category)

    print("train: %d, valid: %d\n" % (train, valid))


if __name__ == '__main__':
    main()

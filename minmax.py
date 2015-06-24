#!/usr/bin/env python

import sys


def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    try:
        f = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid filename"
        usage()
        sys.exit(1)
    maxim = 0
    minim = 11
    for idx, line in enumerate(list(f)):
        tokens = line.split('\t')
        grade = int(tokens[3])
        if grade > maxim:
            maxim = grade
            nameMax = tokens[0]
            surnameMax = tokens[1]
        if grade < minim:
            minim = grade
            nameMin = tokens[0]
            surnameMin = tokens[1]

    print "Name: %s\tSurname: %s\tMaxGrade: %d" % (nameMax, surnameMax, maxim)
    print "Name: %s\tSurname: %s\tMinGrade: %d" % (nameMin, surnameMin, minim)

if __name__ == "__main__":
    sys.exit(main())

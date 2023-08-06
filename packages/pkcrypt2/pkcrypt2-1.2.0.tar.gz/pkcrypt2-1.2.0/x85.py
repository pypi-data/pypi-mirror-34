#!/usr/bin/env python
#
# This is the MIT License
# http://www.opensource.org/licenses/mit-license.php
#
# Copyright (c) 2008 Nick Galbreath
# Copyright (c) 2017 Joel Ward
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

"""
 x85 is a new format suitable for use in filenames, urls, and YAML fields
"""
# Original b85 at https://github.com/client9/stringencoders/blob/master/python/b85.py
# modified to make output better for urls and filesystems - jward


gsIntToChar = [ '!',  '#',  '$',  '(',  ')',  '*',  '+',  '-',
                '0',  '1',  '2',  '3',  '4',  '5',  '6',  '7',  '8',  '9',
                ':',  ';',  '<',  '=',  '>',  '?',  '@',
                'A',  'B',  'C',  'D',  'E',  'F',  'G',  'H',  'I',  'J',
                'K',  'L',  'M',  'N',  'O',  'P',  'Q',  'R',  'S',  'T',
                'U',  'V',  'W',  'X',  'Y',  'Z',  '[',  ']',  '^',  '_',
                'a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',
                'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',
                'u',  'v',  'w',  'x',  'y',  'z',  '{',  '|',  '}',  '~' ]


# This was hardcoded, now generated on the fly - jward
gsCharToInt = [ 256 ] * 256
for n, v in enumerate(gsIntToChar):
    gsCharToInt[ord(v)] = n
    pass


from struct import unpack, pack
# covert 4 characters into 5
def x85_encode(s):
    parts = []
    numchunks = len(s) // 4
    format = '!' + str(numchunks) + 'I'
    for x in  unpack(format, s):
        # network order (big endian), 32-bit unsigned integer
        # note: x86 is little endian
        parts.append(gsIntToChar[x // 52200625])
        parts.append(gsIntToChar[(x // 614125) % 85])
        parts.append(gsIntToChar[(x // 7225) % 85])
        parts.append(gsIntToChar[(x // 85) % 85])
        parts.append(gsIntToChar[x % 85])
    return ''.join(parts)


# convert 5 characters to 4
def x85_decode(s):
    parts = []
    for i in xrange(0, len(s), 5):
        bsum = 0
        for j in xrange(0,5):
            bsum = 85*bsum + gsCharToInt[ord(s[i+j])]
        parts.append( pack('!I', bsum) )
    return ''.join(parts)


import unittest
class X85Test(unittest.TestCase):

    def testDecode1(self):
        s = x85_decode('!!!!#')
        self.assertEquals(4, len(s))
        self.assertEquals(0, ord(s[0]))
        self.assertEquals(0, ord(s[1]))
        self.assertEquals(0, ord(s[2]))
        self.assertEquals(1, ord(s[3]))

        e = x85_encode(s)
        self.assertEquals('!!!!#', e)


def run_timings():
    from time import clock

    N = 1000000
    s = '!!!!#' * 10

    t0 = clock()
    for i in xrange(N):
        x85_decode(s)
    t1 = clock()
    print "decode v1",  t1-t0

    t0 = clock()
    for i in xrange(N):
       x85_decode2(s)
    t1 = clock()
    print "decode v2",  t1-t0

    s = x85_decode('!!!!#' * 10)

    t0 = clock()
    for i in xrange(N):
       x85_encode(s)
    t1 = clock()
    print "encode v1",  t1-t0

    t0 = clock()
    for i in xrange(N):
        x85_encode2(s)
    t1 = clock()
    print "encode v2",  t1-t0

    return


def usage():
    print("""\
x85 - cool encoding/decoding format
 -e = encode stdin
 -d = decode stdin
 -t = run unittests
 -r = run timings
""")


def main():
    import sys
    if not sys.argv[1:]:
        usage()
    elif sys.argv[1] == '-d':
        msg = sys.stdin.read()
        while len(msg) % 4:
            msg = msg + '\0'
        print(x85_encode(msg))
    elif sys.argv[1] == '-e':
        msg = sys.stdin.read()
        print(x85_decode(msg.strip()))
    elif sys.argv[1] == '-t':
        unittest.main()
    elif sys.argv[1] == '-r':
        run_timings()
    else:
        return usage()


if __name__ == '__main__': main()

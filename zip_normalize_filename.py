# coding: utf-8

# normalize encoding of zip archive name 
#   1. filename is encoded to utf-8 (NFC)
#   2. global purpose flag 11 (Language encoding flag) is on

import zipfile
import unicodedata
import copy

def zip_normalize_filename(src, dst, srccodec='utf-8', verbose=False):
    z = zipfile.ZipFile(src, 'r')
    out = zipfile.ZipFile(dst, 'w')

    for i in z.infolist():
        # get byte data
        c = z.read(i)

        # make copy of Zipinfo
        newinfo = copy.deepcopy(i) # is deepcopy needed?

        # test EFS bit
        if newinfo.flag_bits & 0b100000000000:
            # original file is already encoded in utf-8
            pass
        else:
            # original file is loaded as cp473 codec
            # re-decode using srccodec
            newinfo.filename = newinfo.filename.encode('cp437').decode(srccodec)
            # put EFS flag
            newinfo.flag_bits |= 0b100000000000

        # normalize to nfc
        newinfo.filename = unicodedata.normalize('NFC', newinfo.filename)

        if verbose:
            print(newinfo.filename)

        # write
        out.writestr(newinfo, c)


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, help='input .zip filename')
    parser.add_argument('output', type=str, default=None,
                        nargs='?',
                        help='output .zip filename (default <input>-norm.zip)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        default=False, help='verbose mode')
    parser.add_argument('--srccodec', type=str, default='utf-8',
                        help='codec of input zip archives (default: %(default)s)',
                        metavar='codec')
    args = parser.parse_args()

    # when dst is omitted. add '-norm.zip' as new filename
    if args.output is None:
        args.output =  args.input + '-norm.zip'

    zip_normalize_filename(args.input, args.output,
                           srccodec=args.srccodec,
                           verbose=args.verbose)

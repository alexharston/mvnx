import numpy as np
from mvnx.models import MVNX
import argparse
import errno
import os
import warnings

def load(*args, **kwargs):
    return MVNX(*args, **kwargs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="the MVNX file to parse")
    parser.add_argument("-m", "--modality", help="the modality to parse")
    parser.add_argument("-o", "--output", help="filepath to save parsed data to (saves as .npy)")
    args = parser.parse_args()
    if (args.file == None and args.modality == None):
        parser.print_help()
    else:
        try:
            if args.file:
                print(f'{args.file} selected - writing MVNX to {args.output}')
                mvnx = MVNX(args.file)
                if args.modality:
                    modality = mvnx.parse_modality(args.modality)
                    np.save(args.output, modality) 
                elif args.output:
                    np.save(args.output, mvnx)
                else:
                    warnings.warn('No output location selected, printing to terminal instead')
            else:
                raise FileNotFoundError(
                    errno.ENOENT, os.strerror(errno.ENOENT), args.file)
        except Exception:
            print('Something went wrong!')

if __name__ == "__main__":
    main()
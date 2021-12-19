import numpy as np
from mvnx.models import MVNX
import argparse
import errno
import os
import warnings
import traceback

def load(*args, **kwargs):
    return MVNX(*args, **kwargs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="the MVNX file to parse")
    parser.add_argument("-m", "--modality", help="the modality to parse")
    parser.add_argument("-o", "--output", help="filepath to save parsed data to (saves as .npy)")
    parser.add_argument("-c", "--compress", help="Compress the saved object")
    args = parser.parse_args()
    if not args.output:
        args.output = f'{args.file.split(".")[0]}.npy'
    if (args.file == None and args.modality == None):
        parser.print_help()
    else:
        try:
            if args.file:
                print(f'Writing {args.file} to {args.output}')
                mvnx = MVNX(args.file)
                if args.modality:
                    modality = mvnx.parse_modality(args.modality)
                    if args.compress:
                        np.savez_compressed(args.output, modality) 
                    else:
                        np.save(args.output, modality)
                elif args.output:
                    if args.compress:
                        np.savez_compressed(args.output, mvnx)
                    else:
                        np.save(args.output, mvnx)
                else:
                    warnings.warn('No output location selected, printing to terminal instead')
            else:
                raise FileNotFoundError(
                    errno.ENOENT, os.strerror(errno.ENOENT), args.file)
        except Exception as e:
            traceback.print_exc()

if __name__ == "__main__":
    main()

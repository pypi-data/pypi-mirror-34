from sos.targets import file_target, path
import argparse
import multiprocessing
import time
import os
import glob

def write_signature(root, dirs, files):
    #print(f'processing {len(files)} under {root}')
    for file in files:
        file_target(os.path.abspath(os.path.join(root, file))).write_sig()
    return len(files)


def testWriteSignature(dir, njobs):
    pool = multiprocessing.Pool(njobs)
    res = pool.starmap_async(
            write_signature, os.walk(dir))
    return res.get()

def validate_signature(root, dirs, files):
    #print(f'processing {len(files)} under {root}')
    for file in files:
        if not file_target(os.path.abspath(os.path.join(root, file))).validate():
            raise ValueError(f'Failed to validate {os.path.abspath(os.path.join(root, file))}')
    return len(files)


def testValidateSignature(dir, njobs):
    pool = multiprocessing.Pool(njobs)
    res = pool.starmap_async(
            validate_signature, os.walk(dir))
    return res.get()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', help='directory to generate signature')
    parser.add_argument('-j', '--jobs', type=int, help='number of processes')
    args = parser.parse_args()

    sig_file = os.path.join(os.path.abspath(os.path.expanduser('~')), '.sos', 'target_signatures.db')
    if os.path.isfile(sig_file):
        os.remove(sig_file)
        
    st = time.time()
    res = testWriteSignature(args.dir, args.jobs)
    print(f'It took {args.jobs} processes {time.time() - st : .1f} seconds ({(time.time() - st)*10000/sum(res):.1f} per 10000 files) to process {sum(res)} files under {len(res)} directories')

    st = time.time()
    res = testValidateSignature(args.dir, args.jobs)
    print(f'It took {args.jobs} processes {time.time() - st : .1f} seconds ({(time.time() - st)*10000/sum(res):.1f} per 10000 files) to process {sum(res)} files under {len(res)} directories')

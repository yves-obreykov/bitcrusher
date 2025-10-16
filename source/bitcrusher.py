# bitcrusher program written by Yves

import soundfile as sf
import numpy as np
import argparse

def reduce_sample_rate(audio, factor=4):
    return np.repeat(audio[::factor, :], factor, 0)

def reduce_bit_depth(audio, bitdepth=8):
    factor = 2**(bitdepth-1)
    return np.round(audio*factor)/factor    # 1 multiply by factor, 2 round, 3 divide by factor 

# Define program arguments
parser = argparse.ArgumentParser(
        prog='BitCrusherYves',
        description='Simple bitcrusher',
        epilog='Send file, down sample fraction and desired bitrate to get a bitcrushed version of the audio')

parser.add_argument('filename', help='input file, stereo .wav file')
parser.add_argument('-ds', '--downsample', default=4,help='-s down sample fraction', type=int)
parser.add_argument('-bd', '--bitdepth',  default=8, help='-b desired bit depth', type=int)
parser.add_argument('-o', '--output', default='crushed_audio.wav', help='-o optional output file name')

# get arguments
args = parser.parse_args()
data, sr = sf.read(args.filename)
downsample = args.downsample
bitdepth = args.bitdepth
output_file = args.output

# do signal processing
crushed_data = reduce_sample_rate(data, downsample)
bit_crushed_data = reduce_bit_depth(crushed_data, bitdepth)

# save output file
sf.write(output_file, bit_crushed_data, sr)






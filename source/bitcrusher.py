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
        epilog='Input stereo .wav file, down sample by a factor and select desired bit depth to get a bitcrushed version of the audiofile')

parser.add_argument('filename', help='Input stereo .wav file')
parser.add_argument('-s', '--downsample', default=4, type=int,
                    help='Downsample factor (default: 4), Determines how much the sample rate is reduced ')
parser.add_argument('-b', '--bitdepth',  default=8, type=int,
                    help='Target bit depth (default: 8). Controls quantization precision.')
parser.add_argument('-o', '--output', default='crushed_audio.wav', type=str,
                    help='Output filename (default: crushed_audio.wav). Must end with .wav')

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






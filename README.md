# BitCrusher

BitCrusher is a simple audio processing tool written in Python.
It takes a stereo `.wav` file as input and generates a bit-crushed version of the audio.
The amount of downsampling and bit-depth reduction can be controlled using optional command-line arguments.

---

## Requirements

- Python 3.8 or higher
- Libraries: `numpy`, `soundfile`

Install dependencies (if needed):

```bash
pip install numpy soundfile
```

---

## Usage

Run the program with:

```bash
python3 bitcrusher.py input.wav [options]
```

### Positional argument
- **input.wav** — Path to a stereo `.wav` file.

### Optional arguments
| Flag | Type | Description | Default |
|------|------|--------------|----------|
| `-s`, `--downsample` | int | Downsample factor (e.g. 4 means the sample rate is divided by 4). | 4 |
| `-b`, `--bitdepth` | int | Target bit depth for quantization. | 8 |
| `-o`, `--output` | str | Output file name (must end with `.wav`). | `bitcrushed.wav` |
| `-h`, `--help` | — | Display help and exit. | — |

---

## Example

```bash
python3 bitcrusher.py piano.wav -s 24 -b 4 -o crushed.wav
```

This command reads `piano.wav`, reduces the sample rate by a factor of 24, quantizes the signal to 4-bit depth, and writes the result to `crushed.wav`.

---

## Notes

- Input must be a stereo `.wav` file.
- Output is written to the same directory unless otherwise specified.
- The bitcrusher preserves aliasing artifacts to emulate classic digital lo-fi sound.

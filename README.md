# WebP to PNG and PNG to SVG Converter

This Python script provides a command-line interface (CLI) to convert WebP images to PNG format and PNG images to SVG format using the `vtracer` library.

## Prerequisites

- Python 3.x
- `vtracer` library (`pip install vtracer`)
- `Pillow` library (`pip install Pillow`)

## Usage

```
python converter.py [--webp-to-png] [--png-to-svg] [--input-folder INPUT_FOLDER] [--output-folder OUTPUT_FOLDER]
```

### Options

- `--webp-to-png`: Convert WebP images to PNG format.
- `--png-to-svg`: Convert PNG images to SVG format.
- `--input-folder INPUT_FOLDER`: Specify the input folder path containing the WebP or PNG images (default: `./webp`).
- `--output-folder OUTPUT_FOLDER`: Specify the output folder path where the converted PNG or SVG files will be saved (default: `./png` for PNG, `./svg` for SVG).

### Examples

1. Convert WebP images to PNG format:

```
python converter.py --webp-to-png
```

This command will convert all WebP images in the `./webp` folder to PNG format and save them in the `./png` folder.

2. Convert PNG images to SVG format:

```
python converter.py --png-to-svg
```

This command will convert all PNG images in the `./png` folder to SVG format and save them in the `./svg` folder.

3. Convert WebP images to PNG format with custom input and output folders:

```
python converter.py --webp-to-png --input-folder /path/to/input --output-folder /path/to/output
```

This command will convert all WebP images in the `/path/to/input` folder to PNG format and save them in the `/path/to/output` folder.

4. Convert both WebP to PNG and PNG to SVG:

```
python converter.py --webp-to-png --png-to-svg
```

This command will first convert all WebP images in the `./webp` folder to PNG format and save them in the `./png` folder, then convert all PNG images in the `./png` folder to SVG format and save them in the `./svg` folder.

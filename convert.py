import argparse
import vtracer
import os
from PIL import Image


def convert_webp_to_png(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is a .webp file
        if filename.endswith(".webp"):
            # Open the .webp file
            input_path = os.path.join(input_folder, filename)
            image = Image.open(input_path).convert("RGB")

            # Generate the output file name and path
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, output_filename)

            # Save the image as a .png file
            image.save(output_path, "PNG")
            print(f"Converted {filename} to {output_filename}")


def convert_png_to_svg(input_folder, output_folder):
    png_files = os.listdir(input_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for png_file in png_files:
        if png_file.endswith("png"):
            in_file = os.path.join(input_folder, png_file)
            out_file = os.path.join(
                output_folder, f"{os.path.splitext(png_file)[0]}.svg"
            )
            print(f"Converting {png_file} to {out_file}")
            try:
                vtracer.convert_image_to_svg_py(
                    in_file,
                    out_file,
                    colormode="binary",
                    hierarchical="stacked",
                    mode="spline",
                    filter_speckle=4,
                    color_precision=8,
                    layer_difference=16,
                    corner_threshold=60,
                    length_threshold=4.0,
                    max_iterations=10,
                    splice_threshold=45,
                    path_precision=3,
                )
            except Exception as e:
                print(f"Error converting {png_file}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert WebP images to PNG and PNG images to SVG"
    )
    parser.add_argument(
        "--webp-to-png", action="store_true", help="Convert WebP images to PNG"
    )
    parser.add_argument(
        "--png-to-svg", action="store_true", help="Convert PNG images to SVG"
    )
    parser.add_argument(
        "--input-folder", default="./webp", help="Input folder path (default: ./webp)"
    )
    parser.add_argument(
        "--output-folder", default="./png", help="Output folder path (default: ./png)"
    )
    args = parser.parse_args()

    if args.webp_to_png:
        convert_webp_to_png(args.input_folder, args.output_folder)

    if args.png_to_svg:
        convert_png_to_svg(args.output_folder, "./svg")


if __name__ == "__main__":
    main()

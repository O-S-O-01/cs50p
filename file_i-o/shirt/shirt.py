import sys
import os
from PIL import Image, ImageOps


def main():
    check_args()
    process_image()


def check_args():
    # check number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Invalid number of arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # get file extensions
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    allowed = [".jpg", ".jpeg", ".png"]

    # check valid extensions
    if input_ext not in allowed or output_ext not in allowed:
        sys.exit("Invalid input")

    # check matching extensions
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")


def process_image():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # open user image
        photo = Image.open(input_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")

    # open shirt overlay
    shirt = Image.open("shirt.png")

    # get shirt size
    size = shirt.size

    # resize and crop photo to match shirt
    photo = ImageOps.fit(photo, size)

    # paste shirt onto photo
    photo.paste(shirt, shirt)

    # save final image
    photo.save(output_file)


if __name__ == "__main__":
    main()
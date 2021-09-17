import numpy as np
import cv2
import sys
import argparse


def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array(
        [((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]
    ).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


def main(inputPath, outputPath, gamma,debug):
    try:
        original = cv2.imread(inputPath)
        gamma = gamma if gamma > 0 else 0.1
        adjusted = adjust_gamma(original, gamma=gamma)
        if debug:
            cv2.putText(adjusted, "g={}".format(gamma), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            cv2.imwrite(outputPath, np.hstack([original, adjusted]))
        else:
            cv2.imwrite(outputPath, adjusted)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gain Correction")
    parser.add_argument(
        "--input",
        dest="input_path",
        default="",
        type=str,
        help="Input image path, /path/to/image.jpg",
        required=True,
    )
    parser.add_argument(
        "--output",
        dest="output_path",
        default="",
        type=str,
        help="Output image path, /path/to/image.jpg",
        required=True,
    )
    parser.add_argument(
        "--gamma",
        dest="gamma",
        default=2.0,
        type=float,
        help="Gamma value to convert",
        required=False,
    )
    parser.add_argument(
        "--debug",
        dest="debug",
        default=False,
        type=bool,
        help="Will show you the difference",
        required=False,
    )
    args = parser.parse_args()
    main(args.input_path, args.output_path, args.gamma,args.debug)

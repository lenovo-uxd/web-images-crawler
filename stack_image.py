import os
import argparse
import numpy as np
import cv2
import os.path as osp
from math import ceil

def parse_args():
    parser = argparse.ArgumentParser(description='process json.')
    parser.add_argument('--input_image_fold', type=str,
                        default='all_images', help='input image fold')
    parser.add_argument('--save_fold', type=str,
                        default='stacked_images', help='save fold')
    parser.add_argument('--target_width', default=2048, type=int)
    parser.add_argument('--target_height', default=1024, type=int)

    args = parser.parse_args()
    return args

def process_images(src_fold='image', dst_fold='dst_image',
                   target_height=1024, target_width=2048):
    image_names = os.listdir(src_fold)
    for image_name in image_names:
        # skip not png files
        if not image_name.endswith('.png'):
            continue
        image_path = os.path.join(src_fold, image_name)
        img = cv2.imread(image_path, 1)
        stacked_image = get_stacked_image(img, (target_width, target_height))

        # save
        save_image_path = osp.join(dst_fold, image_name)
        cv2.imwrite(save_image_path, stacked_image)


def get_stacked_image(image, target_size):
    org_h, org_w, _ = image.shape
    target_h, target_w = target_size

    # stack numbers
    horisontal_num = ceil(target_w/org_w)
    vertical_num = ceil(target_h / org_h)

    # stack
    h_images = [image for i in range(horisontal_num)]
    image = np.hstack(h_images)
    v_images = [image for i in range(vertical_num)]
    image = np.vstack(v_images)

    # crop
    # x_start = int((org_w*horisontal_num - target_w)/2)
    # y_start = int((org_h*vertical_num - target_h)/2)
    x_start = 0
    y_start = 0
    image = image[y_start:target_h, x_start:target_w, :].copy()

    return image


if __name__=='__main__':
    args = parse_args()
    if not os.path.exists(args.save_fold):
        os.mkdir(args.save_fold)
    process_images(src_fold=args.input_image_fold,
                   dst_fold=args.save_fold,
                   target_width=args.target_height,
                   target_height=args.target_width)
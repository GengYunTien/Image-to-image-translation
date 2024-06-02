import os
from PIL import Image

org_root = '/staging/biology/u1307362/aicup/org_training_dataset'
aug_root = '/staging/biology/u1307362/aicup/aug_training_dataset'

for i in os.listdir(os.path.join(org_root, 'img')):
    img = Image.open(os.path.join(org_root, 'img', i))
    label_img = Image.open(os.path.join(org_root, 'label_img', i[:-4] + '.png'))

    # vertical flip
    img_v = img.transpose(Image.FLIP_TOP_BOTTOM)
    label_img_v = label_img.transpose(Image.FLIP_TOP_BOTTOM)
    img_v.save(os.path.join(aug_root, 'img', i[:-4] + '_v' + '.jpg'))
    label_img_v.save(os.path.join(aug_root, 'label_img', i[:-4] + '_v' + '.png'))

    # horizontal flip
    img_h = img.transpose(Image.FLIP_LEFT_RIGHT)
    label_img_h = label_img.transpose(Image.FLIP_LEFT_RIGHT)
    img_h.save(os.path.join(aug_root, 'img', i[:-4] + '_h' + '.jpg'))
    label_img_h.save(os.path.join(aug_root, 'label_img', i[:-4] + '_h' + '.png'))
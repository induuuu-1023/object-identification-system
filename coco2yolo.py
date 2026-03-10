import json
import os
from tqdm import tqdm
from pycocotools.coco import COCO

def convert_coco_to_yolo(json_file, output_dir, image_dir):
    os.makedirs(output_dir, exist_ok=True)
    coco = COCO(json_file)

    # Get category mapping
    category_map = {cat['id']: i for i, cat in enumerate(coco.loadCats(coco.getCatIds()))}

    for img in tqdm(coco.dataset['images']):
        img_id = img['id']
        file_name = img['file_name']
        width = img['width']
        height = img['height']

        ann_ids = coco.getAnnIds(imgIds=img_id)
        anns = coco.loadAnns(ann_ids)

        label_file = os.path.join(output_dir, file_name.replace('.jpg', '.txt'))
        with open(label_file, 'w') as f:
            for ann in anns:
                cat_id = ann['category_id']
                bbox = ann['bbox']  # [x, y, w, h]
                x, y, w, h = bbox

                # Convert to YOLO format
                x_center = (x + w / 2) / width
                y_center = (y + h / 2) / height
                w /= width
                h /= height

                class_id = category_map[cat_id]
                f.write(f"{class_id} {x_center} {y_center} {w} {h}\n")

if __name__ == "__main__":
    json_file = r"D:\object identification system\datasets\coco\raw\annotations\annotations\instances_val2017.json"
    image_dir = r"D:\object identification system\datasets\coco\images\train2017"
    output_dir = r"D:\object identification system\datasets\coco\labels\train2017"

    convert_coco_to_yolo(json_file, output_dir, image_dir)

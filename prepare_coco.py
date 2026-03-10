import zipfile
import os
import json

# --- Paths ---
base_path = r"D:\object identification system\datasets\coco"
images_path = os.path.join(base_path, "images")
labels_path = os.path.join(base_path, "labels")

# --- Helper: unzip ---
def unzip(zip_file, extract_to):
    os.makedirs(extract_to, exist_ok=True)
    print(f"Extracting {zip_file}...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Done: {extract_to}")

# --- Step 1: Extract images ---
unzip(os.path.join(images_path, "train2017.zip"), os.path.join(images_path, "train2017"))
unzip(os.path.join(images_path, "val2017.zip"), os.path.join(images_path, "val2017"))
# (Optional) unzip test2017 if needed
# unzip(os.path.join(images_path, "test2017.zip"), os.path.join(images_path, "test2017"))

# --- Step 2: Convert COCO JSON to YOLO labels ---
def coco_to_yolo(json_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with open(json_file, 'r') as f:
        data = json.load(f)

    categories = {cat['id']: cat['name'] for cat in data['categories']}
    print(f"Converting {len(data['annotations'])} annotations...")

    for ann in data['annotations']:
        image_id = ann['image_id']
        category_id = ann['category_id']
        bbox = ann['bbox']  # [x,y,width,height]

        # Convert to YOLO format: class x_center y_center width height (normalized)
        x, y, w, h = bbox
        x_center = (x + w / 2) / data['images'][image_id-1]['width']
        y_center = (y + h / 2) / data['images'][image_id-1]['height']
        w /= data['images'][image_id-1]['width']
        h /= data['images'][image_id-1]['height']

        label_file = os.path.join(output_dir, f"{image_id:012}.txt")
        with open(label_file, 'a') as lf:
            lf.write(f"{category_id-1} {x_center} {y_center} {w} {h}\n")

    print(f"Labels saved to {output_dir}")

# Convert train + val annotations
coco_to_yolo(os.path.join(base_path, "raw", "annotations", "instances_train2017.json"),
             os.path.join(labels_path, "train2017"))

coco_to_yolo(os.path.join(base_path, "raw", "annotations", "instances_val2017.json"),
             os.path.join(labels_path, "val2017"))
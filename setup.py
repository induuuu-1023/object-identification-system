from setuptools import setup, find_packages

setup(
    name="item_detection_system",
    version="1.0.0",
    author="Indu Gautam",
    author_email="indugautam1023@gmail.com",
    description="Universal Item Detection System for ages 3-90 using YOLO and multi-dataset fusion",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/induuuu-1023/object-identification-system/tree/main",
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        "torch>=2.0.0,<2.2.0",
        "torchvision>=0.15.0,<0.17.0",
        "ultralytics>=8.0.0,<8.5.0",
        "opencv-python>=4.7.0,<4.12.0",
        "numpy>=1.23.5,<1.25.0",
        "pandas>=1.5.3,<2.0",
        "albumentations>=1.2.1,<1.4",
        "Pillow>=9.5.0,<10.0",
        "scikit-learn>=1.2.2,<1.3",
        "fiftyone>=0.23.0,<0.24",
        "imagehash>=4.3.1",
        "pyyaml>=6.0",
        "matplotlib>=3.6.3,<3.9",
        "tqdm>=4.65.0"
    ],

    entry_points={
        "console_scripts": [
            "run_detection=item_detection_system.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

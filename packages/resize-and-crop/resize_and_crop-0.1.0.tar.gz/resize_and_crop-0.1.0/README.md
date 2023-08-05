# Resize and Crop

## Description

Resize and crop an image to fit the specified size.

## Installation

```python
pip install resize-and-crop
```

or

```python
pipenv install resize-and-crop
```

## Methods

1. resize_and_crop(path, size, crop_origin) - Resize the image located at path, into the size specified, cropping the image starting at the crop_origin.

## Usage

```python
from resize_and_crop import resize_and_crop

image = resize_and_crop("/path/to/image", (200,200), "middle")
```
import os
import yaml
import json
import joblib
import base64
from box.exceptions import BoxValueError
from cnnDeseaseClassifier import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns
    Args:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox Type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_dirs: list, verbose=True):
    """Creates a list of directories
    Args:
        path_to_dirs (list): list of path fo dirs
        ignore_log(bool, optional): ignore if multiple dirs is to be created, Defaults to False.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json data"""

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads the data from json file and returns data as ConfigBox"""

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from : {path}")

    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save binary file"""

    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary file"""

    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")

    return data


@ensure_annotations
def get_file_size(path: Path) -> str:
    """Get the file size"""

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


def decode_image(imgstr, filename):
    """Decode image into base64"""
    imgdata = base64.b64decode(imgstr)

    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()


def encode_img_into_base64(cropped_image_path):
    """Encode the image to base64"""
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read())

import os
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from hub import Transform, dataset
import pandas as pd
input_size=224

class OmdenaGenerator(Transform):
    def meta(self):
        # here we specify the attributes of return type
        return {
            "nightlights_bin": {"shape": (1,), "dtype": "int", "dtag" : "text"},
            "image": {"shape": (1,), "dtype": "object", "chunksize": 100, "dtag" : "image"},
        }

    def forward(self, image_info):
        # we need to return a dictionary of numpy arrays from here
        ds = {}
        ds["nightlights_bin"] = np.empty(1, dtype="int")
        ds["nightlights_bin"][0] = image_info["nightlights_bin"]

        ds["image"] = np.empty(1, object)
        ds["image"][0] = np.array(Image.open(image_info["image_path"]).convert('RGB'))
        return ds


def load_dataset(path):
    df = pd.read_csv(os.path.join(path, "processed", "image_download_actual.csv"))
    country_dirs = os.listdir(os.path.join(path, "countries"))
    image_info_list = []
    for index, row in df.iterrows():
        image_info = {}
        image_info["image_path"]=get_image_path(row['country'],row['image_name'],path)
        image_info["nightlights_bin"]=row["nightlights_bin"]
        try:
            Image.open(image_info["image_path"])
            image_info_list.append(image_info)
        except Exception as identifier:
            print("Image not found")

    # the generator iterates through the argument given, one by one and applies forward. This is done lazily.
    ds = dataset.generate(OmdenaGenerator(), image_info_list)
    return ds


def get_image_path(country, image_name, dataset_path):
    folder = ""
    if country == "mw":
        folder = "malawi_2016"
    elif country == "ng":
        folder = "nigeria_2015"
    elif country == "eth":
        folder = "ethiopia_2015"
    return os.path.join(dataset_path, "countries", folder, "images", image_name)

if __name__ == "__main__":
    path = "./data/"
    ds = load_dataset(path)

    # stores the dataset in username/datasetname
    ds.store("aerial-predicting-poverty-replication")
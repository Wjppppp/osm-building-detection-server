from label import label
import os
from inference import inference_main

def inference(extend, model, api_token):


    print("extend",extend)
    length = label.generate_image_tiles(extend, api_token)
    # model = "FS_model_02"

    argv = [model]

    geojson = inference_main.main(argv)

    num_buildings = len(geojson['features'])

    print(f"detected buildings: {num_buildings}")

    return length, geojson, num_buildings
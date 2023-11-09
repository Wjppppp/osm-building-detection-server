from . import *
import os
import shutil
import yaml
import datetime
import geojson

def refresh_dir(PATH):
    if len(os.listdir(PATH)) >= 1:
        shutil.rmtree(PATH)
        os.makedirs(PATH)

def generate_image_tiles(extend, api_token):

    #  modify config.yaml
    with open(PATH_CONFIG_TEMPLATE, "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.Loader)
        # print(cfg)

    cfg['osm']['bboxes'] = extend
    cfg['image']['api_token'] = api_token

    with open(PATH_CONFIG_TEST,"w") as file:
        yaml.dump(cfg, file)
        print(f'config: {cfg}')


    # ohsome2label vector
    os.system(f'ohsome2label --schema {PATH_CONFIG_SCHEMA} --config {PATH_CONFIG_TEST} vector')


    # create geojson extend
    polygon = geojson.MultiPolygon([
        ([(extend[0], extend[1]),(extend[2], extend[1]),(extend[2], extend[3]),(extend[0], extend[3]),(extend[0], extend[1])],)
    ])
    feature = [geojson.Feature(
        geometry=polygon
    )]
    feature_collection = geojson.FeatureCollection(feature)

    # print(f'geojson {feature_collection}')

    with open(PATH_GEOJSON_RAW, 'w') as f:
        geojson.dump(feature_collection, f)

    refresh_dir(PATH_IMAGE)
    refresh_dir(PATH_TILE)
    refresh_dir(PATH_LABEL)

    # ohsome2label label
    os.system(f'ohsome2label --schema {PATH_CONFIG_SCHEMA} --config {PATH_CONFIG_TEST} label')
    # ohsome2label image
    os.system(f'ohsome2label --schema {PATH_CONFIG_SCHEMA} --config {PATH_CONFIG_TEST} image')

    # os.system(f'ohsome2label --schema {PATH_CONFIG_SCHEMA} --config {PATH_CONFIG_TEST} printcfg')

    length = len(os.listdir(PATH_IMAGE))
    print(f'tile num: {length}')

    return length

if __name__ == "__main__":
    extend = [10.2044794916899786,5.6874603256778036,10.2081243554005656,5.6910385317555923]
    generate_image_tiles(extend)
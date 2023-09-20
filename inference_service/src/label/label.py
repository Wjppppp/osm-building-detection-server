import os
import yaml
import datetime
import geojson

def generate_image_tiles(extend):

    #  modify config.yaml
    with open("./config/config_template.yaml", "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.Loader)
        print(cfg)

    cfg['osm']['bboxes'] = extend

    with open("./config/config_test.yaml","w") as file:
        yaml.dump(cfg, file)


    # ohsome2label vector
    os.system('ohsome2label --config config/config_test.yaml vector')


    # create geojson extend
    polygon = geojson.MultiPolygon([
        ([(extend[0], extend[1]),(extend[2], extend[1]),(extend[2], extend[3]),(extend[0], extend[3]),(extend[0], extend[1])],)
    ])
    feature = [geojson.Feature(
        geometry=polygon
    )]
    feature_collection = geojson.FeatureCollection(feature)

    with open("./data/other/raw/building_building_.geojson", 'w') as f:
        geojson.dump(feature_collection, f)

    # ohsome2label label
    os.system('ohsome2label --config config/config_test.yaml label')
    # ohsome2label image
    os.system('ohsome2label --config config/config_test.yaml image')

    length = len(os.listdir("./data/images"))
    print(length)

    return length

if __name__ == "__main__":
    extend = [10.2044794916899786,5.6874603256778036,10.2081243554005656,5.6910385317555923]
    generate_image_tiles(extend)
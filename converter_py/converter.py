import sys
import subprocess

def convert_osm_to_mbtiles(pbf_file, mbtiles_file):
    try:

        # Шаг 1: Преобразование OSM PBF в GeoJSON
        intermediate_geojson = "intermediate.geojson"
        print("convert pbf to geojson")
        osmium_command = ["osmium", "export", pbf_file, "-o", intermediate_geojson]
        subprocess.run(osmium_command, check=True)

        # Шаг 2: Преобразование GeoJSON в MBTiles
        print("convert geojson to mbtiles")
        tippecanoe_command = ["tippecanoe", "-o", mbtiles_file, intermediate_geojson]
        subprocess.run(tippecanoe_command, check=True)

        # Удаление промежуточного файла GeoJSON
        subprocess.run(["rm", intermediate_geojson])
    except Exception as e:
        print(f"FAIL: {e}")
# Пример использования
# pbf_file = "../pbf_files/north-caucasus-fed-district-latest.osm.pbf"
# mbtiles_file = "../tileserver-data/test.mbtiles"
# convert_osm_to_mbtiles(pbf_file, mbtiles_file)

if __name__ == "__main__":
    # Получение аргументов командной строки
    pbf_file = sys.argv[1]
    mbtiles_file = sys.argv[2]

    # Вызов функции convert_osm_to_mbtiles
    convert_osm_to_mbtiles(pbf_file, mbtiles_file)
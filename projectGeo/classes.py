import os
import platform
import re
import shutil
import tempfile
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as panda
from datetime import date, datetime
from zipfile import *

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  METHODS  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class CliRetun():
    def __init__(self, status, conteudo):
        self.status = status
        self.conteudo = conteudo

    def generate_msg(self):
        response = {"status_code": self.status}
        if self.conteudo is not None:
            response["conteudos"] = self.conteudo
        return response

class ErrorMsg():
    def __init__(self, colum_x, colum_y):
        self.colum_x = colum_x
        self.colum_y = colum_y

    def msg_erro(self):
        return f'Quantidade incorreta para gerar a tupla: {len(self.colum_x)},{len(self.colum_y)}'

class FeatureGeometry():
    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y

    def generate_geometry(self):
        return {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "geometry": {
                "type": "Point",
                "coordinates":  [self.point_x, self.point_y]
              },
              "properties": {
                "weather": "Overcast",
                "temp": "30.2 F"
              }
            }
          ]
        }

class Timer():
    def __init__(self, data=None):
        self.data = data

    def data_textform(self):
        date_current = date.today().strftime("%d_%m_%Y")
        time = datetime.now().time()
        return f'{date_current}_{time.minute + time.microsecond}'

class Generates():
    def __init__(self, text=None):
        self.text = text

    # Has regex implamentation for generate columns and rows
    def generate_columns_x_y(self):
        ColumnX = (re.findall(r"\d{6}\,\d{3}\b | \d{3}\.\d{3},\d{2,3}", self.text))
        ColumnY = (re.findall(r"\d{7}\,\d{3}, | \d{1}\.\d{3}\.\d{3}\,\d{2,3}", self.text))
        return (ColumnX, ColumnY)

    # Has regex implamentation for generate columns and rows for shapely polygon
    def generate_columns_shape(self):
        substituicoes = re.sub(r'(?<=\d)[.]', '', self.text)
        texto_formatado = re.sub(r'(?<=\d)[,]', '.', substituicoes)
        ColumnX = (re.findall(r" \d{6}\ | \d{6}\.\d{2,3}", texto_formatado))
        ColumnY = (re.findall(r" \d{7}\ | \d{7}.\d{2,3}", texto_formatado))
        return (ColumnX, ColumnY)

    # Return the tupla and coordinates geometrics
    def generate_tupla_and_geometry(self, point_a, point_b):
        tupla = {'Coordenada X': point_a, 'Coordenada Y': point_b}
        geoPosition = FeatureGeometry(point_a, point_b).generate_geometry()
        return (tupla, geoPosition)

class OperationZip():
    def __init__(self, directory_temp=None, time=None, files_saved=None):
        self.directory_temp = directory_temp
        self.time = time
        self.files_saved = files_saved

    def empacotar_in_zip(self):
        path = self.directory_temp + f"/{self.time}_shapelyGeometry_Memorial.zip"
        with ZipFile(path, "w") as myzip:
            for count in range(len(self.files_saved)):
                myzip.write(self.files_saved[count])  # NOME DO ARQUIVO QUE DESEJA COLOCAR NO .ZIP
        return path

class Export():
    def __init__(self, directory_temp=None, time=None, geo_data_frame=None,
                 obj_panda=None, dado=None, EPSG=None, tupla=None):
        self.directory_temp = directory_temp
        self.time = time
        self.geo_data_frame = geo_data_frame
        self.obj_panda = obj_panda
        self.dado = dado
        self.EPSG = EPSG
        self.tupla = tupla

    def export_for_csv(self, directory_temp, dado, time):
        data = panda.DataFrame(data=dado)
        path = directory_temp + f"/{time}_csvCoordenates.csv"
        data.to_csv(path)
        return path

    def export_shapely_and_plot(self, directory_temp, geo_data_frame, time):
        path = directory_temp + f"/{time}_shapGeo.shp"
        geo_data_frame.to_file(path)
        self.make_plot(directory_temp, geo_data_frame, time)
        return path

    def make_plot(self, directory_temp, geo_data_frame, time):
        geo_data_frame.plot(figsize=(16, 14), facecolor='white', edgecolor='black')
        plt.title('Memorial')
        plt.savefig(directory_temp + f"/{time}_shapelyPlot.png")  # save the figure in file shapely

    def export_shape_and_geometry(self, tupla, EPSG):
        obj_panda = panda.DataFrame(data=tupla)
        geometry = gpd.points_from_xy(obj_panda.col1, obj_panda.col2)
        geo_data_frame = gpd.GeoDataFrame(obj_panda, geometry=geometry, crs=EPSG)
        return (obj_panda, geo_data_frame)

    def estruct_shape_pandas(self, tupla, EPSG):
        frame_objs = panda.DataFrame(data=tupla)
        geometry_dados = gpd.points_from_xy(frame_objs.col1, frame_objs.col2)
        graph_objs = gpd.GeoDataFrame(frame_objs, geometry=geometry_dados, crs=EPSG)
        frame_objs.astype('float').dtypes

class DirectoryTemp():
    def __init__(self, route=None):
        self.route = route

    def get_createDir_temp(self):
        try:
            so = platform.system()
            default_tmp_dir = tempfile.gettempdir()
            if so == 'Linux':
                os.makedirs(default_tmp_dir + "/Geofiles")
                return default_tmp_dir + "/Geofiles"
            elif so == 'Windows':
                os.makedirs(default_tmp_dir + "\Geofiles")
                return default_tmp_dir + "\Geofiles"
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

    def clear_dir_temp(self, route):
        try:
            shutil.rmtree(route)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

class ListFolder():
    def __init__(self, directory_temp):
        self.directory_temp = directory_temp

    def list_archives_of_folder(self):
        route_files = self.directory_temp
        os.chdir(route_files)
        files_saved = []
        for file in os.listdir():
            files_saved.append(file)
        return files_saved

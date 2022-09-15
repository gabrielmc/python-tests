# Libs Imports
#import PyPDF2
#import os
#from fastapi import FastAPI, HTTPException, UploadFile, File
#from fastapi.responses import FileResponse
#from http import HTTPStatus
#from classes import *
#from functions import *

'''
app = FastAPI(
    name="Coordinates",
    title="API GeoProcessamento",
    description="Coordinates geometric",
    version="1.1.0",
    debug=True
)
'''

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  BACKUP  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

"""
@app.get("/insiraTexto", tags=["Geo Processamento"], description="Coloca a string no input, sairá o shape")
async def selecione_o_texto_e_informe_o_EPSG_para_para_gerar_o_Shapely(text: str, EPSG: int):
    try:
        # EPSG = 31984
        tupla_coords = generate_columns_shape(text)
        data, geo_data_frame = export_shape_and_geo(tupla_coords, EPSG)
        path_csv = export_csv(data)
        export_shapely(geo_data_frame)
        make_plot(geo_data_frame)
        file_path = os.path.join(path_csv)
        return FileResponse(file_path, media_type="text/csv", filename=f"{data_em_texto()}_coordinatesUTM.csv")
    except HTTPException as er:
        return ('HTTP Error:', er.detail)
"""

"""
Metodo responsável pela leitura de arquivo .txt enviado, gerando aequivos em CSV e Json(Para geometrias)  
@:param: file -> UploadFile = File(...)
@:method: upload_doc_in_format_txt
"""
"""
@app.post("/uploadTexto", tags=["Geo Processamento"], description="Ler arquivo .txt")
async def upload_de_arquivo_no_formato_txt_e_EPSG_para_gerar_o_Shapely(EPSG: int, file: UploadFile = File(...)):
    try:
        if (not ('.txt' in file.filename)):
            return CliRetun(HTTPStatus.OK, "Arquivo não está no formato .txt !").generate_msg()

        text_complete = str(await file.read())
        columX, columY = generate_columns_x_y(text_complete)
        if (not (len(columX) - len(columY) == 0)):
            return CliRetun(HTTPStatus.OK, msg_erro(len(columX), len(columY))).generate_msg()

        matriz = []
        geoconfig = []
        for count in range(len(columX)):
            point_x, point_y = remove_point(columX[count].lstrip()), remove_point(columY[count].lstrip())
            tupla, geoPosition = generate_tupla_and_geometry(point_x, point_y)
            matriz.append(tupla)
            geoconfig.append(geoPosition)

        path_csv, path_json = export_csv_and_json(matriz, geoconfig)
        file_path = os.path.join(path_csv)
        return FileResponse(file_path, media_type="text/csv", filename=f"{data_em_texto()}_coordinatesUTM.csv")
    except HTTPException as er:
        return ('HTTP Error:', er.detail)
"""

"""
Metodo responsável pela leitura de campo texto enviado gerando aequivos em CSV e Json(Para geometrias)  
@:param text: str,
@:method read_text_for_coordenates
"""
'''
@app.get("/text", tags=["Geo Processamento"], description="Coloca a string no input")
async def read_text_generate_coordenates(text: str):
    try:
        columX, columY = generate_columns_x_y(text)
        matriz = []
        geoconfig = []
        if (not (len(columX) - len(columY) == 0)):
            return CliRetun(HTTPStatus.OK, msg_erro(len(columX), len(columY))).generate_msg()

        for count in range(len(columX)):
            point_x, point_y = remove_point(columX[count].lstrip()), remove_point(columY[count].lstrip())
            tupla, geoPosition = generate_tupla_and_geometry(point_x, point_y)
            matriz.append(tupla)
            geoconfig.append(geoPosition)

        export_csv(matriz)
        export_json(geoconfig)
        return CliRetun(HTTPStatus.OK, geoconfig).generate_msg()
    except HTTPException as er:
        return ('HTTP Error:', er.detail)
'''

"""
Metodo responsável pela leitura de campo texto enviado gerando aequivos em CSV e Json(Para geometrias)  
@:param text: str,
@:method read_text_for_coordenates
"""
'''
@app.post("/uploadPdf", tags=["Geo Processamento"], description="Ler arquivo .pdf")
async def upload_doc_in_format_pdf(file: UploadFile = File(...) ):
    try:
        if (not ('.pdf' in file.filename) ):
            return CliRetun(HTTPStatus.OK, "Arquivo não está no formato .pdf !").generate_msg()

        #pdf_file = open(r"/home/gmuniz/Documentos/MEMORIAL_DESCRITIVO_UTM.pdf", 'rb')
        #pdf_file = open(file, 'r+b')
        #dados_pdf = PyPDF2.PdfFileReader(pdf_file)
        #qtd_pages = int(dados_pdf.numPages)
        #tetx = text_complete_binary.encode('utf-8')



        text_complete_binary = str(await file.read(), 'utf-8')
        #textasd = text_complete_binary.decode(encoding='utf-8')

        #pdf_file = open(text_complete_binary, 'rb')
        #jysad = pdf_file.read()
        #dados_pdf = PyPDF2.PdfFileReader(pdf_file.read())
        #qtd_pages = int(dados_pdf.numPages)
        #text = file.filename



        matriz = []
        geoconfig = []
        text_complete = ""
        for count in range(qtd_pages):
            text_complete += dados_pdf.getPage(count).extractText()

        columX, columY = generate_columns_x_y(text_complete)
        if (not (len(columX) - len(columY) == 0)):
            return CliRetun(HTTPStatus.OK, msg_erro(len(columX), len(columY))).generate_msg()

        for count in range(len(columX)):
            point_x, point_y = remove_point(columX[count].lstrip()), remove_point(columY[count].lstrip())
            tupla, geoPosition = generate_tupla_and_geometry(point_x, point_y)
            matriz.append(tupla)
            geoconfig.append(geoPosition)

        path_csv, path_json = export_csv_and_json(matriz, geoconfig)
        file_path = os.path.join(path_csv)

        return CliRetun(HTTPStatus.OK, "text_complete_binary").generate_msg()
        #return FileResponse(file_path, media_type="text/csv", filename=f"{data_em_texto()}_coordinatesUTM.csv")
    except HTTPException as er:
        return ('HTTP Error:', er.detail)
'''

'''
@app.post("/uploadDocPDF", tags=["Geo Processamento"], description="Ler arquivo PDF no upload")
def upload_doc_ler_pdf():
    try:
        pdf_file = open(r"/home/gmuniz/Documentos/MEMORIAL_DESCRITIVO_UTM.pdf", 'rb')
        dados_pdf = PyPDF2.PdfFileReader(pdf_file)
        qtd_pages = int(dados_pdf.numPages)
        matriz = []
        geoconfig = []
        text_complete = ""
        for count in range(qtd_pages):
            text_complete += dados_pdf.getPage(count).extractText()

        columX, columY = generate_columns_x_y(text_complete)
        if (not is_valid_matriz(len(columX), len(columY))):
            return CliRetun(HTTPStatus.OK, msg_erro(len(columX), len(columY))).generate_msg()

        for count in range(len(columX)):
            point_x, point_y = remove_point(columX[count].lstrip()), remove_point(columY[count].lstrip())
            tupla, geoPosition = generate_tupla_and_geometry(point_x, point_y)
            matriz.append(tupla)
            geoconfig.append(geoPosition)

        export_csv_and_json(matriz, geoconfig)
        return CliRetun(HTTPStatus.OK, geoconfig).generate_msg()
    except HTTPException as er:
        return ('HTTP Error:', er.detail)
'''
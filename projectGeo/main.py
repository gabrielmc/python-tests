from fastapi import FastAPI, HTTPException, BackgroundTasks as taskBack
from fastapi.responses import FileResponse
from http import HTTPStatus
from classes import *

app = FastAPI(
    name="Coordinates",
    title="API GeoProcessamento",
    description="Coordinates geometric",
    version="1.1.0",
    debug=True
)


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ENDPOINTS  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


"""
Metodo responsável pela leitura de campo texto selecionado de um PDF memorial junto com o EPSG.
Gerando arquivo em CSV e Shapely com .png plotado(Para geometrias e QGIS)  
@:param text: str
@:param EPSG: int | defaul -> EPSG = 31984
@:method /insiraTexto
"""
@app.get("/insiraTexto", tags=["Geo Processamento"], description="Coloca a string no input, sairá o shape")
async def selecione_o_texto_e_informe_o_EPSG_para_gerar_o_Shapely(text: str, EPSG: int, parallel_task: taskBack):
    try:
        if EPSG is None:
            return CliRetun(HTTPStatus.BAD_REQUEST, "EPSG não foi informado de maneira correta!").generate_msg()

        ColumnX, ColumnY = Generates(text).generate_columns_shape()
        if not (len(ColumnX) - len(ColumnY) == 0):
            return CliRetun(HTTPStatus.OK, ErrorMsg(ColumnX, ColumnY).msg_erro()).generate_msg()

        Exp, DirTemp = Export(), DirectoryTemp()
        time = Timer().data_textform()
        obj_panda, geo_data_frame = Exp.export_shape_and_geometry(tupla={'col1': ColumnX, 'col2': ColumnY}, EPSG=EPSG)
        directory_temp = DirTemp.get_createDir_temp()
        Exp.export_shapely_and_plot(directory_temp, geo_data_frame, time)
        Exp.export_for_csv(directory_temp, obj_panda, time)
        files_saved = ListFolder(directory_temp).list_archives_of_folder()
        path_files = OperationZip(directory_temp, time, files_saved).empacotar_in_zip()
        file_path_for_out = os.path.join(path_files)
        filename = f'{time}_shapelyMemorial.zip'
        return FileResponse(file_path_for_out, media_type="application/zip", filename=filename)
    except HTTPException as er:
        return ('HTTP Error:', er.detail)
    finally:
        parallel_task.add_task(DirTemp.clear_dir_temp, directory_temp)


"""
Metodo responsável pela leitura de um arquivo .txt de um PDF memorial junto com o EPSG.
Gerando arquivo em CSV e Shapely com .png plotado(Para geometrias e QGIS)  
@:param file: -> UploadFile = File(...) Type : .txt
@:param EPSG: int | defaul -> EPSG = 31984
@:method /uploadTexto
"""
'''
@app.post("/uploadTexto", tags=["Geo Processamento"], description="Ler arquivo .txt")
async def upload_de_arquivo_no_formato_txt_e_EPSG_para_gerar_o_Shapely(parallel_task: taskBack, EPSG: int, file: UploadFile = File(...)):
    try:
        if (not ('.txt' in file.filename) ):
            return CliRetun(HTTPStatus.BAD_REQUEST, "Arquivo não está no formato .txt!").generate_msg()

        if (EPSG is None):
            return CliRetun(HTTPStatus.BAD_REQUEST, "EPSG não foi informado de maneira correta!").generate_msg()

        text_complete = str(await file.read())
        ColumnX, ColumnY = Generates(text_complete).generate_columns_shape()
        if (not (len(ColumnX) - len(ColumnY) == 0)):
            return CliRetun(HTTPStatus.OK, ErrorMsg(ColumnX, ColumnY).msg_erro()).generate_msg()

        Exp = Export()
        DirTemp = DirectoryTemp()
        time = Timer().data_in_text()

        obj_panda, geo_data_frame = Exp.export_shape_and_geometry(tupla={'col1': ColumnX, 'col2': ColumnY}, EPSG=EPSG)
        directory_temp = DirTemp.get_createDir_temp()
        Exp.export_shapely_and_plot(directory_temp, geo_data_frame, time)
        Exp.export_for_csv(directory_temp, obj_panda, time)

        files_saved = ListFolder(directory_temp).list_archives_of_folder()
        path_files = OperationZip(directory_temp, time, files_saved=files_saved).empacotar_in_zip()
        file_path_for_out = os.path.join(path_files)
        filename = f"{time}_shapelyMemorial.zip"
        return FileResponse(file_path_for_out, media_type="application/zip", filename=filename)
    except HTTPException as er:
        return ('HTTP Error:', er.detail)
    finally:
        parallel_task.add_task(DirTemp.clear_dir_temp, directory_temp)



"""
Metodo responsável pela leitura de um arquivo .pdf de um PDF memorial junto com o EPSG.
Gerando arquivo em CSV e Shapely com .png plotado(Para geometrias e QGIS)  
@:param file: -> UploadFile = File(...) Type : .pdf
@:param EPSG: int | defaul -> EPSG = 31984
@:method /uploadPdf
"""
@app.post("/uploadPdf", tags=["Geo Processamento"], description="Ler arquivo .pdf")
async def upload_de_arquivo_no_formato_PDF_e_EPSG_para_gerar_o_Shapely(EPSG: int, file: UploadFile = File(...) ):
    try:
        if (not ('.pdf' in file.filename) ):
            return CliRetun(HTTPStatus.OK, "Arquivo não está no formato .pdf !").generate_msg()

        #pdf_file = open(r"/home/gmuniz/Área de Trabalho/places/python_place/projectGeo/docs/MEMORIAL DESCRITIVO GILDÁSIO D'OLIVEIRA.pdf", 'rb')
        pdf_file = await file.read()

        dados_pdf = PyPDF2.PdfFileReader(pdf_file)
        qtd_pages = int(dados_pdf.numPages)
        text_complete = ""
        for count in range(qtd_pages):
            text_complete += dados_pdf.getPage(count).extractText()

        if (text_complete is None):
            return CliRetun(HTTPStatus.BAD_REQUEST, "Conteúdo do texto não foi lido!").generate_msg()

        ColumnX, ColumnY = generate_columns_shape(text_complete)
        if (not (len(ColumnX) - len(ColumnY) == 0)):
            return CliRetun(HTTPStatus.OK, ErrorMsg(ColumnX, ColumnY).msg_erro()).generate_msg()

        tupla_coords = {'col1': ColumnX, 'col2': ColumnY}
        data, geo_data_frame = export_shape_and_geo(tupla_coords, EPSG)
        time = data_em_texto()
        export_shapely_and_plot(geo_data_frame, time)
        path_csv = export_csv_for_sh(data, time)
        file_path = os.path.join(path_csv)
        return FileResponse(file_path, media_type="text/csv", filename=f"{time}_coordinatesUTM.csv")
    except HTTPException as er:
        return ('HTTP Error:', er.detail)
'''
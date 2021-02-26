import pandas as pd
import numpy as np
import os
import zipfile


total_zip_files = os.listdir(".\TRUE_FX_ZIP")

print(total_zip_files)

created_folders = 0

extracted_files = 0

for i in total_zip_files:

    try:
        os.mkdir(os.path.join(".\TRUE_FX_EXTRACTED", i))

        print("Creada carpeta", i)

        created_folders += 1

        with zipfile.ZipFile(os.path.join(".\TRUE_FX_ZIP", i), 'r') as zip_ref:
            zip_ref.extractall(os.path.join(".\TRUE_FX_EXTRACTED", i))

        print("Extraido archivo", i)

        extracted_files += 1

    except:

        print("No puedo extraer, la carpeta " + str(i) + " ya está creada.")

print("Se han extraído " + str(extracted_files) + " archivos .zip y se han creado " + str(created_folders) + " carpetas")
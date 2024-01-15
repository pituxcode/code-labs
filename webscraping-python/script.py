#%%
import pandas as pd
tabla_poblacion = pd.read_html("https://www.worldometers.info/world-population/population-by-country/")
print(tabla_poblacion)
tabla_libros = pd.read_html("https://es.wikipedia.org/wiki/Anexo:Libros_m%C3%A1s_vendidos")
tabla_libros
tabla_poblacion[0].to_csv("tabla-poblacion-mundial.csv", index = False)
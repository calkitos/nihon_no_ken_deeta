import marimo

__generated_with = "0.19.4"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Prefecturas de Japón


    En este trabajo vamos a analizar, estudiar y conocer mucha información sobre las prefecturas de Japón. Una [_prefectura_](https://es.wikipedia.org/wiki/Prefectura) es un órgano de gobierno o área territorial. [Japón](https://es.wikipedia.org/wiki/Jap%C3%B3n) está dividido en 47 jurisdicciones territoriales denominadas prefecturas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Preparación


    Primero vamos a preparar lo que necesitamos. Descargamos algunos paquetes e instalamos módulos que nos ayudarán a lograr el objetivo.
    """)
    return


@app.cell
def _():
    import marimo as mo
    import micropip
    # await micropip.install("geopandas")
    # await micropip.install("folium")
    # await micropip.install("mapclassify")


    import folium
    import geopandas as gpd
    import mapclassify
    import pandas as pd
    import zipfile


    from matplotlib import pyplot as plt
    from pathlib import Path
    return Path, gpd, mo, zipfile


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ahora vamos a abrir el archivo de datos que necesitamos analizar.
    """)
    return


@app.cell
def _(Path, gpd, zipfile):
    filename = "prefectures_shape-20260116T003222Z-1-001.zip"
    path = Path("prefectures_shape/")


    if path.exists():
        print("EXISTS")

    else:
        with zipfile.ZipFile(filename, "r") as zip_file:
            filelist = zip_file.namelist()
            print(filelist)
            zip_file.extractall()


    data = gpd.read_file("prefectures_shape/prefectures_data.shp")
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A continuación, nos aseguramos rápdiamente de que la información sobre el año sea un número sin decimales.


    Ahora veamos cuál es la información que tenemos disponible.
    """)
    return


@app.cell
def _(data):
    data["year"] = data["year"].astype(int)

    data.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Nota esta columna llamada 'geometry'.


    ¿Qué crees que es? ¿De qué crees que se trata?


    Mira la siguiente imagen y piensa cómo se relaciona con esos números:


    ![](https://www.onlinemath4all.com/images/fourquadrants8.png)
    """)
    return


@app.cell
def _(data):
    print(data.loc[0,"geometry"])
    return


@app.cell
def _(data, mo):
    year = mo.ui.dropdown(data["year"].unique().tolist(), label="AÑO: ")
    year
    return (year,)


@app.cell
def _(data, year):
    subset = data[data["year"] == year.value].reset_index()
    subset.drop("index", axis=1, inplace=True)
    subset.explore("region")
    return (subset,)


@app.cell
def _(subset):
    subset.sort_values("population", ascending=False).head(10)
    return


@app.cell
def _(subset):
    subset.explore("population")
    return


if __name__ == "__main__":
    app.run()

import matplotlib.pyplot as plt
from math import ceil

#EDA VARIABLES CATEGORICAS:

def Graphs_EDA_STRINGS(cat):
    
    #Calculamos el número de filas que necesitamos:

    filas = ceil(cat.shape[1] / 2)

    #Definimos el gráfico:

    f, ax = plt.subplots(nrows = filas, ncols = 2, figsize = (16, filas * 6))

    #Aplanamos para iterar por el gráfico como si fuera de 1 dimensión en lugar de 2:

    ax = ax.flat 

    #Creamos el bucle que va añadiendo gráficos:
    
    for cada, variable in enumerate(cat):
        cat[variable].value_counts().plot.barh(ax = ax[cada])
        ax[cada].set_title(variable, fontsize = 12, fontweight = "bold")
        ax[cada].tick_params(labelsize = 12)


#EDA VARIABLES NUMERICAS:

def estadistic_cont(num):

    #Calculamos describe:

    estadisticos = num.describe().T 
    #Añadimos la mediana:

    estadisticos['median'] = num.median()
    #Reordenamos para que la mediana esté al lado de la media:

    estadisticos = estadisticos.iloc[:,[0,1,8,2,3,4,5,6,7]]
    
    return(estadisticos)



# SENSE_HAT_EMULATOR

Ejemplo de aplicación de escritorio realziada con la libreria Tkinter y usando el emulador SENSE HAT.  

Version: 0.1

## Objetivo

*Finalidad didáctica:*  

Construir una interfaz de escritorio para poder interaccionar en tiempo real con una aplicación de simulación de datos ambientales.  


## Librerias

Se necesitarán instalar las siguientes librerías:

> Emulador: [sense-emu](https://sense-emu.readthedocs.io/en/v1.0/install.html)  

> Libreria para construir interfaces gráficas de escritorio: [tkinter](https://tkdocs.com/tutorial/install.html)  

> Libreria para generar los gráficos: [matplotlib](https://matplotlib.org/3.1.1/faq/installing_faq.html)  

> Versión de Python utilizada: 3.7.3

## Ejecutar aplicación

Una vez instalada las librerias necesarias, ubicarse en la carpeta donde se clonó este repositorio y ejecutar el siguiente comando:

```python
python3 monitoring.py  
```

Pudiera darse el caso de necesitar arrancar inicialmente la aplicación SENSE_HAT_EMULATOR

## Usando la interfaz gráfica

- Se pueden monitorizar los siguientes parámetros: Temperatura, Presión y Humedad
  Desde la pantalla del emulador a través de los sliders de estos parámetros se pueden variar los valores y se registraán en al aplicación.  
- El intervalo de captura por defecto está fijado a 1 seg (1000mseg) y se podrá modificar desde el menú OPCIONES > PROPIEDADES.
- Para mostrar valores en la gráfica habrá que INICIAR la captura de datos, para ello pulsar el botón INICAR en la sección CONTROL
  de la pestaña MONITORIZACIÓN.
- El eje X de la gráfica representa la marca de tiempo en formato numerico a través de los minutos y segundos. 
  Ejemplo: 18:25:32 --> Marca tiempo = 2532
           09:04:03 --> Marca tiempo =  403
- La visualización gráfica dispone de una barra de menú desde la que se pueden realizar capturas del gráfico entre otras opciones.
- Desde la pestaña MONITORIZACION se dispone de un botón para poder EXPORTAR los datos monitorizados a un fichero *.CSV




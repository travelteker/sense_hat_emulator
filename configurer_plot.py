class ConfigPlot:
    
    FACECOLOR = '#d469a3'
    LABEL_X = 'Marca Tiempo'
    # ROWS,COLUMNS,INDEX
    SUBPLOT = 111
    TITLE = 'title'
    LABEL = 'label'
    # Rotacion texto EJE X
    ROTATION_X = 45
    TIME = 'time'
    SENSOR = 'sensor'


    def __init__(self):
        pass

    def tags_canvas(self):
        # Sensor seleccionado (1-> Temp, 2-> Pres, 3-> Hume)
        return {
            "1": {
                self.TITLE: "Monitor Temperatura",
                self.LABEL: "Valor Tª (ºC)"
            },
            "2": {
                self.TITLE: "Monitor Presión",
                self.LABEL: "Valor P (mmHg)"
            },
            "3": {
                self.TITLE: "Monitor Humedad",
                self.LABEL: "Valor H (%)"
            },
        }

    def dimensions_canvas(self):
        return {
            'x':85, 
            'y':10,
            'width':650,
            'height':550
        }

    def plot_style_temp(self):
        return {
            'color': 'red',
            'marker': 'o',
            'linestyle': 'dashed',
            'linewidth': 2,
            'markersize': 10,
            'label': 'Valores Sensor Temperatura'
        }
    
    def plot_style_pres(self):
        return {
            'color': 'green',
            'marker': 'v',
            'linestyle': 'dashed',
            'linewidth': 2,
            'markersize': 10,
            'label': 'Valores Sensor Presión'
        }

    def plot_style_humd(self):
        return {
            'color': 'blue',
            'marker': '*',
            'linestyle': 'dashed',
            'linewidth': 2,
            'markersize': 10,
            'label': 'Valores Sensor Humedad'
        }

    def get_style_sensor(self, value):
        styles = {
            '1': self.plot_style_temp(),
            '2': self.plot_style_pres(),
            '3': self.plot_style_humd(),
        }
        return styles[value]
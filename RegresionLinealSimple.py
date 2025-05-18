class RegresionLineal:
    
    def __init__(self):
        self.m = None
        self.b = None
    
    def calcularPromedio(self, numeros):
        suma = 0
        for i in range(len(numeros)):
            suma += numeros[i]
        return suma / len(numeros)
    
    def calcularPendiente(self, x:list, y:list):
        prom_x = self.calcularPromedio(x)
        prom_y = self.calcularPromedio(y)
        n = len(x)
        suma_cuadrados = sum(i**2 for i in x)
        suma_productos = sum(x[i]*y[i] for i in range(n))
        self.m = (suma_productos - n*prom_x*prom_y) / (suma_cuadrados - n*(prom_x)**2)
        return self.m

    def calcularOrdenada(self, x:list, y:list):
        self.b = self.calcularPromedio(y) - self.calcularPendiente(x, y)*self.calcularPromedio(x)
        return self.b
    
    def estimaciones(self, x:list, y:list):
        pendiente = self.calcularPendiente(x, y)
        ordenada = self.calcularOrdenada(x, y)
        y_estimado = []
        for i in range(len(x)):
            Y = pendiente * x[i] + ordenada
            y_estimado.append(Y)
        return y_estimado


#Método que não recebe parâmetro e retorna um dado
def getPI():
    return 3.14

#Método que recebe parâmetro e retorna um dado
def calcularArea(raio):
    area = raio * raio * getPI() 
    return area

#Método que recebe parâmetro e não retorna um dado
def imprimirAreaCirculo( raio_ ):
    print( calcularArea(raio_) )

#Método que não recebe parâmetro e não retorna um dado
def imprimirPi():
    print( getPI() )
    

print( "Valor do Pi: ")
imprimirPi()
imprimirAreaCirculo(4)

x = getPI()
y = getPI
print("---------------")
print( x )
print("---------------")
print( y )
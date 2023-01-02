#funciones integradas

#int(). int convierte una cadena a entero

num = int("10")

print(num)

#float(). convierte una cadena a flotante 

num = float("12.3")

print(num)

#str(). pasa un valor numerico a una cadena

num = str(11)

print(num)

#bin(). para un valor numerico a binario

num = bin(10)

print(num)

#hex(). pasa un valor numerico a hexadecimal

num = hex(11)

print(num)

#pasar un binario a entero. para pasar un binario a entero usamos la funcion int()

#tenemos que indicar que valor es binario. para eso usamos los digitos 0b

num = int("0b1010",2) # tenemos que indicarle en que base esta el numero para que sepa convertirlo a un entero

print(num)

#para pasar un valor hexadecimal a entero hacemos lo mismo

num = int("0xb",16)

print(num) 

#abs(). saca el valor absoluto de un numero

num = abs(-43)

print(num)

#round(). redondea un numero al valor mas cercano

num = round(12.3)

print(num)

#len() retorna el numero de elementos en una cadena

num = len("Juan mamaguevi")

print(num)
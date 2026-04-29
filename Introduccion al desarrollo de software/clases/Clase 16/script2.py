# Autor: David Cañaveral Lopera
# Fecha: 29/04/2026
# Version: 1.0
# Descripcion: Likes

likes = [93, 56, 82, 103, 22]

contador_cien= 0 
suma_likes = 0

for i in likes:
    suma_likes += i
    if i >= 100: contador_cien +=1

promedio_likes = suma_likes / len(likes)

print(f'Promedio de likes: {promedio_likes}')
print(f'El total de likes es: {suma_likes}')
print(f'Publicaciones con 100 likes o mas {contador_cien}')
Sistemas-Operativos-y-Redes
===========================

¿Cómo hacerlo?

En caso de windows, abren Git bash, buscan una posición que sea de su interés (usando cd) y ejecutan la siguiente línea:

git clone git@github.com:julioadriazola/Sistemas-Operativos-y-Redes.git

En el caso de Linux, abren consola (ctrl+alt+t), buscan dirección de su interés y ejecutan la misma línea.

¿Si quiero ver mi estado con respecto a la última versión LOCAL?

git status

¿Si quiero agregar algún archivo en particular a mi versión LOCAL?

git add carpeta1/carpeta2/carpeta3/nombre_de_archivo.algo

¿Si quiero agregar TODOs los archivos creados y cambiados a mi versión LOCAL?

git add .

¿Y si además quiero borrar los archivos que borré?

git add . -A

¿Y ahora, cómo hago commit a mi para respaldar mi versión LOCAL?

git commit -m "Un mensaje cualquiera"

Si no haces el -m te pedirá que ingreses un mensaje manualmente a través de VII (creo), el cual es un editor por consola difícil de manejar.

¿Y si quiero compartir mi versión local con el resto?

Oh! espera, primero es mejor que traigas los cambios del resto antes de poner tus cambios, o tendrás problemas de versión. Esto se hace con:

git pull

y para poner tu última versión...

git push

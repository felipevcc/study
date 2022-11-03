## Reto 1 ¿Cuánto costará el teléfono?
"""El IVA es un Impuesto sobre el Valor Añadido de un servicio o producto. En España
disponemos de varios tipos de IVA (21%, 10% y 4%). Este impuesto grava sobre el precio
neto del producto, es decir, el precio total o bruto corresponde al precio neto del
producto más el impuesto que se le aplica.
Estamos interesados en comprar un nuevo teléfono móvil y en el escaparate de una tienda
aparece que el móvil cuesta 420€. El problema es que si nos esperamos a comprarlo al
día siguiente sufrirá un incremento porcentual del 20%. ¿Cuánto costará entonces el
teléfono si nos esperamos?"""

telefono = 420
porcentaje = .20
incremento = telefono * porcentaje
valor = int(telefono + incremento)
print(f'Si se espera un dia mas, el valor total del telefono será de: {valor}€\n')


## Reto 2: ¿Cuántas vueltas dará un Fidget Spinner?
"""El spinner es un juguete que cabe en la palma de la mano y consiste en tres aros unidos
entre sí. En el centro hay un círculo que hace las veces de eje giratorio y permite que
los aros de vueltas y más vueltas, como las hélices de un helicóptero.
Sabemos que un Fidget Spinner da 147 vueltas por minuto ¿Cuántas vueltas dará en 640
segundos? Para este ejercicio se desprecia el rozamiento con el aire."""

vueltas_min = 147

segundos = 640
minutos = segundos / 60
vueltas = int(vueltas_min * minutos)
print(f'En {segundos} segundos el Fidget Spinner dará {vueltas} vueltas\n')


## Reto 3: ¿Cuántas latas de refresco sobran?
"""Un acto de graduación es la ceremonia oficial que clausura el curso escolar y sirve de
reconocimiento a los estudiantes que han completado los requisitos académicos de un plan
de estudios y, por lo tanto, se han hecho merecedores del título académico.
Para organizar una fiesta de graduación del instituto se compran 9 cajas de refrescos,
donde cada caja contiene 24 latas de refrescos. Invitamos a 56 personas y queremos que
todas y cada una de ellas consuman la misma cantidad de refrescos ¿Cuántas latas de
refresco sobrarán?"""

cajas = 9 - 2
latasXcaja = 24
personas = 56

total_latas = latasXcaja * cajas
reparto = int(total_latas / personas)
print(f'Sobran dos cajas (48 latas de refresco), asi cada persona tomaria {reparto} refrescos\n')

## Ejercicio 4: ¿Ves algún error en el precio?
"""El precio del producto Pernil Iberic D'Engreix Llen. Azuaga en porción de 100 gramos
cuesta 5,95€ y el vendedor nos muestra que el precio por kilo cuesta 29,75€. ¿Crees que
es correcto el precio?
En este reto tienes que hacer un programa que calcule correctamente el precio por kilo
del producto."""

gramos = 100
kilos = gramos / 1000
valor = 5.95

precio_kilo = 29.75

valor_real_k = valor * 10
print(f'Es incorrecto el valor que da el vendedor por kilo, ya que la conversion de {gramos}g a kilos, da {kilos}k\nSi los multiplicamos por 10 nos da 1 kilo, asi que el precio de este se debe multiplicar por 10 para saber si realmente dan {precio_kilo}€.\nPero este valor es incorrecto, ya que un kilo cuesta {valor_real_k}€')


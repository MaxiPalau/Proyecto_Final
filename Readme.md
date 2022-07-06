# Proyecto Final

## Profesor
* Luca Cittá Giordano

## Tutor
* Juan Valle

## Integrantes
- Martin Quesada
- Mauro De Carli Montenegro
- Maximiliano Palau

## Video
Haga click [aquí](https://drive.google.com/file/d/1XvPVvoYHo4451S2TqjYxrWMId-PShUUN/view?usp=sharing)

## Aplicación
### Productos
En el apartado de productos se listan todos los elementos que se encuentran en la base de datos con sus atributos.  
A los productos nuevos y que tienen descuento se les agrega una etiqueta para diferenciarlos.  
La funcionalidad del botón comprar no se encuentra desarrollada aún, por el momento cumple la función de ayuda visual para cuando un producto se encuentra sin stock, además de tener una etiqueta que lo indica, el botón comprar no estaría visible.

## Modelos
La carga de productos, marcas, distribuidores y las marcas que son trabajadas por cada distribuidor se realiza a través de formularios que son accedidos por medio de la lista desplegable “Administración” para cada caso particular.  

### Marcas
La carga de las marcas se lleva a cabo completando los siguientes campos, salvo que se especifique lo contrario son todos obligatorios:
- nombre: nombre de la marca, no se puede repetir
- descripción: descripción de la marca, puede estar en blanco

### Tipos (categorías)
La carga de los tipos de productos se lleva a cabo completando los siguientes campos, salvo que se especifique lo contrario son todos obligatorios:
- categoría: especificar la categoría a la que pertenece el producto, por ejemplo herramientas manuales, no se puede repetir
- descripción:  descripción de la marca, puede estar en blanco

### Productos
La carga de productos se lleva a cabo completando los siguientes campos, salvo que se especifique lo contrario son todos obligatorios:
- nombre: carácter
- sku: carácter, no puede ser igual al de otro producto
- marca: seleccionar de la lista previamente cargada
- modelo: carácter
- tipo: seleccionar de la lista previamente cargada
- precio: especificar el precio con números enteros o decimales
- stock: cantidad del producto, solo enteros
- descuento: porcentaje de descuento a aplicar, solamente especificar el número
- novedad: Seleccionar si el producto es nuevo
- imagen: nombre del archivo de imagen
- descripción: descripción del producto, puede estar vacío

### Distribuidores
La carga de distribuidores se lleva a cabo completando los siguientes campos, salvo que se especifique lo contrario son todos obligatorios:
- razon_social: nombre del distribuidor
- dirección: especificar la dirección
- localidad: especificar la localidad
- país: especificar el país
- teléfono: puede ser con números o caracteres
- mail: especificar el mail
- web: especificar la web
- cuit: ingresar solo números (sin guiones), no se puede repetir
- descripción: especificar una descripción, puede estar en blanco

### Distribuidores por marca
La carga de distribuidores por marca se lleva a cabo completando los siguientes campos, salvo que se especifique lo contrario son todos obligatorios:
- marca = seleccionar la marca de la lista
- distribuidor = seleccionar el distribuidor de la lista

## Búsqueda
Se ingresa el texto a buscar en  el campo

## Usuarios con permisos de administración
Para que un usuario creado desde la página de registro o desde el administrador de Django pueda hacer CRUD de productos, marcas, categorías, distribuidores, luego de generado se debe editar el usuario desde el panel de administración de Django y  se le debe asignar el grupo "Ferreteria", caso contrario no tendrá acceso a las funcionalidades antes mencionadas.

## Notas finales
### Usuario de prueba
- Usuario: admin  
- Contraseña: admin

### Archivo .gitignore
Decidimos quitar del archivo .gitignore la carpeta media y la base de datos con la finalidad que se vea el sitio completamente funcional.  
Hay una validación que se hace en función a un grupo creado dentro del panel de administración de Django que no funcionaría de no tener la basae de datos que utilizamos cargando datos.  
Entendemos que en un ambiente productivo estos archivos no se deben  compartir en github.
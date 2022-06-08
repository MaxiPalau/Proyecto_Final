# Modelos
### Marcas
Este modelo almacena los datos de las diferentes marcas. Los campos que contiene son:
- nombre: CharField, length 100, unique
- descripcion: CharField, length 200, blank, default ''

### Tipo
Este modelo almacena los diferentes tipos de herramientas. Los campos que contiene son:
- categoria: CharField, length 100, unique
- descripcion: CharField, length 200, blank, default ''

### Productos
Almacena los diferentes productos con referencias a los modelos Marcas y Tipo. Los campos que contiene son:
- nombre: CharField, length 200
- sku: CharField, length 100, unique
- marca: ForeignKey, Marcas
- modelo: CharField, length 100
- tipo: ForeignKey, Tipo
- precio: FloatField
- stock: IntegerField
- descuento: FloatField
- novedad: BooleanField    
- imagen: CharField, length 100
- descripcion: CharField, length 200, blank, default ''

### Distribuidores
Almacena los datos de los distribuidores. Los campos que contiene son:
- razon_social: CharField, length 200
- direccion: CharField, length 100
- localidad: CharField, length 100
- pais: CharField, length 100
- telefono: CharField, length 100
- mail: CharField, length 100
- web: CharField, length 100
- cuit: IntegerField, unique
- descripcion: CharField, length 200, blank, default ''

### Distribuidores_Marcas
Con este modelo se relacionan los modelos Marcas y Distribuidores
- marca = ForeignKey, Marcas
- distribuidor = ForeignKey, Distribuidores
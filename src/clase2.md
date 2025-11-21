# 🧱 Clase 2 – Continuando con el blog

En esta segunda clase hemos creado un model manager, vistas para list y detail, la estructura de templates y la base.html y list.html templates.

Además le hemos añadido unos estilos a nuestro blog.

---

## ⚙️ Comandos utilizados

```bash

# Interactuar con los modelos desde la línea de comandos
python manage.py shell

>>> from django.contrib.auth.models import User
>>> from blog.models import Post

---
>>> user = User.objects.get(username='admin')

# Recupermos el objeto de usuario con el nombre de usuario admin
# El método get() permite recuperar un solo objeto de la base de datos. 
# Este método ejecuta una sentencia SQL SELECT en segundo plano. 
# Este método espera un resultado que coincida con la consulta. 
# Si la base de datos no devuelve ningún resultado, se generará una excepción DoesNotExist y, 
# si la base de datos devuelve más de un resultado, generará una excepción MultipleObjectsReturned.
---
---
>>> post = Post(title='Otro post',
...slug='otro-post',
...body='Este es otro post.',
...author=user)

# Este objeto está en la memoria y no se almacena en la base de datos; 
# creamos un objeto Python que se puede usar durante el tiempo de ejecución, pero no se guarda en la base de datos.
---
---
>>> post.save()

# Guardamos el objeto Post en la base de datos usando el método save().
# Esta acción ejecuta una sentencia SQL INSERT en segundo plano.
# Primero hemos creado un objeto en memoria y luego lo hemos almacenado en la base de datos.

```
---

```bash
# También podemos crear el objeto y almacenarlo en la base de datos en una sola operación usando el método create()

>>> Post.objects.create(title='One more post',
slug='one-more-post',
body='Post body.',
author=user)

# El método get_or_create() facilita esto, recupera un objeto de la base de datos o lo crea si no se encuentra.
# Este método devuelve una tupla con el objeto recuperado y un valor booleano que indica si se creó un nuevo objeto.

>>> user, created = User.objects.get_or_create(username='user2')

# Actualizamos un campo con:
>>> post.title = 'Nuevo título'

```

---

```bash

# Cada modelo de Django tiene al menos un administrador, y el administrador predeterminado se llama objects. 
# Obtenemos un objeto QuerySet usando el administrador de modelos.

>>> all_posts = Post.objects.all()

# Los QuerySets de Django son perezosos(lazy), lo que significa que solo se evalúan cuando se les fuerza a hacerlo.

>>> Post.objects.all()

# Para filtrar un QuerySet, puede usar el método filter() del administrador. 
# Este método permite especificar el contenido de una cláusula WHERE de SQL mediante búsquedas de campo.

>>> Post.objects.filter(title='Qué es la recursión y cuándo usarla')
>>> post = Post.objects.filter(title='Qué es la recursión y cuándo usarla')
>>> print(post.query)

# La búsqueda produce una coincidencia exacta

>>> Post.objects.filter(id__exact=1)
>>> Post.objects.filter(id=1)

# Podemos generar una búsqueda que no distinga entre mayúsculas y minúsculas con iexact

>>> Post.objects.filter(title__iexact='comprendiendo los principios solid')

# La búsqueda "contains" se traduce a una búsqueda SQL utilizando el operador LIKE:

>>> Post.objects.filter(title__contains='Python')
>>> Post.objects.filter(title__icontains='Python')

# Podemos buscar un iterable determinado (una lista, una tupla u otro objeto QuerySet) con la búsqueda in

>>> Post.objects.filter(id__in=[1, 3])

# Muestra la búsqueda mayor que (gt)

>>> Post.objects.filter(id__gt=3)

# Muestra la búsqueda mayor o igual que (gte)

>>> Post.objects.filter(id__gte=3)

# Muestra la búsqueda menor que (lt)

>>> Post.objects.filter(id__lt=3)

# Muestra la búsqueda menor o igual que (lte)

>>> Post.objects.filter(id__lte=3)

# Realiza una búsqueda "inicia con" que distinga entre mayúsculas y minúsculas.

>>> Post.objects.filter(title__istartswith='Qué')

# Realiza una búsqueda "acaba con" que distinga entre mayúsculas y minúsculas.

>>> Post.objects.filter(title__iendswith='Python')

# Podemos encadenar búsquedas adicionales para los campos relacionados

>>> Post.objects.filter(publish__year=2025, author__username='root')

>>> Post.objects.filter(publish__year=2025).filter(author__username='root')

# Utilizando el método exclude() del administrador excluímos ciertos resultados de su QuerySet.

>>> Post.objects.filter(publish__year=2025).exclude(title__startswith='Qué')

# El orden predeterminado se define en la opción de ordenación de la metadatos del modelo. 
# Podemos anular el orden predeterminado mediante el método order_by() del administrador.

>>> Post.objects.order_by('title')

# Ordenar en orden descendiente

>>> Post.objects.order_by('-title')

# Ordenar por varios campos

>>> Post.objects.order_by('publish','title')

# Ordenar con orden aleatorio

>>> Post.objects.order_by('?')

```
---

```bash

# Podemos limitar un QuerySet a una cierta cantidad de resultados usando los subconjuntos de segmentación de matrices de Python.

>>> Post.objects.all()[:3]

>>> Post.objects.all()[2:4] # A partir del 2 hasta el 4

# Podemos obtener un índice en concreto

>>> Post.objects.all()[1]

# Podemos encadenar opciones de extracción

>>> Post.objects.order_by('?')[0]

``` 

---

```bash

# El método count() cuenta el número total de objetos que coinciden con el QuerySet y devuelve un entero. 
# Este método se traduce en una instrucción SQL SELECT COUNT(*).

>>> Post.objects.filter(id__lt=3).count()

>>> Post.objects.filter(id__gt=3).count()

>>> Post.objects.all().count()

# El método exists() permite comprobar si un QuerySet contiene resultados. 
# Este método devuelve True si el QuerySet contiene elementos y False en caso contrario.

>>> Post.objects.filter(title__startswith='Qué').exists()

# Para eliminar un objeto, podemos hacerlo desde una instancia de objeto mediante el método delete()
# al eliminar objetos también se eliminarán las relaciones de dependencia de los objetos ForeignKey definidos con on_delete establecido en CASCADE.

>>> post = Post.objects.get(id=1)
>>> post.delete()

``` 

```bash

# Si necesitamosa crear consultas más complejas, como consultas con sentencias OR, podemos usar objetos Q.
# Un objeto Q permite encapsular una colección de búsquedas de campos. 
# Podemos crear sentencias combinando objetos Q con los operadores & (y), | (o) y ^ (xor)

>>> from django.db.models import Q
>>> start_que = Q(title__startswith='Qué')
>>> start_estructuras = Q(title__startswith='Estructuras')
>>> Post.objects.filter(start_que | start_estructuras)

>>> Post.objects.filter(Q(title__startswith='Qué') | Q(title__startswith='Estructuras'))

``` 


## 📘 Commits realizados

| Commit    | Descripción   |
|:----------| :-------------|
| `104b6a4` | (HEAD -> clase2) Añadiendo algo de estilos|
| `94cf99f` | Creando list.html template |
| `fc8edde` | Creando base.html template |
| `066bf2b` | Creando la estructura de templates de la app |
| `992356e` | Construyendo las vistas de list y detail |
| `3fd8f0b` | Creando model managers |

---

## 🧩 Resultado al final de la clase

- Posts creados.
- Añadido modelo al panel de administración.
- Creación de vistas y templates.
- Dando primeros estilos al blog.

---
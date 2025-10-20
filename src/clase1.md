# 🧱 Clase 1 – Inicio del Proyecto Django

En esta primera clase hemos creado el proyecto base con **Django**, la aplicación inicial (`blog`), configurado los modelos y el panel de administración.  
También realizamos las primeras migraciones y la creación del superusuario para acceder al *admin*.

---

## ⚙️ Comandos utilizados

```bash
# Crear el proyecto principal
python -m django startproject mysite .

# Aplicar las migraciones
python manage.py migrate

# Ejecutar el servidor de desarrollo
python manage.py runserver 0.0.0.0:8000

# Crear la aplicación 'blog'
python manage.py startapp blog

# Crear las migraciones iniciales
python manage.py makemigrations blog

# Crear el superusuario para acceder al panel de administración
python manage.py createsuperuser

```

## Registrar la aplicación en settings.py
### (añadiendo 'blog' a la lista INSTALLED_APPS)

---

## 📘 Commits realizados

| Commit | Descripción |
|:-------|:-------------|
| `474abfb` | Añadiendo facet counts |
| `34cd067` | Añadiendo modelos al panel de administración |
| `fead2e2` | Creando y aplicando migraciones |
| `4bb7e40` | Añadiendo campo relación con author |
| `0765be2` | Añadiendo campo Status al Post |
| `aa891fb` | Activando la aplicación en settings.py |
| `d6689c6` | Añadiendo campos a la clase Post |
| `f7fba56` | Creación de proyecto y primera app (blog) |
| `2d0c596` | Commit inicial |

---

## 🧩 Resultado al final de la clase

- Proyecto Django inicializado y funcionando.
- Aplicación `blog` creada y registrada.
- Modelo `Post` definido con sus campos (incluyendo `author` y `status`).
- App registrada en `settings.py`.
- Migraciones realizadas correctamente.
- Modelo disponible en el panel de administración.
- Superusuario creado para pruebas en el *admin site*.

---

-----

# 🚀 Django Starter Kit (Dev Container + Docker Compose)

**Django Starter Kit** es una plantilla base para crear proyectos **Django** rápidamente en un entorno de desarrollo **contenedorizado** con **Docker** y **Devcontainers** (VS Code). Te permite empezar a codificar en segundos sin instalaciones locales de Python, entornos virtuales o conflictos de sistema.

-----

## ⚙️ Características principales

  - **Python 3.13** y **Django 5.2.7**
  - **SQLite** como base de datos por defecto (sin configuración adicional)
  - **Docker** y **Devcontainers** para un entorno reproducible en cualquier máquina.
  - **Bind mount** del código fuente local (`src/`) dentro del contenedor.
  - Estructura limpia y minimalista, ideal para empezar nuevos proyectos.
  - **Configuración automática** del entorno de trabajo (archivos `.env`, directorio de trabajo, etc.).

-----

## 🛠️ Requisitos previos

Antes de usar esta plantilla asegúrate de tener instalado:

  - [Docker Desktop](https://www.docker.com/products/docker-desktop) (o Docker Engine)
  - [Visual Studio Code](https://code.visualstudio.com/)
  - Extensión de VS Code: **[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)**

-----

## 💻 Inicio Rápido (Getting Started)

### 1\. Crea y Clona el Repositorio

1.  Crea un nuevo repositorio a partir de esta plantilla usando el botón **`Use this template`** en GitHub (no uses `git clone`).

2.  **Clona** tu nuevo repositorio localmente:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio nombre-de-tu-proyecto
    cd nombre-de-tu-proyecto
    ```

### 2\. Abre el Entorno de Desarrollo

1.  Abre la carpeta del proyecto en VS Code.
2.  Cuando VS Code pregunte: **"Folder contains Dev Container configuration. Reopen in Container?"**, selecciona **"Reopen in Container"** (o usa `Ctrl+Shift+P` / `Cmd+Shift+P` y selecciona **"Dev Containers: Reopen in Container"**).
    *(La primera vez, el entorno tardará unos minutos en construirse.)*

> 💡 **¡Entorno Listo\!** La terminal se abrirá directamente en la carpeta **`src/`** y el archivo `.env` se habrá creado automáticamente a partir de `.env.example`.

-----

## 🚀 Primeros Comandos y Desarrollo

La terminal ya está en el directorio de código (`/workspace/src/`).

### 1\. Configuración Inicial del Proyecto

Utiliza el punto (`.`) para crear la estructura de tu proyecto Django directamente en la carpeta `src/`:

```bash
# La terminal está en src/
python -m django startproject nombre_proyecto .
```

### 2\. Arrancar el Servidor

Ejecuta las migraciones iniciales y arranca el servidor:

```bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Accede a tu aplicación en `http://localhost:8000/`.

-----

## 💾 Git y Control de Versiones

Para realizar `commit` y `push`, debes trabajar desde la raíz del repositorio (`/workspace`), donde se encuentra el directorio **`.git`**.

### Opción A: Usar el Panel de VS Code (Recomendado)

Utiliza el panel de **Control de Código Fuente** (el icono de la bifurcación) de VS Code. El IDE gestionará automáticamente la ubicación del `.git` por ti. Simplemente:

1.  Escribe tu mensaje de *commit*.
2.  Haz clic en **Commit** y luego en **Sync Changes** (o **Push**).

### Opción B: Usar la Terminal

Si prefieres la terminal, sal del directorio `src/` antes de ejecutar comandos Git:

```bash
# 1. Sal del directorio de código
cd .. 

# 2. Ahora estás en /workspace. Ejecuta tus comandos Git:
git status
git add .
git commit -m "feat: Proyecto inicial de Django y estructura base"
git push
```

-----

## Consejos

  - **Dependencias:** Para añadir librerías, edita el archivo **`requirements.txt`** y reconstruye el contenedor (`F1` -\> **"Dev Containers: Rebuild Container"**) para instalar las nuevas dependencias.
  - **Base de Datos:** Puedes cambiar fácilmente a PostgreSQL o MySQL modificando el `docker-compose.dev.yml`.
  - **Uso:** Este entorno está optimizado para **desarrollo y aprendizaje**, no para producción.

-----


## 🔐 Configuración de Autenticación con SSH (Recomendado)

Para interactuar con GitHub de forma segura sin problemas de contraseña, generaremos la clave SSH directamente dentro del Dev Container.

1. Generar la Clave SSH Dentro del Contenedor 🛠️

    Ejecuta el siguiente comando dentro de la terminal del Dev Container:

    Abre la terminal del Dev Container (Asegúrate de que Git y openssh-client estén instalados en el Dockerfile).

    Ejecuta el siguiente comando, sustituyendo el email por el de tu cuenta de GitHub (o el de noreply):

```bash
ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"
```

    Te pedirá dos cosas:

  ```"Enter a file in which to save the key"```: Simplemente presiona ```Enter``` para usar la ubicación por defecto (/root/.ssh/id_ed25519).

  ```"Enter passphrase"```: Introduce una contraseña segura (es opcional, pero recomendada).

2. Añadir la Clave SSH a tu Cuenta de GitHub 🔑
    La clave pública (id_ed25519.pub) debe ser copiada desde el contenedor y registrada en GitHub.

    Copia la Clave Pública desde el Contenedor:

    Ejecuta en la terminal del Dev Container para mostrar el contenido:

```bash
cat /root/.ssh/id_ed25519.pub
```

  Copia todo el contenido que se muestra en la terminal (comienza con ssh-ed25519...).

  Navega a GitHub:

  Ve a ```Settings > SSH and GPG keys```.

  Haz clic en ```New SSH key```.

  Pega la Clave:

  En Title, pon un nombre descriptivo (ej: DevContainer-Blog-Project).

  En Key, pega el contenido copiado de la terminal.

  Haz clic en ```Add SSH key```.

### 3 Cambiar la URL del Repositorio (En el Contenedor)

Finalmente, dentro de la terminal del Dev Container, debes cambiar el protocolo de comunicación de Git.

1.  Abre la terminal del Dev Container y navega a la raíz (`/workspace`).

2.  **Cambia la URL de `origin` a SSH:**

    ```bash
    cd /workspace
    git remote set-url origin git@github.com:tu_email@ejemplo.com/tu_repositorio.git
    ```

A partir de ahora, cualquier comando de Git (`pull`, `push`, `fetch`) funcionará sin problemas de contraseña, ya que VS Code reenviará tu clave SSH privada para la autenticación.

## Licencia

MIT License © 2025

#### Desarrollado como entorno base para cursos y proyectos de aprendizaje con Django + Docker.
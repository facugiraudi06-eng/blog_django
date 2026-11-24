# Blog Django

Proyecto base de un blog web hecho con Django.

## Descripción
El sitio tiene dos páginas, Inicio y Acerca de, con templates HTML,
navegación y estilos CSS. Todavía no tiene modelos propios.

## Instalación
1. Clonar el repositorio:

        git clone ( URl del repositorio )
        cd ( Nombre del repositorio )

2. Crear y activar el entorno virtual:

        python -m venv venv
        .\venv\Scripts\Activate.ps1      (Windows PowerShell)
        source venv/bin/activate         (Linux o macOS)

3. Instalar dependencias:

        pip install -r requirements.txt

4. Levantar el servidor:

        python manage.py runserver

5. Abrir en el navegador: http://127.0.0.1:8000/

## Aplicaciones
- posts: aplicación inicial para las publicaciones del blog.

## Base de datos y administración

Aplicar las migraciones:
python manage.py migrate

Crear un administrador:
python manage.py createsuperuser

Iniciar el servidor:
python manage.py runserver

Entrar a http://127.0.0.1:8000/admin/ con el usuario creado
para agregar publicaciones.

La página de inicio muestra únicamente los posts publicados,
ordenados del más reciente al más antiguo.

## CRUD de publicaciones e imágenes

El sitio permite crear, ver, editar y eliminar publicaciones.
La eliminación requiere confirmación. El inicio muestra solamente
los posts publicados, ordenados del más reciente al más antiguo.

Los formularios usan PostForm, basado en el modelo Post.
Cada publicación puede tener una imagen opcional.

Se instaló Pillow para trabajar con imágenes.
Los archivos se guardan en media/posts/ mediante esta configuración:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

Las rutas del proyecto permiten mostrar las imágenes durante
el desarrollo.

### Ejecutar el proyecto

Con el entorno virtual activado:

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Probar el CRUD

1. Abrir http://127.0.0.1:8000/
2. Elegir Crear publicación y completar el formulario.
3. Seleccionar el estado Publicado y adjuntar una imagen JPG o PNG.
4. Guardar y comprobar que la imagen aparezca en el detalle.
5. Elegir Editar para modificar los datos o cambiar la imagen.
6. Crear otra publicación sin imagen para comprobar que es opcional.
7. Elegir Eliminar: Cancelar conserva el post y Sí, eliminar lo borra.

Las publicaciones y las imágenes cargadas se conservan localmente.

## Usuarios y perfiles

La app accounts gestiona el registro, el inicio y el cierre de sesión.

Para crear las tablas necesarias:
python manage.py migrate

Para iniciar el servidor:
python manage.py runserver

### Uso

1. Elegir Registrarse para crear una cuenta.
2. Iniciar sesión con el usuario y la contraseña elegidos.
3. Entrar a Mi perfil para ver los datos personales.
4. Usar Editar perfil para modificar biografía, enlace web y avatar.
5. Usar Cerrar sesión para salir.

El modelo Perfil está relacionado con User mediante OneToOneField.
El perfil se crea desde la vista de registro, sin signals.
Para usuarios anteriores, se crea con get_or_create al acceder al perfil.

El avatar es opcional y se guarda en media/avatares/.
Su carga utiliza Pillow, request.FILES y un formulario multipart.

Crear, editar y eliminar posts requieren iniciar sesión mediante
@login_required. Ver y editar el perfil también requieren autenticación.
El listado y el detalle de publicaciones siguen siendo públicos.

El menú muestra opciones diferentes según si el usuario inició sesión.
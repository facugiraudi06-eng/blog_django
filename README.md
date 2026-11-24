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
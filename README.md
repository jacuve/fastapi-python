# Proyecto para gestionar tareas.

## Configuracion

- creamos un entorno virtual
  python3 -m venv fastapi-env

- activamos
  source fastapi-env/bin/activate

- instalamos fastapi(framework api)
  pip install fastapi

- instalamos uvicorn (servidor web)
  pip install uvicorn

- Para usar una base de datos Postgresql, 
  usamos docker, que está definido en el fichero docker-compose.yaml

- Para usar base de datos, instalar sqlalchemy
  pip install sqlalchemy

- Para usar Postgresql
  pip install psycopg2-binary

## Ejecución

- Activar entorno virutal : 
  source fastapi-env/bin/activate

- Levantar Docker : 
  docker compose up -d

- Arrancamos y se queda en escucha
  uvicorn main:app --reload

- Para ejecutar y probar toda la API: 
  http://localhost:8000/docs

Para usar esto, es necesario python3

creamos un entorno virtual
python3 -m venv fastapi-env

activamos
source fastapi-env/bin/activate

instalamos fastapi(framework api)
pip install fastapi

instalamos uvicorn (servidor web)
pip install uvicorn

arrancamos y se queda en escucha
uvicorn main:app --reload

Para ejecutar y probar toda la API: :/var/lib/pos

http://localhost:8000/docs


Para usar una base de datos Postgresql, 
usamos docker, que está definido en el fichero docker-compose.yaml

Para levantar docker:
docker-compose up -d

Para usar base de datos, instalar sqlalchemy
pip install sqlalchemy

Para usar Postgresql
pip install psycopg2-binary

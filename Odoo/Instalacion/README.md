# Instalacion de contenedores de docker 


### 1. Descargar los archivos proporcionados y almacenarlos.

```bash
.
├── Archivo1
│   ├── docker-compose.yml
│   ├── prod
│   │   └── addons
│   └── volumesOdoo
│       ├── addons
│       └── odoo
│           ├── filestore
│           └── sessions
├── Archivo2
│   ├── dev
│   │   └── addons
│   └── docker-compose.yml
```

### 2. Despues ejecutas en cada una de las carpetas el comando para iniciar y crear el contenedor.

```bash
docker compose up -d
```

<img src="./images/1.png" align="center"/>
<img src="./images/2.png" align="center"/>


### 3. Entras al puerto de cada uno de los contenedores en este caso 8070 y 8069.


#### Puerto 8069
<img src="./images/3.png" align="center"/>


#### Puerto 8070

<img src="./images/4.png" align="center"/>


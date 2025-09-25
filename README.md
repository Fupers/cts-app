# San Valentín APP CTS Test

python 3.12.3
django 5.2.6
djangorestframework 3.16.1
celery 5.5.3
redis 6.4.0
tailwindcss 3.4.0
djangorestframework-simplejwt 5.5.1
itsdangerous 2.2.0

### Descripción
Este trabajo se realizó mediante un sistema Linux (Ubuntu), donde las explicaciones principales seran en base a un sistema WSL2

## CTS App - Deployment

Este README explica cómo desplegar la aplicación CTS App usando docker-compose en Windows (WSL2) y Linux.

#### Respositorio Git
Descargar archivos de repositorio en github
```
git clone https://github.com/Fupers/cts-app.git
```

#### Prerrequisitos
##### Para Linux:

- Docker: Instalación
- Docker Compose: Instalación
- Git

##### Para Windows (con WSL2):

- Docker Desktop para Windows Descargar
- WSL2 activado
- Distribución Linux instalada (Ubuntu 20.04 o 24.04 recomendado)
- Git

Activar integración de Docker con tu distro WSL2 desde Docker Desktop: Settings → Resources → WSL Integration → Enable

##### Estructura del proyecto
```
cts-app/
├─ backend/                     # Archivo backend usando Django + Celeris
├─ frontend/                    # Archivo frontend con Vuejs
├─ docker-compose.yml           # Docker para desplegar app
├─ Dockerfile.frontend
├─ Dockerfile.backend
├─ requirements.txt
└─ .env                         # Clave para mandar correo con Sendgrid (Crear)
```

- backend/ → Django + Celery + Redis
- frontend/ → Vue 3 + Vite
- docker-compose.yml → Orquesta todos los contenedores
- .env → Variables de entorno (SendGrid API key)

#### Configurar variables de entorno

Crea un archivo .env en la raíz:

##### SendGrid
clave estará en el correo
```
SENDGRID_API_KEY=tu_sendgrid_api_key
```

### Docker Compose

Construir y levantar los contenedores
##### En Linux:
```
cd cts-app
docker-compose up --build
```

##### En Windows con WSL2:

Abre tu distro WSL (ej: Ubuntu)

Ve a la carpeta del proyecto
```
cd ~/home/cts-app
docker-compose up --build
```

##### Acceder a la app

- Frontend Vue: http://localhost:5173
- Backend Django API: http://localhost:5050

##### Usuario Admin
```
Usuario: admin
Contraseña: Admin123
```
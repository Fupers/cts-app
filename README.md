# San Valentín APP CTS Test

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
## Técnicas Tomadas

- Django + DRF: Se eligió Django con Django REST Framework para manejar la API porque facilita la gestión de modelos, serialización y autenticación de usuarios.

- Vue 3 + Pinia: Se usa Vue 3 para el frontend por su reactividad y facilidad de componentes, y Pinia para el manejo del estado global de forma más sencilla que Vuex.

- Docker + Docker Compose: Para aislar servicios y garantizar que Django, Vue y Redis/Celery corran en contenedores independientes sin conflictos de dependencias ni puertos.

- JWT con Simple JWT: Se eligió JWT para autenticar administradores y proteger los endpoints privados, manteniendo la API REST sin sesiones.

- Celery + Redis: Se usa Celery para enviar correos en segundo plano y Redis como broker, evitando que la UI se bloquee mientras se envían emails.

- Rutas públicas y privadas: Se definieron rutas públicas para registro y verificación de concursantes, y rutas protegidas (con token) para administradores, para mantener seguridad.

- Verificación de usuario post contraseña para evitar validaciones sin registro completo.

## Endpoints

1. ###### Registro de concursantes

- URL: /api/contest/register/
- Método: POST
- Permisos: Público (AllowAny)

```
Request
  {
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "phone": "+56912345678"
  }
```

```
Response (201 Created)
  {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "phone": "+56912345678",
    "is_verified": false,
    "created_at": "2025-09-25T11:20:00Z"
  }
```

2. ###### Verificación de cuenta

- URL: /api/contest/verify/
- Método: POST
- Permisos: Público (AllowAny)

```
Request
  {
    "token": "abc123xyz",
    "password": "nuevo_password"
  }
```

```
Response (200 OK)
  {
    "message": "Cuenta activada correctamente"
  }
```

3. ######  Login de administrador

- URL: /api/admin/login/
- Método: POST
- Permisos: Público (AllowAny)

```
Request
  {
    "username": "admin",
    "password": "admin123"
  }
```

```
Response (200 OK)
  {
    "refresh": "jwt-refresh-token",
    "access": "jwt-access-token"
  }
```

4. ###### Listado de concursantes (solo admin)

- URL: /api/admin/contest/
- Método: GET
- Permisos: IsAdminUser

```
Response (200 OK)
  [
    {
      "id": 1,
      "name": "Usuario1",
      "email": "usuario1@test.com",
      "phone": "+56911111111",
      "is_verified": true,
      "created_at": "2025-09-25T11:20:00Z"
    },
    {
      "id": 2,
      "name": "Usuario2",
      "email": "usuario2@test.com",
      "phone": "+56911111112",
      "is_verified": false,
      "created_at": "2025-09-25T11:30:00Z"
    }
  ]
```

5. ###### Sorteo de ganador (solo admin)

- URL: /api/admin/draw_winner/
- Método: POST
- Permisos: IsAdminUser

```
Response (200 OK)
  {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com"
  } 
```

6. ###### Notificación de ganador (solo admin)

- URL: /api/admin/notify_winner/
- Método: POST
- Permisos: IsAdminUser

```
Request
  {
    "winner_id": 1
  }
```

```
Response (200 OK)
  {
    "message": "Correo enviado a juan@example.com"
  }
```

### Versiones de tecnologías

Las versiones usadas de códigos o tecnologías mas importantes.

- python 3.12.3
- django 5.2.6
- djangorestframework 3.16.1
- celery 5.5.3
- redis 6.4.0
- tailwindcss 3.4.0
- djangorestframework-simplejwt 5.5.1
- vue 3.5.18
- node 20.19.0
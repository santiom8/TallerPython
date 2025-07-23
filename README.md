# Library API (In-Memory)

## 📋 Descripción  
API REST para gestionar una colección de libros en memoria, sin persistencia en base de datos.  
Permite listar, crear, eliminar y transformar recursos (páginas y estado “vendido”).

---

## ⚙️ Requisitos del sistema  
- **Python 3.8+**  
- **pip**  
- **Git** (para clonar el repositorio)  
- Windows / macOS / Linux  

> Se recomienda usar un entorno virtual (`venv`).

---

## 🔧 Instalación y arranque

1. **Clonar repositorio**  
   ```bash
   git clone https://github.com/santiom8/TallerPython.git api
   cd api
   ```

2. **Crear y activar entorno virtual**  
   - **Windows (PowerShell)**  
     ```powershell
     python -m venv .venv
     . .\.venv\Scripts\Activate.ps1
     ```   
   - **Linux/macOS**  
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instalar dependencias**  
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Arrancar el servidor**  
   ```bash
   python -m uvicorn app.main:app --reload
   ```
   - **URL base:** `http://127.0.0.1:8000`

---

## 📖 Documentación Swagger / OpenAPI

- **Swagger UI**:  
  `http://127.0.0.1:8000/docs`  
- **ReDoc**:  
  `http://127.0.0.1:8000/redoc`  
- **Esquema OpenAPI (JSON)**:  
  `http://127.0.0.1:8000/openapi.json`
<img width="1194" height="687" alt="image" src="https://github.com/user-attachments/assets/3afaa0ff-b174-4447-a727-6628cf4a5f14" />

---

## 🎯 Casos de uso y endpoints

| Caso                        | Método  | Ruta                                  | Descripción                                               |
|-----------------------------|---------|---------------------------------------|-----------------------------------------------------------|
| 1. Listar todos los libros  | `GET`   | `/books`                              | Devuelve la lista completa de libros.                     |
| 2. Crear un libro           | `POST`  | `/books`                              | Añade un nuevo libro.                                     |
| 3. Eliminar un libro        | `DELETE`| `/books/{name}`                       | Elimina el libro identificado por `name`.                 |
| 4. Añadir páginas           | `PATCH` | `/books/{name}/pages?pages={n}`       | Suma `{n}` páginas al libro `name`.                       |
| 5. Marcar como vendido      | `PATCH` | `/books/{name}/sell`                  | Cambia `is_sold` a `true` para el libro `name`.           |

---

## 🔍 Detalle de las funcionalidades

### 1. `GET /books`  
- **Respuesta (200)**:  
  ```json
  [
    {
      "number": 1,
      "name": "peppa pig",
      "price": 100.0,
      "pages": 50,
      "author": "juan gabriel",
      "is_sold": false
    },
    { /* ... */ }
  ]
  ```

### 2. `POST /books`  
- **Request Body** (`application/json`):
  ```json
  {
    "number": 3,
    "name": "Libro X",
    "price": 150.0,
    "pages": 120,
    "author": "Autor Z"
  }
  ```
- **Respuesta (201)**:  
  Recurso creado idéntico al payload, más `is_sold: false`.

### 3. `DELETE /books/{name}`  
- **Parámetro**: `name` (string)  
- **Respuesta (204)**: cuerpo vacío.  
- **Error (404)**:  
  ```json
  { "detail": "Book not found" }
  ```

### 4. `PATCH /books/{name}/pages`  
- **Parámetro de ruta**: `name`  
- **Query param**: `pages` (int)  
- **Respuesta (200)**:  
  ```json
  {
    "number": 3,
    "name": "Libro X",
    "price": 150.0,
    "pages": 150,
    "author": "Autor Z",
    "is_sold": false
  }
  ```
- **Error (404)**:  
  ```json
  { "detail": "Book not found" }
  ```

### 5. `PATCH /books/{name}/sell`  
- **Parámetro**: `name`  
- **Respuesta (200)**:  
  ```json
  {
    "number": 3,
    "name": "Libro X",
    "price": 150.0,
    "pages": 150,
    "author": "Autor Z",
    "is_sold": true
  }
  ```
- **Error (404)**:  
  ```json
  { "detail": "Book not found" }
  ```

---

## 💻 Comandos cURL de prueba

1. **Listar libros**  
   ```bash
   curl -X GET http://127.0.0.1:8000/books
   ```

2. **Crear un libro**  
   ```bash
   curl -X POST http://127.0.0.1:8000/books \
     -H "Content-Type: application/json" \
     -d '{
       "number": 3,
       "name": "Libro X",
       "price": 150.0,
       "pages": 120,
       "author": "Autor Z"
     }'
   ```

3. **Listar tras crear**  
   ```bash
   curl -X GET http://127.0.0.1:8000/books
   ```

4. **Añadir páginas**  
   ```bash
   curl -X PATCH "http://127.0.0.1:8000/books/Libro%20X/pages?pages=30"
   ```

5. **Marcar como vendido**  
   ```bash
   curl -X PATCH http://127.0.0.1:8000/books/Libro%20X/sell
   ```

6. **Eliminar libro existente**  
   ```bash
   curl -X DELETE http://127.0.0.1:8000/books/Libro%20X
   ```

7. **Eliminar libro inexistente**  
   ```bash
   curl -X DELETE http://127.0.0.1:8000/books/NoExiste
   ```

8. **Añadir páginas a libro falso**  
   ```bash
   curl -X PATCH "http://127.0.0.1:8000/books/NoExiste/pages?pages=10"
   ```


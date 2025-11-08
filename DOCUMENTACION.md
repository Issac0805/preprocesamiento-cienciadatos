# DOCUMENTACIÓN DEL PROYECTO  
## Preprocesamiento de Datos - Cultura Digital y Sociedad  
### Nombre: Yoryhi Isaac Cadena Acosta  
### Unidad 2 - Tema 1  

---
## 1️. Descripción del proyecto
Este proyecto busca crear una serie de pasos simples para preparar datos antes de analizarlos, usando el lenguaje de programación Python y la herramienta llamada . Además, se usará Git y GitHub para guardar los cambios del proyecto de forma ordenada y segura.

---
## 2️. Estructura del repositorio
preprocesamiento-cienciadatos/

├── data/ 

├── docs/

│ . . .  └── evidencias/ 

│

├── .gitignore

├── DOCUMENTACION.md

├── preprocesamiento.py

└── README.md

---
## 3️. Funciones implementadas y comandos utilizados
### Funciones:
- `cargar_datos(ruta_archivo)` → Carga un dataset CSV.  
- `limpiar_datos(df)` → Elimina valores nulos y duplicados.  
- `normalizar_datos(df, columnas)` → Normaliza columnas numéricas entre 0 y 1.  
- `exportar_datos(df, ruta_salida)` → Exporta los datos procesados a un nuevo CSV.

### Comandos:
| Comando | ¿Qué hace? |
|---------|-----------|
|git config --global user.name "Tu Nombre" |Guarda nuestro nombre o el que pusimos en Git|
|git config --global user.email "yoryhicadena@gmail.com"| Guarda el correo asociado al repositorio|
|git init |Inicia un nuevo repositorio de Git en la carpeta|
|git clone URL |Descarga o clona un repositorio de GitHub al computador|
|git status |Muestra que archivos han cambiado o estan listos para subir|
|git add . |Prepara todos los archivos nuevos o modificados para el commit|
|git commit -m "mensaje" |Guarda una versión "commit" del proyecto con un mensaje|
|git branch |Muestra todas las ramas existentes|
|git checkout -b nombre-rama |Crea y cambia a una nueva rama|
|git merge nombre-rama |Une los cambios de otra rama con la rama principal que es main|
|git push origin main |Sube los cambios de la rama principal al repositorio de GitHub|
|git pull |Descarga los últimos cambios desde GitHub|

---
## 4️. Proceso de trabajo con Git y GitHub
1. Crear el proyecto en GitHub y hacer la configuración inicial, con los archivos importantes: (`.gitignore` y `README.md`)
2. Se crea la rama `feature/preprocesamiento`, donde se escribira el código para preparar los datos
3. Se agregan funciones poco a poco y se guarda cada cambio con una nota que explique qué se hiz es decir “commit”
4. Unir el nuevo trabajo "merge" de la rama `feature/preprocesamiento` en `main` 
5. Enviar todos los cambios al proyecto en GitHub, para que queden guardados

---
## 5️. Evidencias del proceso
1. Configuración del nombre y correo en Git ![Evidencia 0](docs/evidencias/0_configuracion_git.png)
2. Creación del repositorio y archivos iniciales (.gitignore, README.md) ![Evidencia 1](docs/evidencias/1_gitignore_y_readme.png)
3. Commit inicial y push a GitHub ![Evidencia 2](docs/evidencias/2_commit_inicial.png) 
4. Creación de la rama feature/preprocesamiento ![Evidencia 3](docs/evidencias/3_creacion_rama.png)
5. Commit con función preprocesamiento completo de datos ![Evidencia 4](docs/evidencias/4_commit_funcion_cargar_datos.png)
6. Commit con función limpiar_datos() ![Evidencia 5](docs/evidencias/5_commit_limpieza_datos.png)
7. Commit con función normalizar_datos() ![Evidencia 6](docs/evidencias/6_commit_normalizacion.png)
8. Commit con función exportar_datos() ![Evidencia 7](docs/evidencias/7_commit_exportar_datos.png)
9. Fusión y push final hacia main ![Evidencia 8](docs/evidencias/8_merge_y_push_main.png)
10. Configuración del workflow de GitHub Actions ![Evidencia 9](docs/evidencias/11_workflow_github_actions.png)
on: indica cuándo se ejecuta es decir cada que se hace push a main y jobs: define lo que hará el flujo, clona el repositorio, instala Python y pandas, luego verifica que el script preprocesamiento.py se ejecute sin errores de sintaxis.

11. Vista del repositorio en GitHub con todos los archivos subidos ![Evidencia 10](docs/evidencias/9_repositorio_github.png)
12. Visualización del código en GitHub ![Evidencia 11](docs/evidencias/10_codigo_en_github.png)
13. Pull Request y fusión en GitHub
Se realizó la simulación de una Pull Request desde la rama `feature/preprocesamiento` hacia la rama `main`, gitHub indicó que ambas ramas estaban sincronizadas a la fusión previa realizada desde la terminal con Git, esto afirma que los cambios fueron correctamente integrados en la rama principal.
![Evidencia 12](docs/evidencias/12_pull_request_simulada.png)
14. GitHub Actions, y ejecución del Workflow
Se configuró un flujo de trabajo automático en `.github/workflows/python-check.yml`, el flujo se ejecuta cada vez que se realiza un push o un pull request en la rama `main`, durante la primera ejecución hubo un error de configuración que se corrigió, validando el script `preprocesamiento.py` y asi mostrando la automatización CI/CD.
![Evidencia 16](docs/evidencias/16_github_actions_error.png)  
![Evidencia 17](docs/evidencias/17_github_actions_exitosa.png)
15. Eliminación de la rama feature/preprocesamiento tras la fusión | ![Evidencia 19](docs/evidencias/19_eliminar_rama_feature.png) |

---
## 6️. Enlace al repositorio en GitHub
[https://github.com/Issac0805/preprocesamiento-cienciadatos](https://github.com/Issac0805/preprocesamiento-cienciadatos)

---
## 7️. Conclusión
Este proyecto ayudó a practicar el uso de Git y GitHub y guardar los cambios del código de forma ordenada, también sirvió para aplicar pasos básicos para preparar los datos antes de analizarlos, también se siguió el proceso donde: se crearon líneas de trabajo (ramas), se guardaron cambios con notas (commits), se unieron los avances (merge), y se documento todo lo hecho con documentación.
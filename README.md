# PDF To Audio

**PDF To Audio** es una utilidad de consola completamente local que convierte archivos PDF a audio MP3.


## Características Principales
- **Extracción Profunda e Instantánea:** Utiliza el motor `PyMuPDF` (Fitz) para leer el contenido textual de documentos PDF.
- **Voz Neuronal Realista:** Aprovecha la síntesis de inteligencia artificial de Microsoft a través de la librería `edge-tts`, utilizando por defecto el modelo uruguayo `es-UY-ValentinaNeural` pero se puede modificar a gusto del consumidor.
- **Rapidez y Privacidad:** Al no depender de plataformas online, los documentos confidenciales e institucionales nunca salen del disco duro.
- **Feedback Visual Dinámico:** Incorpora en consola una barra gráfica de progreso que muestra el avance porcentual y de páginas en vivo del material generado.
- **Lectura Natural Fluida:** Aplica una limpieza inteligente (heurística) en cada página del PDF para evitar "pausas robóticas", uniendo palabras cortadas con guion e ignorando los saltos de línea visuales del documento original.

---

## Requisitos e Instalación

Dependencias clave:
- Python 3.9+
- `PyMuPDF`
- `edge-tts`

**Instalación Rápida:**
Abrir la consola en la carpeta del proyecto e instalar los paquetes ejecutando:
```bash
pip install -r requirements.txt
```

---

## Instrucciones de Uso

Para generar un audio MP3 a partir de un pdf:

**1. Comando Básico:**
Colocar el pdf en la carpeta del proyecto y, en la consola, ejecutar:
```bash
python convertir_pdf.py archivo_ejemplo.pdf
```
*Resultado:* Se creará en los siguientes segundos/minutos un archivo de audio llamado `archivo_ejemplo.mp3`.

**2. Guardar el MP3 con un nombre personalizado:**
Para elegir directamente cómo se va a llamar el archivo de sonido, se emplea el sufijo `-o`:
```bash
python convertir_pdf.py capitulo_biologia.pdf -o audio_para_alumnos.mp3
```

## A tener en cuenta
1. **Páginas Escaneadas:** El programa lee "texto incrustado". Si el documento que se intenta convertir es una foto o imagen escaneada pegada en un PDF (sin texto seleccionable), el programa avisará en ese caso se requerirán herramientas previas de reconocimiento óptico (OCR).
2. **Duración:** PDFs muy extensos crearán archivos MP3 largos y su tiempo de procesamiento aumentará.

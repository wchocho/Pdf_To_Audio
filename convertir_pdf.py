import sys
import asyncio
import argparse
import fitz  # PyMuPDF
import edge_tts

# Voz uruguaya 
VOZ_UY = "es-UY-ValentinaNeural"

async def pdf_a_audio(pdf_path, output_mp3):
    print(f" Abriendo PDF: {pdf_path}")
    
    try:
        with fitz.open(pdf_path) as doc:
            total_paginas = len(doc)
            print(f" El documento tiene {total_paginas} páginas.")
            print(f" Iniciando minería de crypto(shhh!!!), generación de audio y escritura en vivo a: {output_mp3}\n")
            
            paginas_validas = 0
            
            # Abrimos el archivo mp3 para ir "empujando" los fragmentos crudos en binario (wb)
            with open(output_mp3, "wb") as mp3_file:
                for index, pagina in enumerate(doc):
                    texto_pagina = pagina.get_text().strip()
                    
                    if texto_pagina:
                        paginas_validas += 1
                        
                        # Limpieza heurística anti-pausas robóticas:
                        texto_pagina = texto_pagina.replace("-\n", "")
                        texto_pagina = texto_pagina.replace("\n", " ")
                        texto_pagina = " ".join(texto_pagina.split())
                        
                        # Generar audio solo para esta página 
                        communicate = edge_tts.Communicate(texto_pagina, VOZ_UY, rate="+5%")
                        
                        async for chunk in communicate.stream():
                            if chunk["type"] == "audio":
                                mp3_file.write(chunk["data"])
                    
                    # Tremenda barra de progreso
                    porcentaje = int(((index + 1) / total_paginas) * 100)
                    barra = "█" * (porcentaje // 5) + "░" * (20 - (porcentaje // 5))
                    sys.stdout.write(f"\r  Progreso: [{barra}] {porcentaje}% (Página {index+1}/{total_paginas})")
                    sys.stdout.flush()
            
            print("\n")  # Salto de línea para limpiar la barra al terminar
            if paginas_validas == 0:
                print("El PDF parece estar vacío o compuesto exclusivamente por imágenes (requiere OCR).")
            else:
                print("Pronto! Audio guardado.")

    except Exception as e:
        print(f"\n Error procesando el documento: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convierte PDFs a formato Audio (MP3)")
    parser.add_argument("pdf", help="Ruta al archivo PDF que quieres leer.")
    parser.add_argument("-o", "--output", help="Ruta del archivo MP3 de salida (Opcional).", default=None)
    
    args = parser.parse_args()
    
    pdf_in = args.pdf
    mp3_out = args.output
    
    # Si no se pone nombre de salida, le da el mismo nombre que el PDF pero terminando en .mp3
    if not mp3_out:
        mp3_out = pdf_in.rsplit(".", 1)[0] + ".mp3"
        
    asyncio.run(pdf_a_audio(pdf_in, mp3_out))

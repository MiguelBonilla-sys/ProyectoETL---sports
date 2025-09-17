"""
Visualización de Datos Deportivos - Le Mans
==========================================
Script especializado para generar visualizaciones de los datos
ya procesados en la base de datos SQLite.

Prerrequisito: Ejecutar primero main.py para procesar los datos.

Autor: Sistema ETL
Fecha: 2025
"""

import os
import sys
from pathlib import Path

# Agregar el directorio raíz al path para importaciones
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from app.Visualize.SportsVisualizer import SportsVisualizer
from app.Config.config import Config


def print_header():
    """Imprime el encabezado del programa."""
    print("=" * 60)
    print("📊 GENERADOR DE VISUALIZACIONES - LE MANS DATA 📊")
    print("=" * 60)
    print()


def check_database_exists():
    """
    Verifica que la base de datos existe antes de generar visualizaciones.
    
    Returns:
        bool: True si la base de datos existe, False en caso contrario
    """
    if not os.path.exists(Config.SQLITE_DB_PATH):
        print("❌ ERROR: Base de datos no encontrada")
        print(f"   Buscando: {Config.SQLITE_DB_PATH}")
        print()
        print("💡 SOLUCIÓN:")
        print("   1. Ejecuta primero: python main.py")
        print("   2. Asegúrate de que el proceso ETL se complete exitosamente")
        print("   3. Luego ejecuta este script de visualización")
        return False
    
    print(f"✅ Base de datos encontrada: {Config.SQLITE_DB_PATH}")
    return True


def visualize_data():
    """
    Ejecuta la generación de todas las visualizaciones.
    
    Returns:
        bool: True si la visualización fue exitosa, False en caso contrario
    """
    print("\n" + "="*50)
    print("🎨 INICIANDO GENERACIÓN DE VISUALIZACIONES")
    print("="*50)
    
    try:
        # Crear visualizador
        print("🔧 Inicializando visualizador...")
        visualizer = SportsVisualizer()
        
        # Generar todas las gráficas
        success = visualizer.generate_all_charts()
        
        if success:
            print("\n✅ VISUALIZACIÓN COMPLETADA EXITOSAMENTE")
            print(f"📁 Gráficas disponibles en: {Config.CHARTS_OUTPUT_DIR}")
            
            # Listar archivos generados
            charts_dir = Config.CHARTS_OUTPUT_DIR
            if os.path.exists(charts_dir):
                chart_files = [f for f in os.listdir(charts_dir) if f.endswith('.png')]
                if chart_files:
                    print("\n📊 GRÁFICAS GENERADAS:")
                    for i, chart_file in enumerate(sorted(chart_files), 1):
                        print(f"   {i}. 🖼️  {chart_file}")
                        
                    print(f"\n💡 TIP: Abre la carpeta {charts_dir} para ver las gráficas")
            
            return True
        else:
            print("\n❌ ERROR EN LA VISUALIZACIÓN")
            print("⚠️  Revisa los mensajes de error anteriores")
            return False
        
    except Exception as e:
        print(f"\n❌ ERROR CRÍTICO EN VISUALIZACIÓN: {e}")
        return False


def print_summary(success):
    """
    Imprime el resumen final del proceso de visualización.
    
    Args:
        success (bool): Si el proceso fue exitoso
    """
    print("\n" + "="*60)
    print("📋 RESUMEN DE VISUALIZACIÓN")
    print("="*60)
    
    if success:
        print("🎉 ¡VISUALIZACIÓN COMPLETADA CON ÉXITO!")
        print("✅ Todas las gráficas generadas correctamente")
        print(f"📂 Ubicación: {Config.CHARTS_OUTPUT_DIR}")
        print("\n📊 TIPOS DE ANÁLISIS GENERADOS:")
        print("   • Análisis de Velocidad")
        print("   • Análisis de Resistencia") 
        print("   • Análisis Temporal")
        print("   • Dashboard Resumen")
    else:
        print("❌ VISUALIZACIÓN FALLÓ")
        print("⚠️  Revisa los errores mostrados anteriormente")
        print("\n🔧 POSIBLES SOLUCIONES:")
        print("   • Verifica que la base de datos existe (ejecuta main.py)")
        print("   • Comprueba que las dependencias están instaladas")
        print("   • Revisa permisos de escritura en la carpeta Charts/")
    
    print("="*60)


def main():
    """
    Función principal que ejecuta la generación de visualizaciones.
    """
    import time
    start_time = time.time()
    
    # Imprimir encabezado
    print_header()
    
    success = False
    
    try:
        # Verificar prerrequisitos
        if not check_database_exists():
            return
        
        # Generar visualizaciones
        success = visualize_data()
        
    except KeyboardInterrupt:
        print("\n⚠️  Proceso interrumpido por el usuario")
        success = False
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}")
        success = False
    
    finally:
        # Calcular tiempo transcurrido
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # Mostrar resumen
        print_summary(success)
        print(f"⏱️  Tiempo total: {elapsed_time:.2f} segundos")
        
        # Código de salida
        if success:
            print("\n🚀 ¡Visualización finalizada con éxito!")
            print("💡 Revisa las gráficas generadas en la carpeta Charts/")
            sys.exit(0)
        else:
            print("\n💥 Visualización falló")
            sys.exit(1)


if __name__ == "__main__":
    main()

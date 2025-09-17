"""
ETL Pipeline para Datos Deportivos
==================================
Pipeline principal que ejecuta las etapas de Extract, Transform y Load
para procesar datos deportivos de Le Mans.

Autor: Sistema ETL
Fecha: 2025
"""

import os
import sys
from pathlib import Path

# Agregar el directorio raíz al path para importaciones
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from app.Extract.SportsExtract import Extractor
from app.Transform.SportsTransformer import SportsTransformer
from app.Load.SportsLoader import Loader
from app.Config.config import Config


def print_header():
    """Imprime el encabezado del programa."""
    print("=" * 60)
    print("🏁 ETL PIPELINE - DATOS DEPORTIVOS LE MANS 🏁")
    print("=" * 60)
    print()


def print_step(step_number, title):
    """Imprime el título de cada paso del ETL."""
    print(f"\n{'='*20} PASO {step_number}: {title.upper()} {'='*20}")


def extract_data():
    """
    Ejecuta la etapa de extracción de datos.
    
    Returns:
        DataFrame: Los datos extraídos o None si hay error
    """
    print_step(1, "Extracción de Datos")
    
    # Verificar que el archivo existe
    input_file = Config.INPUT_PATH
    if not os.path.exists(input_file):
        print(f"❌ Error: El archivo {input_file} no existe")
        return None
    
    print(f"📂 Archivo fuente: {input_file}")
    
    # Crear extractor y extraer datos
    extractor = Extractor(input_file)
    df = extractor.extract()
    
    if df is not None:
        print(f"✅ Extracción exitosa:")
        print(f"   📊 Filas extraídas: {len(df)}")
        print(f"   📋 Columnas: {len(df.columns)}")
        print(f"   📝 Primeras columnas: {list(df.columns[:5])}")
        print(f"   📅 Rango de años: {df['Year'].min():.0f} - {df['Year'].max():.0f}")
    else:
        print("❌ Error en la extracción")
    
    return df


def transform_data(df):
    """
    Ejecuta la etapa de transformación de datos.
    
    Args:
        df: DataFrame con los datos extraídos
        
    Returns:
        DataFrame: Los datos transformados o None si hay error
    """
    print_step(2, "Transformación de Datos")
    
    if df is None:
        print("❌ Error: No hay datos para transformar")
        return None
    
    # Crear transformador y procesar datos
    transformer = SportsTransformer(df)
    transformed_df = transformer.transform()
    
    if transformed_df is not None:
        # Mostrar estadísticas finales
        stats = transformer.get_summary_stats()
        print(f"\n📊 ESTADÍSTICAS FINALES:")
        print(f"   📈 Total de registros: {stats['total_rows']}")
        print(f"   📋 Total de columnas: {stats['total_columns']}")
        print(f"   👥 Pilotos únicos: {stats['unique_drivers']}")
        print(f"   🏢 Equipos únicos: {stats['unique_teams']}")
        print(f"   🏁 Velocidad promedio: {stats['avg_speed']}")
        print(f"   📅 Período: {stats['year_range']}")
    else:
        print("❌ Error en la transformación")
    
    return transformed_df


def load_data(df):
    """
    Ejecuta la etapa de carga de datos.
    
    Args:
        df: DataFrame con los datos transformados
        
    Returns:
        bool: True si la carga fue exitosa, False en caso contrario
    """
    print_step(3, "Carga de Datos")
    
    if df is None:
        print("❌ Error: No hay datos para cargar")
        return False
    
    # Crear loader
    loader = Loader(df)
    
    try:
        # Cargar en SQLite
        print("💾 Guardando en base de datos SQLite...")
        loader.to_sqlite()
        
        # Cargar en CSV (backup)
        output_csv = Config.CSV_OUTPUT_PATH
        
        # Crear directorio Output si no existe
        os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
        
        print(f"💾 Guardando CSV de respaldo en: {output_csv}")
        loader.to_csv(output_csv)
        
        print("✅ Carga completada exitosamente")
        return True
        
    except Exception as e:
        print(f"❌ Error en la carga: {e}")
        return False


def print_summary(success, start_time=None):
    """
    Imprime el resumen final del proceso ETL.
    
    Args:
        success (bool): Si el proceso fue exitoso
        start_time: Tiempo de inicio (opcional)
    """
    print(f"\n{'='*60}")
    print("📋 RESUMEN DEL PROCESO ETL")
    print(f"{'='*60}")
    
    if success:
        print("🎉 ¡PROCESO ETL COMPLETADO EXITOSAMENTE!")
        print("✅ Todos los pasos ejecutados correctamente")
        print(f"📂 Datos disponibles en:")
        print(f"   🗄️  Base de datos: {Config.SQLITE_DB_PATH}")
        print(f"   📄 CSV procesado: Output/sports_data_processed.csv")
    else:
        print("❌ PROCESO ETL FALLÓ")
        print("⚠️  Revisa los errores mostrados anteriormente")
    
    print(f"{'='*60}")


def main():
    """
    Función principal que ejecuta todo el pipeline ETL.
    """
    import time
    start_time = time.time()
    
    # Imprimir encabezado
    print_header()
    
    success = False
    
    try:
        # PASO 1: Extracción
        df_raw = extract_data()
        if df_raw is None:
            raise Exception("Error en la extracción de datos")
        
        # PASO 2: Transformación
        df_transformed = transform_data(df_raw)
        if df_transformed is None:
            raise Exception("Error en la transformación de datos")
        
        # PASO 3: Carga
        load_success = load_data(df_transformed)
        if not load_success:
            raise Exception("Error en la carga de datos")
        
        success = True
        
    except Exception as e:
        print(f"\n❌ ERROR CRÍTICO: {e}")
        success = False
    
    finally:
        # Calcular tiempo transcurrido
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # Mostrar resumen
        print_summary(success)
        print(f"⏱️  Tiempo total: {elapsed_time:.2f} segundos")
        
        # Código de salida
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

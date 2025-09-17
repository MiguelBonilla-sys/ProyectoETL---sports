import pandas as pd
import numpy as np
from Config.config import Config

class SportsTransformer:
    """
    Clase para transformar y limpiar los datos deportivos extraídos.
    """
    
    def __init__(self, dataframe=None):
        self.df = dataframe
        self.original_rows = len(dataframe) if dataframe is not None else 0
    
    def clean_data(self):
        """
        Limpia los datos eliminando valores nulos y duplicados.
        """
        if self.df is None:
            print("Error: No hay datos para transformar")
            return None
            
        print(f"📊 Iniciando limpieza de datos...")
        print(f"   Filas originales: {self.original_rows}")
        
        # Eliminar filas completamente vacías
        self.df = self.df.dropna(how='all')
        print(f"   Después de eliminar filas vacías: {len(self.df)}")
        
        # Eliminar duplicados
        duplicates_before = len(self.df)
        self.df = self.df.drop_duplicates()
        duplicates_removed = duplicates_before - len(self.df)
        if duplicates_removed > 0:
            print(f"   Duplicados eliminados: {duplicates_removed}")
        
        print(f"   ✅ Filas finales después de limpieza: {len(self.df)}")
        return self.df
    
    def normalize_data(self):
        """
        Normaliza los datos aplicando formatos consistentes.
        """
        if self.df is None:
            print("Error: No hay datos para normalizar")
            return None
            
        print(f"🔧 Normalizando datos...")
        
        # Normalizar columnas de texto (eliminar espacios extra, convertir a título)
        text_columns = ['Drivers', 'Team', 'Car', 'Tyre', 'Series', 'Driver_nationality', 'Team_nationality']
        for col in text_columns:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(str).str.strip().str.title()
        
        # Normalizar columnas numéricas
        numeric_columns = ['Year', 'Laps', 'Km', 'Mi', 'Average_speed_kmh', 'Average_speed_mph', 'Average_lap_time']
        for col in numeric_columns:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        
        # Limpiar la columna Class (remover caracteres especiales)
        if 'Class' in self.df.columns:
            self.df['Class'] = self.df['Class'].astype(str).str.replace('>', '', regex=False).str.strip()
            self.df['Class'] = pd.to_numeric(self.df['Class'], errors='coerce')
        
        print(f"   ✅ Datos normalizados correctamente")
        return self.df
    
    def add_calculated_fields(self):
        """
        Añade campos calculados útiles para el análisis.
        """
        if self.df is None:
            print("Error: No hay datos para agregar campos calculados")
            return None
            
        print(f"➕ Agregando campos calculados...")
        
        # Década del año
        if 'Year' in self.df.columns:
            self.df['Decade'] = (self.df['Year'] // 10) * 10
        
        # Categoría de velocidad
        if 'Average_speed_kmh' in self.df.columns:
            self.df['Speed_Category'] = pd.cut(
                self.df['Average_speed_kmh'], 
                bins=[0, 100, 150, 200, float('inf')], 
                labels=['Slow', 'Medium', 'Fast', 'Very Fast']
            )
        
        # Categoría de resistencia (basada en número de vueltas)
        if 'Laps' in self.df.columns:
            self.df['Endurance_Category'] = pd.cut(
                self.df['Laps'], 
                bins=[0, 100, 150, 200, float('inf')], 
                labels=['Short', 'Medium', 'Long', 'Ultra Long']
            )
        
        # Eficiencia (distancia por vuelta)
        if 'Km' in self.df.columns and 'Laps' in self.df.columns:
            self.df['Km_per_Lap'] = self.df['Km'] / self.df['Laps']
            self.df['Km_per_Lap'] = self.df['Km_per_Lap'].round(2)
        
        print(f"   ✅ Campos calculados agregados: Decade, Speed_Category, Endurance_Category, Km_per_Lap")
        return self.df
    
    def transform(self):
        """
        Ejecuta todo el proceso de transformación.
        """
        print(f"\n🚀 INICIANDO TRANSFORMACIÓN DE DATOS")
        print(f"=" * 50)
        
        # Ejecutar todas las transformaciones
        self.clean_data()
        self.normalize_data()
        self.add_calculated_fields()
        
        # Mostrar resumen final
        if self.df is not None:
            print(f"\n📈 RESUMEN DE TRANSFORMACIÓN:")
            print(f"   Filas procesadas: {len(self.df)}")
            print(f"   Columnas: {len(self.df.columns)}")
            print(f"   Columnas disponibles: {list(self.df.columns)}")
            print(f"   Rango de años: {self.df['Year'].min():.0f} - {self.df['Year'].max():.0f}")
            print(f"=" * 50)
        
        return self.df
    
    def get_summary_stats(self):
        """
        Retorna estadísticas resumen de los datos transformados.
        """
        if self.df is None:
            return None
            
        stats = {
            'total_rows': len(self.df),
            'total_columns': len(self.df.columns),
            'year_range': f"{self.df['Year'].min():.0f} - {self.df['Year'].max():.0f}",
            'unique_drivers': self.df['Drivers'].nunique() if 'Drivers' in self.df.columns else 0,
            'unique_teams': self.df['Team'].nunique() if 'Team' in self.df.columns else 0,
            'avg_speed': f"{self.df['Average_speed_kmh'].mean():.2f} km/h" if 'Average_speed_kmh' in self.df.columns else 'N/A'
        }
        return stats

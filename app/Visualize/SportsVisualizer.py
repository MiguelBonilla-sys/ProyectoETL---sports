"""
SportsVisualizer - Módulo de Visualización para Datos de Le Mans
==============================================================
Genera gráficas y análisis visuales usando los datos procesados
de la base de datos SQLite con seaborn y matplotlib.

Autor: Sistema ETL
Fecha: 2025
"""

import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from pathlib import Path
from ..Config.config import Config


class SportsVisualizer:
    """
    Clase para generar visualizaciones de los datos deportivos de Le Mans.
    """
    
    def __init__(self, db_path=None):
        """
        Inicializa el visualizador.
        
        Args:
            db_path (str): Ruta a la base de datos SQLite. Si es None, usa la configuración por defecto.
        """
        self.db_path = db_path or Config.SQLITE_DB_PATH
        self.output_dir = Config.CHARTS_OUTPUT_DIR
        self.df = None
        
        # Configurar estilo de seaborn
        sns.set_style(Config.CHART_THEMES)
        plt.style.use('default')
        
        # Crear directorio de salida si no existe
        os.makedirs(self.output_dir, exist_ok=True)
    
    def _load_data_from_db(self):
        """
        Carga los datos desde la base de datos SQLite.
        
        Returns:
            DataFrame: Los datos cargados o None si hay error
        """
        try:
            if not os.path.exists(self.db_path):
                print(f"❌ Error: La base de datos {self.db_path} no existe")
                return None
            
            print(f"📊 Cargando datos desde: {self.db_path}")
            
            conn = sqlite3.connect(self.db_path)
            query = f"SELECT * FROM {Config.SQLITE_TABLE}"
            df = pd.read_sql_query(query, conn)
            conn.close()
            
            print(f"✅ Datos cargados exitosamente:")
            print(f"   📈 Registros: {len(df)}")
            print(f"   📋 Columnas: {len(df.columns)}")
            
            return df
            
        except Exception as e:
            print(f"❌ Error al cargar datos: {e}")
            return None
    
    def create_speed_analysis(self):
        """
        Crea gráficas de análisis de velocidad.
        """
        if self.df is None:
            print("❌ No hay datos disponibles para análisis de velocidad")
            return False
        
        try:
            print("📊 Generando análisis de velocidad...")
            
            # Crear figura con subplots
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))
            fig.suptitle('Análisis de Velocidad - Le Mans', fontsize=16, fontweight='bold')
            
            # 1. Distribución de velocidades por categoría
            if 'Speed_Category' in self.df.columns:
                sns.countplot(data=self.df, x='Speed_Category', ax=axes[0,0], palette='viridis')
                axes[0,0].set_title('Distribución por Categorías de Velocidad')
                axes[0,0].set_xlabel('Categoría de Velocidad')
                axes[0,0].set_ylabel('Número de Carreras')
                axes[0,0].tick_params(axis='x', rotation=45)
            
            # 2. Evolución de velocidad por década
            if 'Decade' in self.df.columns and 'Average_speed_kmh' in self.df.columns:
                decade_speed = self.df.groupby('Decade')['Average_speed_kmh'].mean().reset_index()
                sns.lineplot(data=decade_speed, x='Decade', y='Average_speed_kmh', 
                            marker='o', linewidth=3, ax=axes[0,1])
                axes[0,1].set_title('Evolución de Velocidad Promedio por Década')
                axes[0,1].set_xlabel('Década')
                axes[0,1].set_ylabel('Velocidad Promedio (km/h)')
            
            # 3. Box plot de velocidades por década
            if 'Decade' in self.df.columns and 'Average_speed_kmh' in self.df.columns:
                sns.boxplot(data=self.df, x='Decade', y='Average_speed_kmh', ax=axes[1,0])
                axes[1,0].set_title('Distribución de Velocidades por Década')
                axes[1,0].set_xlabel('Década')
                axes[1,0].set_ylabel('Velocidad (km/h)')
                axes[1,0].tick_params(axis='x', rotation=45)
            
            # 4. Histograma de velocidades
            if 'Average_speed_kmh' in self.df.columns:
                sns.histplot(data=self.df, x='Average_speed_kmh', bins=20, 
                            kde=True, ax=axes[1,1], color='skyblue')
                axes[1,1].set_title('Distribución de Velocidades')
                axes[1,1].set_xlabel('Velocidad Promedio (km/h)')
                axes[1,1].set_ylabel('Frecuencia')
            
            plt.tight_layout()
            
            # Guardar gráfica
            output_path = os.path.join(self.output_dir, 'speed_analysis.png')
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"✅ Análisis de velocidad guardado en: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error creando análisis de velocidad: {e}")
            return False
    
    def create_endurance_trends(self):
        """
        Crea gráficas de análisis de resistencia.
        """
        if self.df is None:
            print("❌ No hay datos disponibles para análisis de resistencia")
            return False
        
        try:
            print("📊 Generando análisis de resistencia...")
            
            # Crear figura con subplots
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))
            fig.suptitle('Análisis de Resistencia - Le Mans', fontsize=16, fontweight='bold')
            
            # 1. Distribución por categorías de resistencia
            if 'Endurance_Category' in self.df.columns:
                sns.countplot(data=self.df, x='Endurance_Category', ax=axes[0,0], palette='plasma')
                axes[0,0].set_title('Distribución por Categorías de Resistencia')
                axes[0,0].set_xlabel('Categoría de Resistencia')
                axes[0,0].set_ylabel('Número de Carreras')
                axes[0,0].tick_params(axis='x', rotation=45)
            
            # 2. Correlación entre vueltas y velocidad
            if 'Laps' in self.df.columns and 'Average_speed_kmh' in self.df.columns:
                sns.scatterplot(data=self.df, x='Laps', y='Average_speed_kmh', 
                              alpha=0.6, ax=axes[0,1])
                axes[0,1].set_title('Correlación: Vueltas vs Velocidad')
                axes[0,1].set_xlabel('Número de Vueltas')
                axes[0,1].set_ylabel('Velocidad Promedio (km/h)')
            
            # 3. Evolución de vueltas por década
            if 'Decade' in self.df.columns and 'Laps' in self.df.columns:
                decade_laps = self.df.groupby('Decade')['Laps'].mean().reset_index()
                sns.barplot(data=decade_laps, x='Decade', y='Laps', ax=axes[1,0], palette='coolwarm')
                axes[1,0].set_title('Evolución de Vueltas Promedio por Década')
                axes[1,0].set_xlabel('Década')
                axes[1,0].set_ylabel('Vueltas Promedio')
                axes[1,0].tick_params(axis='x', rotation=45)
            
            # 4. Eficiencia por década
            if 'Decade' in self.df.columns and 'Km_per_Lap' in self.df.columns:
                sns.boxplot(data=self.df, x='Decade', y='Km_per_Lap', ax=axes[1,1])
                axes[1,1].set_title('Eficiencia (Km por Vuelta) por Década')
                axes[1,1].set_xlabel('Década')
                axes[1,1].set_ylabel('Km por Vuelta')
                axes[1,1].tick_params(axis='x', rotation=45)
            
            plt.tight_layout()
            
            # Guardar gráfica
            output_path = os.path.join(self.output_dir, 'endurance_trends.png')
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"✅ Análisis de resistencia guardado en: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error creando análisis de resistencia: {e}")
            return False
    
    def create_temporal_analysis(self):
        """
        Crea gráficas de análisis temporal.
        """
        if self.df is None:
            print("❌ No hay datos disponibles para análisis temporal")
            return False
        
        try:
            print("📊 Generando análisis temporal...")
            
            # Crear figura con subplots
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))
            fig.suptitle('Análisis Temporal - Evolución Le Mans', fontsize=16, fontweight='bold')
            
            # 1. Número de participantes por década
            if 'Decade' in self.df.columns:
                decade_counts = self.df['Decade'].value_counts().sort_index()
                sns.barplot(x=decade_counts.index, y=decade_counts.values, 
                           ax=axes[0,0], palette='viridis')
                axes[0,0].set_title('Participantes por Década')
                axes[0,0].set_xlabel('Década')
                axes[0,0].set_ylabel('Número de Participantes')
                axes[0,0].tick_params(axis='x', rotation=45)
            
            # 2. Distribución de equipos únicos por década
            if 'Decade' in self.df.columns and 'Team' in self.df.columns:
                teams_per_decade = self.df.groupby('Decade')['Team'].nunique().reset_index()
                sns.lineplot(data=teams_per_decade, x='Decade', y='Team', 
                            marker='s', linewidth=3, ax=axes[0,1])
                axes[0,1].set_title('Diversidad de Equipos por Década')
                axes[0,1].set_xlabel('Década')
                axes[0,1].set_ylabel('Equipos Únicos')
            
            # 3. Evolución tecnológica (distancia total)
            if 'Decade' in self.df.columns and 'Km' in self.df.columns:
                decade_km = self.df.groupby('Decade')['Km'].mean().reset_index()
                sns.lineplot(data=decade_km, x='Decade', y='Km', 
                            marker='o', linewidth=3, ax=axes[1,0], color='orange')
                axes[1,0].set_title('Evolución de Distancia Promedio')
                axes[1,0].set_xlabel('Década')
                axes[1,0].set_ylabel('Distancia Promedio (Km)')
            
            # 4. Heatmap de categorías por década
            if all(col in self.df.columns for col in ['Decade', 'Speed_Category', 'Endurance_Category']):
                # Crear tabla cruzada
                heatmap_data = pd.crosstab(self.df['Decade'], self.df['Speed_Category'])
                sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlOrRd', ax=axes[1,1])
                axes[1,1].set_title('Categorías de Velocidad por Década')
                axes[1,1].set_xlabel('Categoría de Velocidad')
                axes[1,1].set_ylabel('Década')
            
            plt.tight_layout()
            
            # Guardar gráfica
            output_path = os.path.join(self.output_dir, 'temporal_analysis.png')
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"✅ Análisis temporal guardado en: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error creando análisis temporal: {e}")
            return False
    
    def create_summary_dashboard(self):
        """
        Crea un dashboard resumen con las métricas más importantes.
        """
        if self.df is None:
            print("❌ No hay datos disponibles para el dashboard")
            return False
        
        try:
            print("📊 Generando dashboard resumen...")
            
            # Crear figura grande
            fig = plt.figure(figsize=(20, 12))
            fig.suptitle('Dashboard Resumen - Le Mans Data Analysis', fontsize=20, fontweight='bold')
            
            # Layout de la grilla
            gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)
            
            # Estadísticas generales (texto)
            ax_stats = fig.add_subplot(gs[0, 0])
            ax_stats.axis('off')
            
            total_races = len(self.df)
            year_range = f"{self.df['Year'].min():.0f} - {self.df['Year'].max():.0f}"
            avg_speed = self.df['Average_speed_kmh'].mean()
            total_teams = self.df['Team'].nunique() if 'Team' in self.df.columns else 0
            
            stats_text = f"""ESTADÍSTICAS GENERALES
            
📊 Total Carreras: {total_races:,}
📅 Período: {year_range}
🏁 Velocidad Promedio: {avg_speed:.1f} km/h
🏢 Equipos Únicos: {total_teams:,}
🏆 Décadas Analizadas: {self.df['Decade'].nunique() if 'Decade' in self.df.columns else 'N/A'}"""
            
            ax_stats.text(0.1, 0.5, stats_text, fontsize=12, verticalalignment='center',
                         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
            
            # Top 10 equipos más exitosos
            if 'Team' in self.df.columns:
                ax_teams = fig.add_subplot(gs[0, 1:3])
                top_teams = self.df['Team'].value_counts().head(10)
                sns.barplot(x=top_teams.values, y=top_teams.index, ax=ax_teams, palette='viridis')
                ax_teams.set_title('Top 10 Equipos (Más Participaciones)')
                ax_teams.set_xlabel('Número de Participaciones')
            
            # Evolución de velocidad
            if 'Year' in self.df.columns and 'Average_speed_kmh' in self.df.columns:
                ax_speed_evolution = fig.add_subplot(gs[0, 3])
                yearly_speed = self.df.groupby('Year')['Average_speed_kmh'].mean()
                ax_speed_evolution.plot(yearly_speed.index, yearly_speed.values, linewidth=2, color='red')
                ax_speed_evolution.set_title('Evolución de Velocidad')
                ax_speed_evolution.set_xlabel('Año')
                ax_speed_evolution.set_ylabel('Velocidad (km/h)')
                ax_speed_evolution.tick_params(axis='x', rotation=45)
            
            # Distribución de categorías
            if 'Speed_Category' in self.df.columns:
                ax_speed_cat = fig.add_subplot(gs[1, 0])
                speed_counts = self.df['Speed_Category'].value_counts()
                colors = plt.cm.Set3(range(len(speed_counts)))
                ax_speed_cat.pie(speed_counts.values, labels=speed_counts.index, autopct='%1.1f%%',
                               colors=colors, startangle=90)
                ax_speed_cat.set_title('Categorías de Velocidad')
            
            # Correlación vueltas vs velocidad
            if 'Laps' in self.df.columns and 'Average_speed_kmh' in self.df.columns:
                ax_correlation = fig.add_subplot(gs[1, 1])
                sns.scatterplot(data=self.df, x='Laps', y='Average_speed_kmh', 
                              alpha=0.6, ax=ax_correlation)
                ax_correlation.set_title('Vueltas vs Velocidad')
                ax_correlation.set_xlabel('Vueltas')
                ax_correlation.set_ylabel('Velocidad (km/h)')
            
            # Heatmap por década
            if all(col in self.df.columns for col in ['Decade', 'Speed_Category']):
                ax_heatmap = fig.add_subplot(gs[1, 2:])
                heatmap_data = pd.crosstab(self.df['Decade'], self.df['Speed_Category'])
                sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlOrRd', ax=ax_heatmap)
                ax_heatmap.set_title('Categorías de Velocidad por Década')
            
            # Timeline de participaciones
            if 'Year' in self.df.columns:
                ax_timeline = fig.add_subplot(gs[2, :])
                yearly_counts = self.df['Year'].value_counts().sort_index()
                ax_timeline.bar(yearly_counts.index, yearly_counts.values, alpha=0.7, color='steelblue')
                ax_timeline.set_title('Timeline de Participaciones por Año')
                ax_timeline.set_xlabel('Año')
                ax_timeline.set_ylabel('Número de Participaciones')
                ax_timeline.tick_params(axis='x', rotation=45)
            
            # Guardar dashboard
            output_path = os.path.join(self.output_dir, 'summary_dashboard.png')
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"✅ Dashboard resumen guardado en: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error creando dashboard: {e}")
            return False
    
    def generate_all_charts(self):
        """
        Genera todas las gráficas y análisis disponibles.
        
        Returns:
            bool: True si todas las gráficas se generaron exitosamente
        """
        print(f"\n🎨 INICIANDO GENERACIÓN DE VISUALIZACIONES")
        print(f"=" * 60)
        
        # Cargar datos
        self.df = self._load_data_from_db()
        if self.df is None:
            print("❌ No se pudieron cargar los datos")
            return False
        
        print(f"📂 Directorio de salida: {self.output_dir}")
        
        success_count = 0
        total_charts = 4
        
        # Generar cada tipo de gráfica
        charts = [
            ("Análisis de Velocidad", self.create_speed_analysis),
            #("Análisis de Resistencia", self.create_endurance_trends),
            #("Análisis Temporal", self.create_temporal_analysis),
            #("Dashboard Resumen", self.create_summary_dashboard)
        ]
        
        for chart_name, chart_method in charts:
            print(f"\n🎯 Generando: {chart_name}")
            if chart_method():
                success_count += 1
            else:
                print(f"⚠️  Falló: {chart_name}")
        
        # Resumen final
        print(f"\n{'='*60}")
        print(f"📊 RESUMEN DE VISUALIZACIONES")
        print(f"{'='*60}")
        print(f"✅ Gráficas exitosas: {success_count}/{total_charts}")
        print(f"📁 Ubicación: {self.output_dir}")
        
        if success_count == total_charts:
            print("🎉 ¡Todas las visualizaciones generadas exitosamente!")
            return True
        else:
            print("⚠️  Algunas visualizaciones fallaron")
            return False

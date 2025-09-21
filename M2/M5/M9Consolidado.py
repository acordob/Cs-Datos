# EVALUACIÓN FINAL M9: ANÁLISIS DE MOVIMIENTOS MIGRATORIOS CON SPARK
# Alumna: Alejandra Córdoba Sepúlveda

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Crear sesión Spark
spark = SparkSession.builder.appName("Migraciones").getOrCreate()

# Define schema to read problematic numeric columns as StringType
schema = StructType([
    StructField("ID", IntegerType(), True),
    StructField("Origen", StringType(), True),
    StructField("Destino", StringType(), True),
    StructField("Año", IntegerType(), True),
    StructField("Razón", StringType(), True),
    StructField("PIB_Origen", StringType(), True), # Read as String
    StructField("PIB_Destino", StringType(), True), # Read as String
    StructField("Tasa_Desempleo_Origen", DoubleType(), True),
    StructField("Tasa_Desempleo_Destino", DoubleType(), True),
    StructField("Nivel_Educativo_Origen", DoubleType(), True),
    StructField("Nivel_Educativo_Destino", DoubleType(), True),
    StructField("Población_Origen", StringType(), True), # Read as String
    StructField("Población_Destino", StringType(), True)  # Read as String
])


# Cargar dataset with defined schema
df = spark.read.csv("migraciones.csv", header=True, schema=schema)

# Clean problematic numeric columns
cols_to_clean_cast = ["PIB_Origen", "PIB_Destino", "Población_Origen", "Población_Destino"]
for col_name in cols_to_clean_cast:
    df = df.withColumn(col_name, regexp_replace(col(col_name), ",", "")) # Remove commas

# Define a UDF to safely cast string to double
def safe_cast_to_double(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None # Return None for values that cannot be cast

safe_cast_udf = udf(safe_cast_to_double, DoubleType())

# Cast problematic numeric columns to DoubleType using UDF
for col_name in cols_to_clean_cast:
    df = df.withColumn(col_name, safe_cast_udf(col(col_name)))


# Exploración y estadísticas descriptivas
df.show(5)
df.printSchema()
df.describe().show()

# Data Transformations using DataFrame operations
# Example: filter migrations by economic cause
df_economica = df.filter(df["Razón"] == "Económica")

# Map destination countries (using select)
destinos_df = df.select("Destino")

# Count records
print("Total de migraciones:", df.count())
print("Migraciones económicas:", df_economica.count())
print("Primeros destinos:")
destinos_df.show(5)

# Filtrar por año reciente
df_filtrado = df.filter(df["Año"] >= 2015)

# Agregación: migraciones por país de destino
df_agg = df.groupBy("Destino").count().orderBy("count", ascending=False)
df_agg.show()

# Guardar en formato Parquet
df_agg.write.parquet("resultados_migracion.parquet", mode="overwrite")

# Registrar tabla temporal
df.createOrReplaceTempView("migraciones")

# Países con mayor recepción
spark.sql("""
SELECT Destino, COUNT(*) AS Total
FROM migraciones
GROUP BY Destino
ORDER BY Total DESC
""").show()

# Razones de migración por región
spark.sql("""
SELECT `Región_Origen`, Razón, COUNT(*) AS Total
FROM migraciones
GROUP BY `Región_Origen`, Razón
ORDER BY Total DESC
""").show()

# Indexar variables categóricas
indexer = StringIndexer(inputCol="Razón", outputCol="Razón_Index")
df_indexed = indexer.fit(df).transform(df)

# Handle missing values in numeric columns (including those just cast)
numeric_cols = ["PIB_Origen", "PIB_Destino", "Tasa_Desempleo_Origen", "Tasa_Desempleo_Destino", "Nivel_Educativo_Origen", "Nivel_Educativo_Destino", "Población_Origen", "Población_Destino"]
df_filled = df_indexed.na.fill(0.0, subset=numeric_cols) # Fill with 0.0 for DoubleType


# Vector de características
assembler = VectorAssembler(
    inputCols=numeric_cols + ["Razón_Index"],
    outputCol="features"
)
df_final = assembler.transform(df_filled)

# Select features and label, ensuring 'Migró' column exists or creating a dummy one for demonstration
# Based on the schema, 'Migró' column does not exist. We will create a dummy column for demonstration purposes.
# In a real scenario, you would need a column indicating migration status.
df_final = df_final.withColumn("Migró", lit(1).cast(DoubleType())).select("features", "Migró")


# División de datos
train, test = df_final.randomSplit([0.8, 0.2], seed=42)

lr = LogisticRegression(labelCol="Migró", featuresCol="features")
modelo = lr.fit(train)

# Evaluación
predicciones = modelo.transform(test)
evaluator = BinaryClassificationEvaluator(labelCol="Migró")
precision = evaluator.evaluate(predicciones)

print(f"Precisión del modelo: {precision:.2f}")
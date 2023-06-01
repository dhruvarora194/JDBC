import pyspark.sql.functions as F

# read in the data
df = spark.read.csv('assignment-individual-data.csv',header = True)

# drop any missing values
df = df.dropna()

# calculate summary statistics
df.select(['GENDER','INCOMETOTAL']).groupBy('GENDER').agg(F.mean('INCOMETOTAL').alias('Mean Income'), F.stddev('INCOMETOTAL').alias('Std. Dev. Income'), F.min('INCOMETOTAL').alias('Min. Income'), F.max('INCOMETOTAL').alias('Max. Income')).show()

# create a bar chart
df.groupBy('GENDER').pivot('EDUCATIONLEVEL').count().orderBy('GENDER').show()

# create a pie chart
df.groupBy('GENDER').pivot('OWNPROPERTY').count().orderBy('GENDER').show()

# create a bar chart
df.groupBy('GENDER').pivot('MARITALSTATUS').count().orderBy('GENDER').show()

# create a histogram
df.select(['GENDER','INCOMETOTAL']).groupBy('GENDER').agg(F.mean('INCOMETOTAL').alias('Mean Income'), F.stddev('INCOMETOTAL').alias('Std. Dev. Income'), F.min('INCOMETOTAL').alias('Min. Income'), F.max('INCOMETOTAL').alias('Max. Income')).show()

# create a box plot
df.groupBy('GENDER').pivot('HOUSINGTYPE').count().orderBy('GENDER').show()

# create a bubble plot
df.groupBy('GENDER').pivot('FAMSIZE','CREDITSTATUS').count().orderBy('GENDER').show()

# create a one-way ANOVA
df.groupBy('HOUSINGTYPE').agg(F.mean('INCOMETOTAL').alias('Mean Income'), F.stddev('INCOMETOTAL').alias('Std. Dev. Income'), F.min('INCOMETOTAL').alias('Min. Income'), F.max('INCOMETOTAL').alias('Max. Income')).show()

# create a one-way ANOVA with blocking
df.groupBy('CREDITSTATUS','HOUSINGTYPE').agg(F.mean('INCOMETOTAL').alias('Mean Income'), F.stddev('INCOMETOTAL').alias('Std. Dev. Income'), F.min('INCOMETOTAL').alias('Min. Income'), F.max('INCOMETOTAL').alias('Max. Income')).show()

# create a one-way ANOVA with post-hoc pairwise comparisons
df.groupBy('HOUSINGTYPE').agg(F.mean('INCOMETOTAL').alias('Mean Income'), F.stddev('INCOMETOTAL').alias('Std. Dev. Income'), F.min('INCOMETOTAL').alias('Min. Income'), F.max('INCOMETOTAL').alias('Max. Income')).show()

# create a one-way ANOVA
df.groupBy('EDUCATIONLEVEL').agg(F.mean('INCOMETOTAL').alias('Mean Income'), F.stddev('INCOMETOTAL').alias('Std. Dev. Income'), F.min('INCOMETOTAL').alias('Min. Income'), F.max('INCOMETOTAL').alias('Max. Income')).show()

# create a one-way ANOVA with blocking
df.groupBy('HOUSINGTYPE','EDUCATIONLEVEL').agg(F.mean('INCOMETOTAL').alias('Mean Income'), F.stddev('INCOMETOTAL').alias('Std. Dev. Income'), F.min('INCOMETOTAL').alias('Min. Income'), F.max('INCOMETOTAL').alias('Max. Income')).show()

# create a one-way ANOVA with post-hoc pairwise comparisons
df.groupBy('EDUCATIONLEVEL').agg(F.mean('INCOMETOTAL').alias('Mean Income'), F.stddev('INCOMETOTAL').alias('Std. Dev. Income'), F.min('INCOMETOTAL').alias('Min. Income'), F.max('INCOMETOTAL').alias('Max. Income')).show()

import pandas as pd

squirrel_central_park = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
squirrel_color = squirrel_central_park['Primary Fur Color']  # Selects only the 'Primary Fur Color' column or series

squirrel_count = squirrel_color.value_counts()  # Count the number of squirrels of each color

df = pd.DataFrame(squirrel_count)  # Turns into a data frame
df.to_csv('squirrels_count.csv')  # Create a csv file with the data frame
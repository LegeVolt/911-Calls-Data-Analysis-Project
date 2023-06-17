import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Set styles for each graph
sns.set(style="whitegrid", palette="Set2")
sns.set_context("notebook", font_scale=1.2)

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\Barif\OneDrive\שולחן העבודה\הכל  פה גבר\Programming\data analytics\Projects\911 Calls\911.csv")

# Display information about the DataFrame
print(df.info())

# Display the first few rows of the DataFrame
print(df.head())

# Top 5 zip codes with the highest call frequencies
top5_zipcodes = df['zip'].value_counts().head()
print(top5_zipcodes)

# Top 5 townships with the highest call frequencies
top5_townships = df['twp'].value_counts().head()
print(top5_townships)

# Extract the reason for the call from the title column
df['Reason'] = df['title'].apply(lambda string: string.split(':')[0])
print(df['Reason'])

# Count the most common reasons for the call
most_common_reasons = df['Reason'].value_counts()
print(most_common_reasons)

# Create a count plot to visualize the reasons for the call
plt.figure(figsize=(8, 6))
sns.countplot(x='Reason', data=df, palette='Spectral')
plt.title('Reasons for the Call')

# Convert the timeStamp column to datetime type
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# Add new columns for hour, month, and day of the week
df['Hour'] = df['timeStamp'].dt.hour
df['Month'] = df['timeStamp'].dt.month
df['Day of Week'] = df['timeStamp'].dt.dayofweek

# Map day of the week numbers to their corresponding names
weekday_mapping = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
df['Day of Week'] = df['Day of Week'].map(weekday_mapping)

# Create a count plot to visualize the emergency calls by day of the week
plt.figure(figsize=(10, 6))
sns.countplot(x='Day of Week', data=df, hue='Reason')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.title('Emergency Calls by Day of the Week')

# Create a count plot to visualize the emergency calls by month
plt.figure(figsize=(10, 6))
sns.countplot(x='Month', data=df, hue='Reason')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.title('Emergency Calls by Month')

# Group the DataFrame by month and count the calls
byMonth = df.groupby('Month').count().reset_index()
print(byMonth)

# Create a linear regression plot to visualize the count of calls by month
plt.figure(figsize=(10, 6))
sns.lmplot(x='Month', y='twp', data=byMonth)
plt.title('Count of Calls by Month')

# Add new column Year with a date data type
df['Year'] = df['timeStamp'].dt.year

# Group the DataFrame by date and count the calls
group_by_year = df.groupby('Year').count()['lat'].reset_index()

# Create a line plot to visualize the 911 calls by year
plt.figure()
sns.lineplot(x='Year', y='lat', data=group_by_year)
plt.title('911 Calls by Year')

# Group the DataFrame by year and count the calls for the 'Traffic' reason
group_by_year_traffic = df[df['Reason'] == 'Traffic'].groupby('Year').count()['lat'].reset_index()

# Create a line plot to visualize the 911 calls for the 'Traffic' reason by year
plt.figure()
plt.title('911 Calls - Traffic')
sns.lineplot(x='Year', y='lat', data=group_by_year_traffic)

# Group the DataFrame by date and count the calls for the 'Fire' reason
group_by_year_fire = df[df['Reason'] == 'Fire'].groupby('Year').count()['lat'].reset_index()

# Create a line plot to visualize the 911 calls for the 'Fire' reason by date
plt.figure()
sns.lineplot(x='Year', y='lat', data=group_by_year_fire)
plt.title('911 Calls - Fire')
plt.ylabel('Count')

# Group the DataFrame by year and count the calls for the 'EMS' reason
group_by_date_ems = df[df['Reason'] == 'EMS'].groupby('Year').count()['lat'].reset_index()

# Create a line plot to visualize the 911 calls for the 'EMS' reason by year
plt.figure()
sns.lineplot(x='Year', y='lat', data=group_by_date_ems)
plt.title('911 Calls - EMS')
plt.ylabel('Count')

# Create a larger figure for the day-hour heatmap
plt.figure(figsize=(12, 6))

# Group the DataFrame by day of the week and hour and count the calls for each combination
dayHour = df.groupby(['Day of Week', 'Hour']).count()['Reason'].unstack()

# Create a heatmap to visualize the count of calls by day and hour
sns.heatmap(dayHour, cmap='viridis')
plt.title('Count of Calls by Day and Hour')

plt.show()

<<<<<<< HEAD

import time
import datetime as dt
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#This function retrieves the initial filters neccessary to move on through the application: In this case we ask user for city, month and day to filter the data


def get_filters():
    city = input('Hello! Let\'s explore some US bikeshare data! What city data would you like to explore?Chicago/New York City/Washington?:')
    if city == 'Chicago' or city == 'chicago':
        city ='chicago'
    elif city == 'New York City' or city == 'new york city':
        city ='new york city'
    elif city == 'Washington' or city == 'washington':
        city = 'washington'
    else:
        print('Invalid input. Please choose from Chicago, New York City or Washington')
        return get_filters()

    month = ''
    month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
        print("\nI'm sorry, I'm not sure which month you're trying to filter by. Let's try again.")
        return get_filters()

    day = ''
    day = input('What day?:').lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print("\nI'm sorry, I didn't get that. Let's start over")
        return get_filters()

    print('-'*40)
    return city, month, day


#This function loads the specified data:


def load_data(city, month, day):

    # load data file inChito a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


# This function fetches and dispays the time statistics for our application:

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most popular month is', common_month)

    # TO DO: display the most common day of week
    df['dayofweek'] = df['Start Time'].dt.dayofweek
    dayofweek = df['dayofweek'].mode()[0]
    print('The most popular day of the week is', dayofweek)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['hour'].mode()[0]
    print('The most popular hour is', hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# This function fetches and dispays the station statistics for our application:

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start = df['Start Station'].mode()[0]
    print('The most common start station is:', start)

    # TO DO: display most commonly used end station
    end = df['End Station'].mode()[0]
    print('The most common end station is:', end)


    # TO DO: display most frequent combination of start station and end station trip
    freq_combin = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination of start and end station trip is:', freq_combin)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# This function fetches and dispays the trip duration statistics for our application:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print('The total travel time is: {} hours {} minutes and {} seconds'.format(hour, minute, second))


    # TO DO: display mean travel time
    df['End Time'] =pd.to_datetime(df['End Time'])
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    total_time = df['End Time'] - df['Start Time']
    mean_time = total_time.mean()
    print('The mean travel time is:', mean_time)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# This function fetches and dispays the user statistics for our application:


def user_stats(df):
  """Displays statistics on bikeshare users."""

  print('\nCalculating User Stats...\n')
  start_time = time.time()

  # TO DO: Display counts of user types
  user_type_counts = df['User Type'].value_counts()
  print('The counts of user type are:', user_type_counts)

  # TO DO: Display counts of gender
  while 'Gender' in df.columns:
      
      gender_counts = df['Gender'].value_counts()
      print('The gender counts are:', gender_counts)
      break
    
  while 'Birth Year' in df.columns:
      # TO DO: Display earliest, most recent, and most common year of birth
      earliest_yob = df['Birth Year'].sort_values(ascending =True).iloc[0]
      most_recent_yob = df['Birth Year'].sort_values(ascending =False).iloc[0]
      common_yob = df['Birth Year'].value_counts().idxmax()
      print('The earliest year of birth is:',earliest_yob)
      print('The most recent year of birth is:', most_recent_yob)
      print('The most common year of birth is:', common_yob)
      break
    
  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)


# This function gives the user the option to look at raw data. Specifically this displays five lines of data at a time.

def display_data(df):
    start_row = 0
    end_row =5
    
    raw_data = input('Would you like to see the first five rows of the dataset? (yes/no)')
    
    if raw_data == 'yes' or raw_data=='Yes':
        while end_row <= df.shape[0]-1:
            
            print(df.iloc[start_row:end_row,:])
            start_row += 5
            end_row +=5
            
            more_data = input('Would you like to look at more rows?:')
            
            
            if more_data == 'no' or more_data == 'No':
                break
    



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
||||||| merged common ancestors
=======

import time
import datetime as dt
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#THIS FUNCTION RETRIEVES USER FILTERS.

def get_filters():
    city = input('Hello! Let\'s explore some US bikeshare data! What city data would you like to explore?Chicago/New York City/Washington?:')
    if city == 'Chicago' or city == 'chicago':
        city ='chicago'
    elif city == 'New York City' or city == 'new york city':
        city ='new york city'
    elif city == 'Washington' or city == 'washington':
        city = 'washington'
    else:
        print('Invalid input. Please choose from Chicago, New York City or Washington')
        return get_filters()

    month = ''
    month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
        print("\nI'm sorry, I'm not sure which month you're trying to filter by. Let's try again.")
        return get_filters()

    day = ''
    day = input('What day?:').lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print("\nI'm sorry, I didn't get that. Let's start over")
        return get_filters()

    print('-'*40)
    return city, month, day



#THIS FUNCTION LOADS DATA BASED ON FILTERS CHOSEN IN LAST FUNCTION:

def load_data(city, month, day):

    # load data file inChito a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


#THIS FUNCTION DISPLAYS TIME STATISTICS:

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most popular month is', common_month)

    # TO DO: display the most common day of week
    df['dayofweek'] = df['Start Time'].dt.dayofweek
    dayofweek = df['dayofweek'].mode()[0]
    print('The most popular day of the week is', dayofweek)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['hour'].mode()[0]
    print('The most popular hour is', hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# THIS FUNCTION DISPLAYS STATION STATISTICS:

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start = df['Start Station'].mode()[0]
    print('The most common start station is:', start)

    # TO DO: display most commonly used end station
    end = df['End Station'].mode()[0]
    print('The most common end station is:', end)


    # TO DO: display most frequent combination of start station and end station trip
    freq_combin = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination of start and end station trip is:', freq_combin)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#THIS FUNCTION DISPLAYS TRIP DURATION STATISTICS:

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print('The total travel time is: {} hours {} minutes and {} seconds'.format(hour, minute, second))


    # TO DO: display mean travel time
    df['End Time'] =pd.to_datetime(df['End Time'])
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    total_time = df['End Time'] - df['Start Time']
    mean_time = total_time.mean()
    print('The mean travel time is:', mean_time)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#THIS FUNCITON DISPLAYS USER STATISTICS, BASED ON WHICH DATASET IS CHOSEN
def user_stats(df):
  """Displays statistics on bikeshare users."""

  print('\nCalculating User Stats...\n')
  start_time = time.time()

  # TO DO: Display counts of user types
  user_type_counts = df['User Type'].value_counts()
  print('The counts of user type are:', user_type_counts)

  # TO DO: Display counts of gender
  while 'Gender' in df.columns:
      
      gender_counts = df['Gender'].value_counts()
      print('The gender counts are:', gender_counts)
      break
    
  while 'Birth Year' in df.columns:
      # TO DO: Display earliest, most recent, and most common year of birth
      earliest_yob = df['Birth Year'].sort_values(ascending =True).iloc[0]
      most_recent_yob = df['Birth Year'].sort_values(ascending =False).iloc[0]
      common_yob = df['Birth Year'].value_counts().idxmax()
      print('The earliest year of birth is:',earliest_yob)
      print('The most recent year of birth is:', most_recent_yob)
      print('The most common year of birth is:', common_yob)
      break
    
  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)

#THIS FUNCTION GIVES USER THE OPTION TO VIEW FIVE ROWS OF RAW DATA:
def display_data(df):
    start_row = 0
    end_row =5
    
    raw_data = input('Would you like to see the first five rows of the dataset? (yes/no)')
    
    if raw_data == 'yes' or raw_data=='Yes':
        while end_row <= df.shape[0]-1:
            
            print(df.iloc[start_row:end_row,:])
            start_row += 5
            end_row +=5
            
            more_data = input('Would you like to look at more rows?:')
            
            
            if more_data == 'no' or more_data == 'No':
                break
    



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
>>>>>>> refactoring

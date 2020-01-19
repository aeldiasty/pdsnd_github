import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, or/and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York, or Washington?").title()
    while city not in ['Chicago', 'New York', 'Washington']:
        city = input('Please enter the correct city name; "Chicago", "New York", or "Washington":').title()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to filter by? (Please type: "January", "February", "March", or "all"):').title()
    while month not in ['January', 'February', 'March', 'April', 'May', 'June', 'All']:
        month = input('Please enter the correct month name; "January", "February", "March", or "all"').title()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day would you like to filter by? (Please type: "Saturday", "Sunday", "Monday", ... or "all"):').title()
    while day not in ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'All']:
        day = input('Please enter the correct month name; "Saturday", "Sunday", "Monday", ... or "all"').title()
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month_index = months.index(month)
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month_index+1]
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day]
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    if month == "All":
        popular_month = df['month'].mode()[0]
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        print('The most frequent month of travel is: ', months[popular_month-1])
        
    # TO DO: display the most common day of week
    if day == "All":
        popular_day = df['day_of_week'].mode()[0]
        print('The most frequent day of travel is: ', popular_day)
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most frequent hour of travel is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commmonly used start station is: ', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commmonly used end station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'] + " and " + df['End Station']
    popular_start_end_station = df['Start_End'].mode()[0]
    print('The most frequent combination of start station and end station trip is: ', popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel tims is: ', df['Trip Duration'].sum(), ' seconds.')

    # TO DO: display mean travel time
    print('The mean travel tims is: ', df['Trip Duration'].mean(), ' seconds.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types is: \n', df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print('The counts of gender is: \n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print('The earliest year of birth is: ', df['Birth Year'].min())
        print('The most recent year of birth is: ', df['Birth Year'].max())
        print('The most common year of birth is: ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.')
        index1 = 0
        index2 = 0
        while raw_data == 'yes':
            index1 = index2
            index2 = index1 + 5
            print(df.iloc[index1:index2])
            raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

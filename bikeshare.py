import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = {'a' : 'chicago', 'b' : 'new york city', 'c' : 'washington'}
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['m', 'tu', 'w', 'th', 'f', 'sa', 'su']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    
    while True:
        try:
            city_key = input("\nChoose the city you would like to see its data, type:\n'A' for Chicago.\n'B' for New York.\n'C' for Washington.\n").lower()
            if city_key in ['a', 'b', 'c']:
                city = cities[city_key]
                print("Looks like you wanna hear about {}! if this isn't true, restart the program now!\n".format(city.title()))
                break
            else:
                print("Invaild city input, please try again!")
        except:
            print("Invaild input, please try again!")
    
    while True:
        try:
            filter_type = input("Would you like to filter the data by month, day, both, or not at all? type 'none' for no time filter.\n").lower()
            if filter_type == 'month':
                month = input("Which month? January, February, March, April, May, or June?\n").lower()
                day = 'all'
                if month in months:
                    break
                else:
                    print("Invaild month input, please try again!")
            elif filter_type == 'day':
                month = 'all'
                day = input("Which day? Please type a day M, Tu, W, Th, F, Sa, Su.\n").lower()
                if day in days:
                    break
                else:
                    print("Invaild day input, please try again!")
            elif filter_type == 'both':
                month = input("Which month? January, February, March, April, May, or June?\n").lower()
                day = input("Which day? Please type a day M, Tu, W, Th, F, Sa, Su.\n").lower()
                if month in months and day in days:
                    break
                else:
                    print("Invaild month or day input, please try again!")
            elif filter_type == 'none':
                month, day = 'all', 'all'
                break
            else:
                print("Invaild filter type input, please try again!")
        except:
            print("Invaild input, please try again!")
            

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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month_index = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month_index]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        day_index = days.index(day)
        df = df[df['day_of_week'] == day_index]
    
    return df

    

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        common_month = df['month'].mode()[0]
        print("The most common month: {}.".format(common_month))

    # TO DO: display the most common day of week
    if day == 'all':
        common_day = days[int(df['day_of_week'].mode()[0])]
        print("The most common day: {}.".format(common_day.title()))

    # TO DO: display the most common start hour
    common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most common start hour: {}.".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: {}.".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: {}.".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip: {}.".format(common_combination)) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("the total travel time: {} seconds.".format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("the mean travel time: {} seconds.".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("the counts of user types:")
    print(user_types)

    if city != 'washington':
    # TO DO: Display counts of gender
        user_genders = df['Gender'].value_counts()
        print("\nthe counts of user genders:")
        print(user_genders)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        
        print("\nthe earliest year of birth: {}, the most recent year: {}, the most common year: {}.".format(earliest_year, most_recent_year, most_common_year))
        
    else:
        print("\nNo gender or birth year data was provided for this city!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    
    print("\nRaw data is available to check ...\n")
    display_data = input("Would you like to check some raw data? Enter yes or no.\n").lower()
    
    while display_data == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], chunksize = 5):
                print('\n')
                print(chunk)
                display_data = input("Would you like to check some more raw data? Enter yes or no.\n").lower()
                if display_data == 'no':
                    break
        except:
            print("Invaild input, please try again!")
            
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

import time
import pandas as pd
import numpy as np

name = input("enter your name: ")
print('''
¡Hi {}!

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    cities=['chicago','new york city','washington']
    months=['january','february','march', 'april','may','june']
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """"

    print('Hello there! Let\'s explore some US bikeshare facts, so you can get familiar!')
    '

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city = input("\n Which city do you want to consult? \n Please select one of the following cities: Chicago, New York City, Washington. \n").lower()
            if city not in cities:
                print("Sorry, it seems that the city you are looking for is misspelled. Try again.")
                continue
            else:
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
           month = input("\n What month would I like to explore?: january, february, march, april, may, june, all? \n").lower()
           if month !='all' and month not in months:
                print("It seems that the month you chose is not available. Try again")
                continue
           else:
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
           day = input("\nWhat day do you want to see?: monday, tuesday, wednesday, thursday, friday, saturday, sunday, all? \n").lower()
           if day !='all' and day not in days:
                print("Sorry! You did not enter a correct day of the week. Try again.")
                continue
           else:
                break


    print('.'*40)
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

   #Load file in df
    df = pd.read_csv(CITY_DATA[city])

   # Change start time format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   #Create month and day of week variable
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

   #Create the variable time
    df['hour'] = df['Start Time'].dt.hour

    #Create the most frequent route
    df['route'] = df['Start Station'] + ' & '+ df['End Station']

   #Filter month
    if month != 'all':
        months=['january','february','march', 'april','may','june']
        month = months.index(month)+1
        df = df[df['month'] == month]

   #Filter day#
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print ('\n The month {} of the year was the most common.'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\n The most common day of week was: ', most_common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('\n The {} hour is the most common.\n'.format(most_common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('.'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station =df['Start Station'].value_counts().idxmax()
    print('\n The most commonly used start station is ', Start_Station)

    # TO DO: display most commonly used end station
    End_Station =df['End Station'].value_counts().idxmax()
    print('\n The most commonly used end station is ', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    more_frequent_trip = df['route'].mode()[0]
    print('\nThe most frequent combination of start station and end station trip is ', more_frequent_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('.'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= sum(df['Trip Duration'])
    print('\n The total travel time is {} days.\n'.format(round((total_travel_time/86400), 1)))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('\n The mean travel time is {} minutes.\n'.format(round((mean_travel_time/60), 1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('.'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('The user types are:\n', user_types)

    # TO DO: Display counts of gender
    try:
          gender_=df['Gender'].value_counts()
          print('\n The total users by gender are:\n', gender_)
    except KeyError:
          print('\n Sorry! There is no gender information for your query')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        by_earliest=df['Birth Year'].min()
        print('\n The year of birth of the oldest person who rides a bicycle is', round(by_earliest, 0))
    except KeyError:
        print('\n Sorry! There is no information for the year of birth of the older person who rides a bicycle.')

    try:
        by_most_recent=df['Birth Year'].max()
        print('\n The year of birth of the young person who uses bicycles is ', round(by_most_recent, 0))
    except KeyError:
        print('\n Sorry! There is no information on the year of birth of the young man who rides a bicycle.')

    try:
        by_most_common=df['Birth Year'].value_counts().idxmax()
        print('\n The most common year of birth for bicycle users is ', round(by_most_common, 0))
    except KeyError:
        print('\n We have no information for your query')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('.'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view=input('\n Would you like to have a view of the first 5 records of the database? indicate yes or no: ').lower()
        five_rows=0
        answer=True

        while (answer):
            print(df.iloc[five_rows:five_rows+5])
            five_rows+=5
            view = input("\n Would you like to have a view of the first 5 records of the database? indicate yes or no: ").lower()
            if view == "no":
                answer=False

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

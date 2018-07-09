
# coding: utf-8

# In[6]:


import fitbit
import gather_keys_oauth2 as Oauth2
import datetime


# In[32]:


# Authentication
USER_ID = "22D37F"
CLIENT_SECRET = "4dbd95ded6b3e02160887deb8cc4f178"
"""for obtaining Access-token and Refresh-token"""

#server = Oauth2.OAuth2Server(USER_ID, CLIENT_SECRET)
#server.browser_authorize()

ACCESS_TOKEN = "xxxxxxx"
#expires_in = 28800
REFRESH_TOKEN = "xxxxxx"


ACCESS_TOKEN = "xxxxxxx"
REFRESH_TOKEN = "xxxxxx"

# In[3]:
def get_fit_bit_data():

    # Authorization Client

    auth2_client = fitbit.Fitbit(USER_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


    # ## Define Time period

    # In[22]:


    start_date = datetime.date(2018, 5, 21)
    time_period = 7


    # ## Get Metrics

    # In[31]:


    # Calculate Resting Heart Rate, Activity Calories,

    restingHeartRate = 0
    activityCalories = 0
    totalMinutesAsleep = 0

    hr_day_count = 0.0
    ac_day_count = 0.0
    s_day_count = 0.0

    for days in range(time_period):

        day = (start_date + datetime.timedelta(days=days))
        fitbit_stats = auth2_client.activities(day)

        # Check if the data was generated
        if 'restingHeartRate' in fitbit_stats['summary']:
            restingHeartRate += fitbit_stats['summary']['restingHeartRate']
            hr_day_count += 1

        if 'activityCalories' in fitbit_stats['summary']:
            activityCalories += fitbit_stats['summary']['activityCalories']
            ac_day_count += 1

        fitbit_stats = auth2_client.sleep(day)
        if 'totalMinutesAsleep' in fitbit_stats['summary']:
            totalMinutesAsleep += fitbit_stats['summary']['totalMinutesAsleep']
            s_day_count += 1


    # Get User Info
    fitbit_stats = auth2_client.user_profile_get()


    fit_bit_data = [0]*6;

    restingHeartRate = restingHeartRate * 1.0/hr_day_count
    activityCalories = activityCalories * 1.0/ac_day_count
    totalMinutesAsleep = totalMinutesAsleep * 1.0/(60*s_day_count)
    age = fitbit_stats['user']['age']
    weight = fitbit_stats['user']['weight']
    height = fitbit_stats['user']['height']

    print('restingHeartRate', restingHeartRate)
    print('activityCalories', activityCalories)
    print('totalMinutesAsleep', totalMinutesAsleep)
    print('age', age)
    print('weight', weight)
    print('height', height)

    fit_bit_data[0] = age;
    fit_bit_data[1] = weight;
    fit_bit_data[2] = height;
    fit_bit_data[3] = restingHeartRate;
    fit_bit_data[4] = totalMinutesAsleep;
    fit_bit_data[5] = activityCalories;
    return fit_bit_data

if __name__ == "__main__":
    get_fit_bit_data()

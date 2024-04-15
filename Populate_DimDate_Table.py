from datetime import date, datetime
import pandas as pd
import sqlalchemy
import psycopg2

# start date is automatically configured to start from date of script run
# you can configure this to a minimum date of 1900-01-01
start_date = date.today().strftime('%F')
days_to_load = 2000

date_df = pd.DataFrame({"FullDate": pd.date_range("start_date", periods=days_to_load, freq="D")})
date_df["Date_ID"] = date_df.FullDate.dt.strftime("%Y%m%d")
date_df["Year"] = date_df.FullDate.dt.year
date_df["Day"] = date_df.FullDate.dt.day
date_df["Month"] = date_df.FullDate.dt.month
date_df["DayofWeek"] = date_df.FullDate.dt.day_of_week
date_df["IsWeekday"] = date_df["DayofWeek"] < 5
date_df["MonthName"] = date_df.FullDate.dt.month_name()
date_df["DayofWeekName"] = date_df.FullDate.dt.day_name()

date_df = date_df[["Date_ID", "Year", "Day", "Month", "FullDate", "IsWeekday", "DayofWeek", "MonthName", "DayofWeekName"]]

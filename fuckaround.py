import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

data = {
  "calories": [420, 380, 390, 425],
  "duration": [50, 40, 45, 67]
}
print(data)
#load data into a DataFrame object:
df = pd.DataFrame(data, index = ["2026-06-27", "2026-06-28", "2026-06-29", "2026-06-30"])

print(df)
#idk = df.loc[f"2026-06-27"] + df.loc[f"2026-06-28"]
#print(idk)

b = df.loc[f"{date.today()}", "duration"]

def docoolstuff(input):
  input = pd.DataFrame(input)
  if input - relativedelta(days = 1) == None: #skip if there is no relative delta from 2 days ago
    a = 0
  else:
    for x in input:
    #divide the soonest date by the date from 2 days ago
      a = input.loc[f"{x}"] / (input.loc[f"{x}"] - relativedelta(days = 1))
    
  print(a)

#print(calendar.month_abbr[date.today().month])

def idk(input):
  df = pd.DataFrame(input)
  um = df.loc["2026-06-30"].sort_values(ascending=True)
  matcha = um.nlargest(3).index
  print(matcha)
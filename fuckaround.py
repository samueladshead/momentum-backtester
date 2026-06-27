import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data, index = ["2025-03-04", "2025-03-05", "2025-03-06"])

print(df)
#print(df.loc["2025-03-04","duration"])
'''
row1 = df.iloc[0]
row2 = df.iloc[1]
hmm = row1 + row2
print(hmm)
hmm = hmm.transpose(hmm)
idk = pd.DataFrame(hmm, index = ['Results'] )

print(idk)
'''

end = date.today() - relativedelta(days=(date.today().day)) - relativedelta(months = date.today().month-1)
print(end)
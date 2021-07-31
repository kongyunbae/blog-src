import pandas as pd
from numpy.random import *
from faker import Faker


# faker object
faker = Faker('ja_JP')

# make csv file
csv_list = []

# name, email row
for _ in range(300):
    name = faker.name()
    email = faker.email()
    csv_list.append([name, email])
df = pd.DataFrame(csv_list,columns=['名前', 'メールアドレス'])

# age row
age_list = randint(20, 69, 300)
df['年齢'] = pd.DataFrame(age_list)

# sex row
sex = ['男', '女']
sex_list = choice(sex, 300, p=[0.5, 0.5])
df['性別'] = pd.DataFrame(sex_list)

# point rows
event_point_list = randint(1, 6, 300)
event_place_point_list = randint(1, 6, 300)
df['イベント満足度'] = pd.DataFrame(event_point_list)
df['イベント会場評価'] = pd.DataFrame(event_place_point_list)

# export data frame to csv file
df.to_csv('./src/sample_file_n.txt', header=False, index=False)

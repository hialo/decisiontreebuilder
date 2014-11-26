import pandas as pd
import numpy as np
import string as st
from scipy.stats import mode

# Script created to clean the Titanic database and do Feature Engineering.

#################################################################################

def verifyingDataConsistency(df, column, choice):
    df[column] = df[column].fillna(0.0)
    target = '/home/hialo/UnB/TCC2/codes/databases/' + column + '_data.csv'
    target_sorted = '/home/hialo/UnB/TCC2/codes/databases/' + column + '_data_sorted.csv'

    if (column == 'age'):
        new_df = df[[column]]
        new_df_sorted = new_df.sort([column])

        pdf = pd.DataFrame(new_df_sorted)
        pdf.to_csv(target_sorted, index = False)

    elif (column == 'fare'):
        new_df = df[['pclass', column]]
        new_df = new_df.apply(lambda x: x['fare'] if x['pclass'] == choice else 0, axis = 1)

        target = '/home/hialo/UnB/TCC2/codes/databases/' + column + '_data_pclass' + str(choice) + '.csv'

    pdf = pd.DataFrame(new_df)
    pdf.to_csv(target, index = False)


##################################################################################

def finding_substring(full_string, substr):
    for substring in substr:
        if st.find(full_string, substring) != -1:
            return substring
    return np.nan

#################################################################################

def clearingQuotes(df):
    df.name = df.name.map(lambda x: str(x).replace(',', '-'))
    df.name = df.name.map(lambda x: str(x).replace('"', ''))

    df['surname'] = df.name.map(lambda x: str(x).split("-")[0])
    df.name = df.name.map(lambda x: str(x).split("-")[1])

    df.home_dest = df.home_dest.fillna('Unknown')
    df.home_dest = df.home_dest.map(lambda x: str(x).replace(',', ' -'))
    df.home_dest = df.home_dest.map(lambda x: str(x).replace('"', ''))

    return df

#################################################################################

def clean_database(df):
    df = clearingQuotes(df)

    mean_age = np.mean(df.age)
    df.age = df.age.fillna(mean_age)
    
    df.fare = df.fare.map(lambda x: np.nan if x == 0 else x)
    classmeans = df.pivot_table('fare', rows='pclass', aggfunc='mean')
    df.fare = df[['fare', 'pclass']].apply(lambda x: classmeans[x['pclass']] if pd.isnull(x['fare']) else x['fare'], axis = 1)
    
    df.cabin = df.cabin.fillna('Unknown')

    embarked = mode(df.embarked)[0][0]
    df.embarked = df.embarked.fillna(embarked)

    df.boat = df.boat.fillna('Unknown')
    
    df.body = df.body.fillna('0')

    return df 

#################################################################################

def clean_database_round1(df):
    df = clean_database(df)

    df = df[['pclass', 'name', 'surname', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home_dest', 'survived']]

    return df

#################################################################################


def clean_database_round2(df):
    df = clean_database(df)

    df = df[['pclass', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'body','home_dest', 'survived']]

    return df

#################################################################################


def clean_database_round3(df):
    df = clean_database(df)

    df['family'] = df.sibsp + df.parch

    cabin_list = ['A', 'B', 'C', 'D', 'E', 'F', 'T', 'G', 'U']
    df['deck'] = df.cabin.map(lambda x: finding_substring(x, cabin_list))

    df = df[['pclass', 'sex', 'age', 'family', 'deck', 'ticket', 'fare', 'embarked', 'home_dest', 'survived']]

    return df


#################################################################################

def main():
    path = '/home/hialo/UnB/TCC2/codes/databases/titanic.csv'
    target = '/home/hialo/UnB/TCC2/codes/databases/titanic3.csv'

    df = pd.read_csv(path)

    #verifyingDataConsistency(df, 'fare', 1)
    
    df = clean_database_round2(df)

    predictiondf = pd.DataFrame(df)

    predictiondf.to_csv(target, index = False)
    
main()
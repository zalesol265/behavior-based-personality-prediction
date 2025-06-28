import pandas as pd



def remove_group_outliers(df, group_col, numeric_cols, method='iqr', threshold=1.5, remove=True):

    df_out = df.copy()
    df_out['is_outlier'] = False

    for label in df_out[group_col].unique():
        group_df = df_out[df_out[group_col] == label]

        for col in numeric_cols:
            Q1 = group_df[col].quantile(0.25)
            Q3 = group_df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - threshold * IQR
            upper = Q3 + threshold * IQR

            # Mark as outlier
            condition = (df_out[group_col] == label) & ((df_out[col] < lower) | (df_out[col] > upper))
            df_out.loc[condition, 'is_outlier'] = True

    if remove:
        return df_out[~df_out['is_outlier']].drop(columns='is_outlier')
    else:
        return df_out


def load_and_clean_data(path='../data/personality_dataset.csv'):

    df = pd.read_csv(path)

    # Convert categorical string values to numeric
    df['Stage_fear'] = df['Stage_fear'].map({'Yes': 1, 'No': 0})
    df['Drained_after_socializing'] = df['Drained_after_socializing'].map({'Yes': 1, 'No': 0})
    df['Personality'] = df['Personality'].map({'Extrovert': 1, 'Introvert': 0})

    return df

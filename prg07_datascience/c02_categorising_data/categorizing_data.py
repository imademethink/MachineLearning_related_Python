#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# get the  data from csv file
base_path = '/home/imademethink/prg_datascience/c02_categorising_data/'
file_non_categorical_data = base_path + 'non_categorical_data.csv'

non_categorical_dataset_df = pd.read_csv(file_non_categorical_data,
                                      header='infer',sep=',',index_col=False,
                                      dtype = 'object')
print(type(non_categorical_dataset_df))
print(non_categorical_dataset_df.shape)
print(non_categorical_dataset_df)




#----------------------------------------------------------------
# categorisation using simple find and replace
required_objects_df                     = non_categorical_dataset_df.select_dtypes(include=['object']).copy()
required_objects_df.head()
# count occurance of respective items
print(required_objects_df["department_id"].value_counts())
# for now simply replace dataqa --> 400 and datadev --> 200
find_replace_dictionary                 = {"department_id":     {"deptqa": 400, "deptdev": 200}}
required_objects_df.replace(find_replace_dictionary, inplace=True)
print(required_objects_df)
print(type(required_objects_df))


#----------------------------------------------------------------
# categorisation using LabelEncoder fit_transform() method
nparr_non_categorical_department_id     = non_categorical_dataset_df.iloc[:, 1].values
print(nparr_non_categorical_department_id)
labelencoder_department_id              = LabelEncoder()
categorical_department_id               = labelencoder_department_id.fit_transform(nparr_non_categorical_department_id)
print(categorical_department_id)
print(categorical_department_id.dtype)


#----------------------------------------------------------------
# categorisation using OneHotEncoder
nparr_non_categorical_department_id     = non_categorical_dataset_df.iloc[:, 1].values
labelencoder_department_id              = LabelEncoder()
categorical_department_id               = labelencoder_department_id.fit_transform(nparr_non_categorical_department_id)
print(categorical_department_id.shape)
print(categorical_department_id)
# reshape to 1 coloumn
categorical_department_id               = categorical_department_id.reshape(len(categorical_department_id), 1)
onehotencoder_dept_id                   = OneHotEncoder(sparse=False)
onehot_encoded                          = onehotencoder_dept_id.fit_transform(categorical_department_id)
print(type(onehot_encoded))
print(onehot_encoded.dtype)
print(onehot_encoded)



#----------------------------------------------------------------
# One hot encodind simplified approach - for categorical data
nparr_non_categorical_department_id     = non_categorical_dataset_df.iloc[:, 1].values
categorical_department_id               = pd.get_dummies(nparr_non_categorical_department_id)
print(type(categorical_department_id))
print(categorical_department_id.shape)
print(categorical_department_id)






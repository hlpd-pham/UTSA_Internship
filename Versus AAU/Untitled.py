#import numpy as np
import pandas as pd

total_research = pd.read_excel('total_research.xlsx')
federal_research = pd.read_excel('federal_research.xlsx')
endowment_asserts = pd.read_excel('endowment_assets.xlsx')
annual_giving = pd.read_excel('annual_giving.xlsx')
natl_academy = pd.read_excel('natl_academy.xlsx')
falcuty_awards = pd.read_excel('faculty_awards.xlsx')
dr_awards = pd.read_excel('doctorates.xlsx')
postdocs = pd.read_excel('postdocs.xlsx')


data_2015 = [endowment_asserts, annual_giving,
       natl_academy, falcuty_awards, dr_awards]
data_2014 = [total_research, federal_research, postdocs]

for dataset in data_2015:
    dataset.columns = dataset.iloc[0]
    dataset = dataset.reindex(dataset.index.drop(0))

for dataset in data_2014:
    dataset.columns = dataset.iloc[0]
    dataset = dataset.reindex(dataset.index.drop(0))

total_research.head(2)

utsa = total_research["Institutions Reporting Any\nFederal Research in Past Five Years\n(in Alphabetical Order)"] == 'University of Texas - San Antonio'

utsa_1st = {}
for dataset in data_2015:
    utsa_1st[dataset.columns[4]] = dataset[utsa].iloc[:,4].values[0]




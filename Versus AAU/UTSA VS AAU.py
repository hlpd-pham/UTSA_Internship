import numpy as np
import pandas as pd

total_research = pd.read_excel('total_research.xlsx')
federal_research = pd.read_excel('federal_research.xlsx')
endowment_asserts = pd.read_excel('endowment_assets.xlsx')
annual_giving = pd.read_excel('annual_giving.xlsx')
natl_academy = pd.read_excel('natl_academy.xlsx')
faculty_awards = pd.read_excel('faculty_awards.xlsx')
dr_awards = pd.read_excel('doctorates.xlsx')
postdocs = pd.read_excel('postdocs.xlsx')


data = [endowment_asserts, annual_giving, natl_academy, faculty_awards, dr_awards,
        total_research, federal_research, postdocs]
data_2015 = [endowment_asserts, annual_giving,
       natl_academy, faculty_awards, dr_awards]
data_2014 = [total_research, federal_research, postdocs]

for dataset in data_2015:
    dataset.columns = dataset.iloc[0]
    dataset = dataset.reindex(dataset.index.drop(0))
for dataset in data_2014:
    dataset.columns = dataset.iloc[0]
    dataset = dataset.reindex(dataset.index.drop(0))

total_research.columns[3]

merge_col = 'Institutions Reporting Any\nFederal Research in Past Five Years\n(in Alphabetical Order)'


new_df = pd.merge(total_research,federal_research,on=merge_col)
new_df = pd.merge(new_df,endowment_asserts,on=merge_col)
new_df = pd.merge(new_df,annual_giving,on=merge_col)
new_df = pd.merge(new_df,natl_academy,on=merge_col)
new_df = pd.merge(new_df,faculty_awards,on=merge_col)
new_df = pd.merge(new_df,dr_awards,on=merge_col)
new_df = pd.merge(new_df,postdocs,on=merge_col)
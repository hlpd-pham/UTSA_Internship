
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


total_research = pd.read_excel('total_research.xlsx')
federal_research = pd.read_excel('federal_research.xlsx')
endowment_asserts = pd.read_excel('endowment_assets.xlsx')
annual_giving = pd.read_excel('annual_giving.xlsx')
natl_academy = pd.read_excel('natl_academy.xlsx')
faculty_awards = pd.read_excel('faculty_awards.xlsx')
dr_awards = pd.read_excel('doctorates.xlsx')
postdocs = pd.read_excel('postdocs.xlsx')


# In[3]:


data = [endowment_asserts, annual_giving, natl_academy, faculty_awards, dr_awards,
        total_research, federal_research, postdocs]
data_2015 = [endowment_asserts, annual_giving,
       natl_academy, faculty_awards, dr_awards]
data_2014 = [total_research, federal_research, postdocs]


# In[4]:


for dataset in data_2015:
    dataset.columns = dataset.iloc[0]
    dataset = dataset.reindex(dataset.index.drop(0))
for dataset in data_2014:
    dataset.columns = dataset.iloc[0]
    dataset = dataset.reindex(dataset.index.drop(0))


# In[5]:


total_research.head(2)


# In[6]:


utsa = total_research["Institutions Reporting Any\nFederal Research in Past Five Years\n(in Alphabetical Order)"] == 'University of Texas - San Antonio'


# In[7]:


total_research[utsa]


# In[8]:


utsa_1st = {}
for dataset in data_2015:
    utsa_1st[dataset.columns[4]] = dataset[utsa].iloc[:,4].values[0]
for dataset in data_2014:
    utsa_1st[dataset.columns[4]] = dataset[utsa].iloc[:,4].values[0]


# In[9]:


utsa_1st


# In[10]:


utsa_2nd = {}
for dataset in data_2015:
    utsa_2nd[dataset.columns[7]] = dataset[utsa].iloc[:,7].values[0]
for dataset in data_2014:
    utsa_2nd[dataset.columns[7]] = dataset[utsa].iloc[:,7].values[0]
utsa_2nd


# In[11]:


utsa_3rd = {}
for dataset in data_2015:
    utsa_3rd[dataset.columns[10]] = dataset[utsa].iloc[:,10].values[0]
for dataset in data_2014:
    utsa_3rd[dataset.columns[10]] = dataset[utsa].iloc[:,10].values[0]
utsa_3rd


# In[12]:


utsa_4th = {}
for dataset in data_2015:
    utsa_4th[dataset.columns[13]] = dataset[utsa].iloc[:,13].values[0]
for dataset in data_2014:
    utsa_4th[dataset.columns[13]] = dataset[utsa].iloc[:,13].values[0]
utsa_4th


# In[13]:


utsa_5th = {}
for dataset in data_2015:
    utsa_5th[dataset.columns[16]] = dataset[utsa].iloc[:,16].values[0]
for dataset in data_2014:
    utsa_5th[dataset.columns[16]] = dataset[utsa].iloc[:,16].values[0]
utsa_5th


# In[14]:


index_col = ['Endowment Assets x $1000','Annual Giving x $1000','National Academy Members',
             'Faculty Awards','Doctorates Awared','Total Research x $1000', 'Federal Research x $1000',
             'Postdoctoral Appointees']


# In[15]:


list(utsa_1st.values())


# In[16]:


utsa_dict = { 'Measure': index_col,'Year 2015 - 2014' : list(utsa_1st.values()),
            'Year 2014 - 2013': np.array(list(utsa_2nd.values())).astype(int),'Year 2013 - 2012': list(utsa_3rd.values()), 
            'Year 2012 - 2011': list(utsa_4th.values()),'Year 2011 - 2010': list(utsa_5th.values()),
          }


# In[17]:


pd.DataFrame.from_dict(utsa_dict)


# In[18]:


AAU_df = pd.read_excel('AAU.xlsx',sheet_name='Total Research 2008')


# In[19]:


AAU_df.head()


# In[20]:


AAU_list = AAU_df['Institution'].values


# In[21]:


AAU_list


# In[22]:


col_name = "Institutions Reporting Any\nFederal Research in Past Five Years\n(in Alphabetical Order)"


# **Get different dataframe for AAU list**

# In[23]:


AAU_total_research = total_research[total_research[col_name].isin(AAU_list)].copy()


# In[24]:


AAU_total_research.drop(AAU_total_research.columns[0],axis=1,inplace=True)


# In[25]:


AAU_fed_research = federal_research[federal_research[col_name].isin(AAU_list)].copy().drop(federal_research.columns[0],axis=1)


# In[26]:


AAU_endow_assets = endowment_asserts[endowment_asserts[col_name].isin(AAU_list)].copy()


# In[27]:


AAU_endow_assets.drop(AAU_endow_assets.columns[0],axis=1,inplace=True)


# In[28]:


AAU_annual_giving = annual_giving[annual_giving[col_name].isin(AAU_list)].copy()


# In[29]:


AAU_annual_giving.drop(AAU_annual_giving.columns[0],axis=1,inplace=True)


# In[30]:


AAU_nat_member = natl_academy[natl_academy[col_name].isin(AAU_list)].copy()


# In[31]:


AAU_nat_member.drop(AAU_nat_member.columns[0],axis=1,inplace=True)


# In[32]:


AAU_fac_award = faculty_awards[faculty_awards[col_name].isin(AAU_list)].copy()


# In[33]:


AAU_fac_award.drop(AAU_fac_award.columns[0],axis=1,inplace=True)


# In[34]:


AAU_doc_award = dr_awards[dr_awards[col_name].isin(AAU_list)].copy()


# In[35]:


AAU_doc_award.drop(AAU_doc_award.columns[0],axis=1,inplace=True)


# In[36]:


AAU_postdoc = postdocs[postdocs[col_name].isin(AAU_list)].copy()


# In[37]:


AAU_postdoc.drop(AAU_postdoc.columns[0],axis=1,inplace=True)


# **Total Research for AAU In Year 15-14**

# In[38]:


search_string = '2014\n***\nTotal Research \n x $1000'


# In[39]:


TResearch_1514_20th = np.percentile(AAU_total_research[search_string],[0,20])


# In[40]:


#Average Total Research for AAU Univerisiies in 2014 (0th-20th)
AAU_total_research[(AAU_total_research[search_string] >= TResearch_1514_20th[0]) & (AAU_total_research[search_string] <= TResearch_1514_20th[1])][search_string].mean().astype(int)


# In[41]:


TResearch_1514_40th = np.percentile(AAU_total_research[search_string],[21,40])


# In[42]:


#Average Total Research for AAU Univerisiies in 2014 (21st-40th)
AAU_total_research[(AAU_total_research[search_string] >= TResearch_1514_40th[0]) & (AAU_total_research[search_string] <= TResearch_1514_40th[1])][search_string].mean().astype(int)


# In[43]:


TResearch_1514_60th = np.percentile(AAU_total_research[search_string],[41,60])


# In[44]:


#Average Total Research for AAU Univerisiies in 2014 (41st-60th)
AAU_total_research[(AAU_total_research[search_string] >= TResearch_1514_60th[0]) & (AAU_total_research[search_string] <= TResearch_1514_60th[1])][search_string].mean().astype(int)


# In[45]:


TResearch_1514_80th = np.percentile(AAU_total_research[search_string],[61,80])


# In[46]:


#Average Total Research for AAU Univerisiies in 2014 (61st-80th)
AAU_total_research[(AAU_total_research[search_string] >= TResearch_1514_80th[0]) & (AAU_total_research[search_string] <= TResearch_1514_80th[1])][search_string].mean().astype(int)


# In[47]:


TResearch_1514_100th = np.percentile(AAU_total_research[search_string],[81,100])


# In[48]:


#Average Total Research for AAU Univerisiies in 2014 (61st-80th)
AAU_total_research[(AAU_total_research[search_string] >= TResearch_1514_100th[0]) & 
                   (AAU_total_research[search_string] <= TResearch_1514_100th[1])][search_string].mean().astype(int)


# In[49]:


AAU_total_research[[col_name,search_string]].sort_values(by=col_name)


# In[50]:


aau_research_2014 = AAU_total_research[[col_name,search_string]].sort_values(by=search_string)
aau_research_2014.columns = ['Institution','Total Research x $1000']


# In[51]:


writer = pd.ExcelWriter('UTSA vs AAU.xlsx')
aau_research_2014.to_excel(writer,'Total Research 2014')
# six_year.to_excel(writer,'6-year')
# writer.save()


# **Federal Research for AAU In Year 15-14**

# In[52]:


search_string_1 = '2014\n***\nFederal Research \n x $1000'


# In[53]:


FResearch_1514_20th = np.percentile(AAU_fed_research[search_string_1],[0,20])


# In[54]:


#Average Federal Research for AAU Univerisiies in 2014 (0th-20th)
AAU_fed_research[(AAU_fed_research[search_string_1] >= FResearch_1514_20th[0]) & (AAU_fed_research[search_string_1] <= FResearch_1514_20th[1])][search_string_1].mean().astype(int)


# In[55]:


FResearch_1514_40th = np.percentile(AAU_fed_research[search_string_1],[21,40])


# In[56]:


#Average Federal Research for AAU Univerisiies in 2014 (21st-40th)
AAU_fed_research[(AAU_fed_research[search_string_1] >= FResearch_1514_40th[0]) & (AAU_fed_research[search_string_1] <= FResearch_1514_40th[1])][search_string_1].mean().astype(int)


# In[57]:


FResearch_1514_60th = np.percentile(AAU_fed_research[search_string_1],[41,60])


# In[58]:


#Average Federal Research for AAU Univerisiies in 2014 (41st-60th)
AAU_fed_research[(AAU_fed_research[search_string_1] >= FResearch_1514_60th[0]) & (AAU_fed_research[search_string_1] <= FResearch_1514_60th[1])][search_string_1].mean().astype(int)


# In[59]:


FResearch_1514_80th = np.percentile(AAU_fed_research[search_string_1],[61,80])


# In[60]:


#Average Federal Research for AAU Univerisiies in 2014 (61st-80th)
AAU_fed_research[(AAU_fed_research[search_string_1] >= FResearch_1514_80th[0]) & (AAU_fed_research[search_string_1] <= FResearch_1514_80th[1])][search_string_1].mean().astype(int)


# In[61]:


FResearch_1514_100th = np.percentile(AAU_fed_research[search_string_1],[81,100])


# In[62]:


#Average Federal Research for AAU Univerisiies in 2014 (61st-80th)
AAU_fed_research[(AAU_fed_research[search_string_1] >= FResearch_1514_100th[0]) & (AAU_fed_research[search_string_1] <= FResearch_1514_100th[1])][search_string_1].mean().astype(int)


# In[63]:


#Average Federal Research for AAU Univerisiies in 2014 (21st-40th)
AAU_fed_research[[col_name,search_string_1]].sort_values(by=search_string_1)


# In[64]:


aau_federal_2014 = AAU_fed_research[[col_name,search_string_1]].sort_values(by=search_string_1)
aau_federal_2014.columns = ['Institution','Federal Research']


# In[65]:


aau_research_2014.to_excel(writer,'Federal Research 2014')


# **Endowmen Assets for AAU In Year 15-14**

# In[66]:


searh_string_2 = '2015\n***\nEndowment Assets \n x $1000'


# In[67]:


Assets_1514_20th = np.percentile(AAU_endow_assets[searh_string_2],[0,20])


# In[68]:


#Average Endowment Assets for AAU Univerisiies in 2015 (0tt-20th)
AAU_endow_assets[(AAU_endow_assets[searh_string_2] >= Assets_1514_20th[0]) & (AAU_endow_assets[searh_string_2] <= Assets_1514_20th[1])][searh_string_2].mean().astype(int)


# In[69]:


Assets_1514_40th = np.percentile(AAU_endow_assets[searh_string_2],[21,40])


# In[70]:


#Average Endowment Assets for AAU Univerisiies in 2015 (21st-40th)
AAU_endow_assets[(AAU_endow_assets[searh_string_2] >= Assets_1514_40th[0]) & (AAU_endow_assets[searh_string_2] <= Assets_1514_40th[1])][searh_string_2].mean().astype(int)


# In[71]:


Assets_1514_60th = np.percentile(AAU_endow_assets[searh_string_2],[41,60])


# In[72]:


#Average Endowment Assets for AAU Univerisiies in 2015 (41st-60th)
AAU_endow_assets[(AAU_endow_assets[searh_string_2] >= Assets_1514_60th[0]) & (AAU_endow_assets[searh_string_2] <= Assets_1514_60th[1])][searh_string_2].mean().astype(int)


# In[73]:


Assets_1514_80th = np.percentile(AAU_endow_assets[searh_string_2],[61,80])


# In[74]:


#Average Endowment Assets for AAU Univerisiies in 2015 (61st-80th)
AAU_endow_assets[(AAU_endow_assets[searh_string_2] >= Assets_1514_80th[0]) & (AAU_endow_assets[searh_string_2] <= Assets_1514_80th[1])][searh_string_2].mean().astype(int)


# In[75]:


Assets_1514_100th = np.percentile(AAU_endow_assets[searh_string_2],[61,80])


# In[76]:


#Average Endowment Assets for AAU Univerisiies in 2015 (81st-100th)
AAU_endow_assets[(AAU_endow_assets[searh_string_2] >= Assets_1514_100th[0]) & (AAU_endow_assets[searh_string_2] <= Assets_1514_100th[1])][searh_string_2].mean().astype(int)


# In[77]:


aau_assets_2015 = AAU_endow_assets[[col_name,searh_string_2]].sort_values(by=searh_string_2)
aau_assets_2015.columns = ['Institution','Endowment Assets']


# In[78]:


aau_assets_2015.to_excel(writer,'Endowment 2015')


# **Annual Giving for AAU In Year 15-14**

# In[79]:


search_string_3 = '2015\n***\nAnnual Giving \n x $1000'


# In[80]:


giving_2015_20th = np.percentile(AAU_annual_giving[search_string_3],[0,20])


# In[81]:


#Average Annual Giving for AAU Univerisiies in 2015 (0th-20th)
AAU_annual_giving[(AAU_annual_giving[search_string_3] >= giving_2015_20th[0]) &
                 (AAU_annual_giving[search_string_3] <= giving_2015_20th[1])][search_string_3].mean().astype(int)


# In[82]:


giving_2015_40th = np.percentile(AAU_annual_giving[search_string_3],[21,40])


# In[83]:


#Average Annual Giving for AAU Univerisiies in 2015 (21st-40th)
AAU_annual_giving[(AAU_annual_giving[search_string_3] >= giving_2015_40th[0]) &
                  (AAU_annual_giving[search_string_3] <= giving_2015_40th[1])][search_string_3].mean().astype(int)


# In[84]:


giving_2015_60th = np.percentile(AAU_annual_giving[search_string_3],[41,60])


# In[85]:


#Average Annual Giving for AAU Univerisiies in 2015 (41st-60th)
AAU_annual_giving[(AAU_annual_giving[search_string_3] >= giving_2015_60th[0]) &
                  (AAU_annual_giving[search_string_3] <= giving_2015_60th[1])][search_string_3].mean().astype(int)


# In[86]:


giving_2015_80th = np.percentile(AAU_annual_giving[search_string_3],[61,80])


# In[87]:


#Average Annual Giving for AAU Univerisiies in 2015 (61st-80th)
AAU_annual_giving[(AAU_annual_giving[search_string_3] >= giving_2015_80th[0]) &
                  (AAU_annual_giving[search_string_3] <= giving_2015_80th[1])][search_string_3].mean().astype(int)


# In[88]:


giving_2015_100th = np.percentile(AAU_annual_giving[search_string_3],[81,100])


# In[89]:


#Average Annual Giving for AAU Univerisiies in 2015 (81st-100th)
AAU_annual_giving[(AAU_annual_giving[search_string_3] >= giving_2015_100th[0]) &
                  (AAU_annual_giving[search_string_3] <= giving_2015_100th[1])][search_string_3].mean().astype(int)


# In[90]:


aau_giving_2015 = AAU_annual_giving[[col_name,search_string_3]].sort_values(by=search_string_3)
aau_giving_2015.columns = ['Institution', 'Annual Giving']


# In[91]:


aau_giving_2015.to_excel(writer,'Annual Giving 2015')


# **National Academy Members for AAU In Year 15-14**

# In[92]:


search_string_4 = '2015\n***\nAcademy Members'


# In[93]:


member_2015_20th = np.percentile(AAU_nat_member[search_string_4],[0,20])


# In[94]:


#Average National Academy Members for AAU Univerisiies in 2015 (0th-20th)
AAU_nat_member[(AAU_nat_member[search_string_4] >= member_2015_20th[0]) &
               (AAU_nat_member[search_string_4] <= member_2015_20th[1])][search_string_4].mean().astype(int)


# In[95]:


member_2015_40th = np.percentile(AAU_nat_member[search_string_4],[21,40])


# In[96]:


#Average National Academy Members for AAU Univerisiies in 2015 (21st-40th)
AAU_nat_member[(AAU_nat_member[search_string_4] >= member_2015_40th[0]) &
               (AAU_nat_member[search_string_4] <= member_2015_40th[1])][search_string_4].mean().astype(int)


# In[97]:


member_2015_60th = np.percentile(AAU_nat_member[search_string_4],[41,60])


# In[98]:


#Average National Academy Members for AAU Univerisiies in 2015 (41st-60th)
AAU_nat_member[(AAU_nat_member[search_string_4] >= member_2015_60th[0]) &
               (AAU_nat_member[search_string_4] <= member_2015_60th[1])][search_string_4].mean().astype(int)


# In[99]:


member_2015_80th = np.percentile(AAU_nat_member[search_string_4],[61,80])


# In[100]:


#Average National Academy Members for AAU Univerisiies in 2015 (61st-80th)
AAU_nat_member[(AAU_nat_member[search_string_4] >= member_2015_80th[0]) &
               (AAU_nat_member[search_string_4] <= member_2015_80th[1])][search_string_4].mean().astype(int)


# In[101]:


member_2015_100th = np.percentile(AAU_nat_member[search_string_4],[81,100])


# In[102]:


#Average National Academy Members for AAU Univerisiies in 2015 (61st-80th)
AAU_nat_member[(AAU_nat_member[search_string_4] >= member_2015_100th[0]) &
               (AAU_nat_member[search_string_4] <= member_2015_100th[1])][search_string_4].mean().astype(int)


# In[103]:


aau_member_2015 = AAU_nat_member[[col_name,search_string_4]].sort_values(by=search_string_4)
aau_member_2015.columns = ['Institution', 'National Academy Members']
aau_member_2015.to_excel(writer,'National Academy Members 2015')


# **Faculty Awards 2015 (AAU)**

# In[104]:


search_string_5 = '2015\n***\nFaculty Awards'


# In[105]:


fac_2015_20th = np.percentile(AAU_fac_award[search_string_5],[0,20])


# In[106]:


#Average Faculty Awards for AAU Univerisiies in 2015 0-20
AAU_fac_award[(AAU_fac_award[search_string_5] >= fac_2015_20th[0]) &
               (AAU_fac_award[search_string_5] <= fac_2015_20th[1])][search_string_5].sort_values().mean().astype(int)


# In[107]:


fac_2015_40th = np.percentile(AAU_fac_award[search_string_5],[21,40])


# In[108]:


#Average Faculty Awards for AAU Univerisiies in 2015 21-40
AAU_fac_award[(AAU_fac_award[search_string_5] >= fac_2015_40th[0]) &
              (AAU_fac_award[search_string_5] <= fac_2015_40th[1])][search_string_5].sort_values().mean().astype(int)


# In[109]:


fac_2015_60th = np.percentile(AAU_fac_award[search_string_5],[41,60])


# In[110]:


#Average Faculty Awards for AAU Univerisiies in 2015 41-60
AAU_fac_award[(AAU_fac_award[search_string_5] >= fac_2015_60th[0]) &
              (AAU_fac_award[search_string_5] <= fac_2015_60th[1])][search_string_5].sort_values().mean().astype(int)


# In[111]:


fac_2015_80th = np.percentile(AAU_fac_award[search_string_5],[61,80])


# In[112]:


#Average Faculty Awards for AAU Univerisiies in 2015 61-80
AAU_fac_award[(AAU_fac_award[search_string_5] >= fac_2015_80th[0]) &
              (AAU_fac_award[search_string_5] <= fac_2015_80th[1])][search_string_5].sort_values().mean().astype(int)


# In[113]:


fac_2015_100th = np.percentile(AAU_fac_award[search_string_5],[81,100])


# In[114]:


#Average Faculty Awards for AAU Univerisiies in 2015 81-100
AAU_fac_award[(AAU_fac_award[search_string_5] >= fac_2015_100th[0]) &
              (AAU_fac_award[search_string_5] <= fac_2015_100th[1])][search_string_5].sort_values().mean().astype(int)


# In[115]:


aau_award_2015 = AAU_fac_award[[col_name,search_string_5]].sort_values(by=search_string_5)
aau_award_2015.columns = ['Institution', 'Faculty Awards']
aau_award_2015.to_excel(writer,'Faculty Awards 2015')


# **Doctorates Granted 2015**

# In[116]:


search_string_6 = '2015\n***\nDoctorates'


# In[117]:


dr_2015_20th = np.percentile(AAU_doc_award[search_string_6],[0,20])


# In[118]:


#Average PhD Awards for AAU Univerisiies in 2015 0-20
AAU_doc_award[(AAU_doc_award[search_string_6] >= dr_2015_20th[0]) &
              (AAU_doc_award[search_string_6] <= dr_2015_20th[1])][search_string_6].sort_values().mean().astype(int)


# In[119]:


dr_2015_40th = np.percentile(AAU_doc_award[search_string_6],[21,40])


# In[120]:


#Average PhD Awards for AAU Univerisiies in 2015 21-40
AAU_doc_award[(AAU_doc_award[search_string_6] >= dr_2015_40th[0]) &
              (AAU_doc_award[search_string_6] <= dr_2015_40th[1])][search_string_6].sort_values().mean().astype(int)


# In[121]:


dr_2015_60th = np.percentile(AAU_doc_award[search_string_6],[41,60])


# In[122]:


#Average PhD Awards for AAU Univerisiies in 2015 41-60
AAU_doc_award[(AAU_doc_award[search_string_6] >= dr_2015_40th[0]) &
              (AAU_doc_award[search_string_6] <= dr_2015_40th[1])][search_string_6].sort_values().mean().astype(int)


# In[123]:


dr_2015_80th = np.percentile(AAU_doc_award[search_string_6],[61,80])


# In[124]:


#Average PhD Awards for AAU Univerisiies in 2015 61-80
AAU_doc_award[(AAU_doc_award[search_string_6] >= dr_2015_80th[0]) &
              (AAU_doc_award[search_string_6] <= dr_2015_80th[1])][search_string_6].sort_values().mean().astype(int)


# In[125]:


dr_2015_100th = np.percentile(AAU_doc_award[search_string_6],[81,100])


# In[126]:


#Average PhD Awards for AAU Univerisiies in 2015 81-100
AAU_doc_award[(AAU_doc_award[search_string_6] >= dr_2015_100th[0]) &
              (AAU_doc_award[search_string_6] <= dr_2015_100th[1])][search_string_6].sort_values().mean().astype(int)


# In[127]:


aau_dr_2015 = AAU_doc_award[[col_name,search_string_6]].sort_values(by=search_string_6)
aau_dr_2015.columns = ['Institution', 'Doctorates Awards']
aau_dr_2015.to_excel(writer,'Doctorates Awards 2015')


# **Postdoctoral Appointees 2014**

# In[128]:


search_string_7 = '2014\n***\nPostdocs'


# In[129]:


postdr_2014_20th = np.percentile(AAU_postdoc[search_string_7],[0,20])


# In[130]:


#Average Postdoc Appointees for AAU Univerisiies in 2008 0-20
AAU_postdoc[(AAU_postdoc[search_string_7] >= postdr_2014_20th[0]) &
            (AAU_postdoc[search_string_7] <= postdr_2014_20th[1])][search_string_7].sort_values().mean().astype(int)


# In[131]:


postdr_2014_40th = np.percentile(AAU_postdoc[search_string_7],[21,40])


# In[132]:


#Average Postdoc Appointees for AAU Univerisiies in 2008 21-40
AAU_postdoc[(AAU_postdoc[search_string_7] >= postdr_2014_40th[0]) &
            (AAU_postdoc[search_string_7] <= postdr_2014_40th[1])][search_string_7].sort_values().mean().astype(int)


# In[133]:


postdr_2014_60th = np.percentile(AAU_postdoc[search_string_7],[41,60])


# In[134]:


#Average Postdoc Appointees for AAU Univerisiies in 2008 41-60
AAU_postdoc[(AAU_postdoc[search_string_7] >= postdr_2014_60th[0]) &
            (AAU_postdoc[search_string_7] <= postdr_2014_60th[1])][search_string_7].sort_values().mean().astype(int)


# In[135]:


postdr_2014_80th = np.percentile(AAU_postdoc[search_string_7],[61,80])


# In[136]:


#Average Postdoc Appointees for AAU Univerisiies in 2008 61-80
AAU_postdoc[(AAU_postdoc[search_string_7] >= postdr_2014_80th[0]) &
            (AAU_postdoc[search_string_7] <= postdr_2014_80th[1])][search_string_7].sort_values().mean().astype(int)


# In[137]:


postdr_2014_100th = np.percentile(AAU_postdoc[search_string_7],[81,100])


# In[138]:


#Average Postdoc Appointees for AAU Univerisiies in 2008 61-80
AAU_postdoc[(AAU_postdoc[search_string_7] >= postdr_2014_100th[0]) &
            (AAU_postdoc[search_string_7] <= postdr_2014_100th[1])][search_string_7].sort_values().mean().astype(int)


# In[139]:


aau_postdr_2015 = AAU_postdoc[[col_name,search_string_7]].sort_values(by=search_string_7)
aau_postdr_2015.columns = ['Institution', 'Postdoctoral Appointees']
aau_postdr_2015.to_excel(writer,'Postdoctoral Appointees 2015')
writer.save()


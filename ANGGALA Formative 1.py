#!/usr/bin/env python
# coding: utf-8

# # Programming Set 1
# 
# ## This assignment will familiarize you with Python's basics.
# 

# In[19]:


def savings(gross_pay, tax_rate, expenses):
    remaining = round(gross_pay - (tax_rate*gross_pay)) - expenses   
    return remaining


# In[13]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    
    consumed_material = num_jobs*job_consumption
    waste = total_material - consumed_material 
    wasted_material = str(waste) +  material_units
    return wasted_material


# In[ ]:


def interest(principal, rate, periods):
  
    interest_gained = principal*rate*periods 
    final_value = int(principal + interest_gained)
    return final_value 


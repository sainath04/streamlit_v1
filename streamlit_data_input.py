

import streamlit as st
import json



with st.form("my_form"):

      name = st.text_input('GDS User Name')

      mail_id = st.text_input('GDS  Mail ID')

      GPN = st.text_input('Enter your GPN')

      purpose = st.text_area('Purpose')

      project = st.text_input('Project Name')

      reason =st.text_area('Reason for Access')

      duration = st.date_input('Till when do you need access')

      credits_required = st.number_input('Total Credits required for the Project',min_value = 0,step=1)

      Warehouse_size = st.selectbox('Warehouse size',('XS','S','M','L'))

      designation = st.selectbox('Current Designation',('Staff','Senior','Manager','Senior Manager','PPEDD'))


      
      # button_check = st.form_submit_button("Validate")

      # st.write(" Please confirm your details:", '\n\n', 'Name: ', name, '\n\n', 'Mail: ',mail_id,'\n\n', 'GPN: ',GPN,'\n\n', 'purpose: ',purpose,'\n\n', 'project: ',project,'\n\n', 'reason: ',reason,'\n\n', 'duration: ',duration,'\n\n', 'credits_required: ',credits_required,'\n\n', 'Warehouse_size: ',Warehouse_size, '\n\n' , 'designation: ',designation,'\n')


      submitted = st.form_submit_button("Confirm and Submit")



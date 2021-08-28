import pickle
import streamlit as st


model = open('logrmodel.pickle','rb')
lr = pickle.load(model)


st.title("Attrition Prediction")

age = st.slider('Age in years', 0, 40, value=24)

gender = st.selectbox("Gender ",['Female', 'Male', 'Other'])

marriagestatus = st.selectbox("Marriage Status ",['Single', 'Married', 'Divorced/Seperated'])

exp = st.slider('Experience in years', 0, 20)

rectype = st.selectbox("Recruitment Type ",['Direct', 'Employee Referral', 'Agency'])

promotion = st.radio("Promotion recieved",('Yes', 'No'))

jobmatch = st.radio("Job role matched",('Yes', 'No'))

empgroup = st.radio("Employee Group",('B1', 'B2', 'B3', 'Other Groups'))

#Age
Age=age

#Gender
if(gender=='Female'):
    Female=1
    other=0

elif(gender=="Other"):
    Female=0
    other=1

else:
    Female=0
    other=0

#Marriage Status
if(marriagestatus=='Married'):
    Marr=1
    other_status=0

elif(marriagestatus=='Divorced/Seperated'):
    Marr=0
    other_status=1

else:
    Marr=0
    other_status=0

#Expeience
Exp=exp

#Recruitment
if(rectype=='Direct'):
    Direct=1
    Employee_Referral=0

elif(rectype=='Employee Referral'):
    Direct=0
    Employee_Referral=1

else:
    Direct=0
    Employee_Referral=0


#Promotion
if(promotion=='Yes'):
    New_Promotion=1
    
else:
    New_Promotion=0


#Jobmatch
if(jobmatch=='Yes'):
    New_Job_Role_Match=1

else:
    New_Job_Role_Match=0

#Employee Group
if(empgroup=='B2'):
    B2=1
    B3=0
    other_group=0

elif(empgroup=='B3'):
    B2=0
    B3=1
    other_group=0

elif(empgroup=='Other Groups'):
    B2=0
    B3=0
    other_group=1

else:
    B2=0
    B3=0
    other_group=0

prediction=lr.predict([[
            Exp,
            Age,
            New_Promotion,
            New_Job_Role_Match,
            Direct,
            Employee_Referral,
            Marr,
            other_status,
            B2,
            B3,
            other_group,
            Female,
            other
        ]])   

if(prediction[0]=='Left'):
    prediction[0]='Leave'

st.success("The employee will: {}".format(prediction[0]))
















from django import forms

FIELD1_CHOICES= [
    ('Age_Group', 'Age Group'),
    ('Zip_Code___3_digits', 'Zip Code (3 Digits)')]

FIELD2_CHOICES= [
    ('Gender', 'Gender'),
    ('APR_MDC_Description', 'Diagnosis'),
    ('Race', 'Race'),
    ('Ethnicity', 'Ethnicity'),
    ('Type_of_Admission', 'Type of Admission'),
    ('Hospital_Service_Area', 'Hospital Service Area')]

ZIP_CODES = [(str(i), str(i)) for i in range(100, 150)]+[('OOS', 'OOS')]

AGE_GROUP = [
    ('0 to 17', '0 to 17'),
    ('18 to 29', '18 to 29'),
    ('30 to 49', '30 to 49'),
    ('50 to 69', '50 to 69'),
    ('70 or Older', '70 or Older')]

RACE_GROUP = [
    ('White', 'White'),
    ('Black/African American', 'Black/African American'),
    ('Other Race', 'Other Race'),
    ('Multi-racial', 'Multi-racial')]

GENDER = [
    # ('U', 'Unknown'),
    ('M', 'Male'),
    ('F', 'Female')]

TYPE_OF_ADMISSION = [
    ('Elective', 'Elective'),
    ('Emergency', 'Emergency'),
    ('Newborn', 'Newborn'),
    ('Not Available', 'Not Available'),
    ('Trauma', 'Trauma'),
    ('Urgent', 'Urgent')]

class QueryForm(forms.Form):

    field1_choice = forms.CharField(label='Select your first field', widget=forms.Select(choices=FIELD1_CHOICES))
    field2_choice = forms.CharField(label='Select your second field', widget=forms.Select(choices=FIELD2_CHOICES))

class PredictionForm(forms.Form):
    field1_choice = forms.CharField(label="Zip Code (3 Digits)", widget=forms.Select(choices=ZIP_CODES))
    field2_choice = forms.CharField(label="Age Group", widget=forms.Select(choices=AGE_GROUP))
    field3_choice = forms.CharField(label="Gender", widget=forms.Select(choices=GENDER))
    field4_choice = forms.CharField(label="Race", widget=forms.Select(choices=RACE_GROUP))
    field5_choice = forms.CharField(label="Type of Admission", widget=forms.Select(choices=TYPE_OF_ADMISSION))
    
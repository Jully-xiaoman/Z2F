# Z2F
Z2F: Heterogeneous Graph-Based Android Malware Detection

# Floder:decompile
Step1:using apktoo.jar and apktool.bat to install apktool to decompile Android packages;
Step2:using decompile.py to batch decompile Android packages.

# Floder:filter_samples
using check_empty.py,check_smali.py,delete_empty.py and filter_samples.py to check and delete all waste samples;

# Floder:Android features extraction
After decompilation, we get a folder for each Android application;
Step1:using extract_api.py to extract api feature;
Step12:using extract_interface.py to extract interface feature;
...

# Floder:features_data
We use JSON format to store the extracted raw data，api data not uploaded due to storage capacity；

# file:hadmard_normalize.py
Refer to the paper 's original formula (1) ,formula (2);



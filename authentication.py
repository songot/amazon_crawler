import pandas as pd
import os
data = pd.read_csv('store_credentials.csv', header=0, sep=';', index_col=False)
email = data.Email[0]
pswrd= data.Password[0]
shared_code = data.Shared[0]
os.system("echo 'yes\n"+pswrd +"\n"+pswrd+"\n"+shared_code+"\n"+"' | authenticator add Google:"+email+"; echo '#!/usr/bin/env bash\n(echo "+"'" +pswrd+"'"+" | authenticator generate) & sleep 1; kill $!' >> cook_otp; chmod +x cook_otp")

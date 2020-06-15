import os

os.system("apt install chromium-browser=83.0.4103.61-0ubuntu0.18.04.1 && python -m pip install authenticator pandas virtualenv && virtualenv env && . env/bin/activate && python -m pip install selenium pandas && cd env/bin/ && wget -nc https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip && unzip -u chromedriver_linux64.zip")

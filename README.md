##### Imports:
!This project is made with Python.
Before you start you should install these requirements on your environment:(info:you can do that from your terminal using pip install)
- Django
- numpy
- pandas
- matplotlib
- io
- base64

### Purpose of the project:
This project aims to create a web site and use the datas from an IoT device. In this website using the datas from device we create graphics to show the variance and changes in data.

### Explainig the code and structure:
#### views.py file
This file includes the graphics(which you can add more for your own preference) and the code snippet that shows on the website. 
#### forms.py
This file includes the part where we take the input from the user. Creates the form in the home page.
#### html files(home,index,visualize)
These three files creates our front end. home.html is used to create the home page; index.html is used to create the selection part where the user chooses from one of the examples. 
visualize.htlm is used for visualizing the graphics.
#### apps.py and models.py
These two files are at default(only adding "myapp" on apps.py)
#### test.py, admin.py and urls.py
These files are empty. But you can create yourself an admin page with admin.py and run test on your project using test.py. urls.py shows our home and visualize page.





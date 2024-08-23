from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataOptionsForm
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

# Data from `aa.py`
data = [
    {'device': 100, 'pk': 'N/A', 'pub_date': 'N/A', 'field_1': '31', 'field_2': '95', 'field_3': '38', 'field_4': '70', 'field_5': '59', 'field_6': '93', 'field_7': '54', 'field_8': '23'},
    {'device': 100, 'pk': 'N/A', 'pub_date': 'N/A', 'field_1': '73', 'field_2': '81', 'field_3': '100', 'field_4': '67', 'field_5': '98', 'field_6': '72', 'field_7': '41', 'field_8': '30'},
    {'device': 100, 'pk': 'N/A', 'pub_date': 'N/A', 'field_1': '85', 'field_2': '98', 'field_3': '78', 'field_4': '62', 'field_5': '84', 'field_6': '1', 'field_7': '39', 'field_8': '97'},
    {'device': 100, 'pk': 'N/A', 'pub_date': 'N/A', 'field_1': '91', 'field_2': '73', 'field_3': '82', 'field_4': '11', 'field_5': '85', 'field_6': '12', 'field_7': '96', 'field_8': '8'},
    {'device': 100, 'pk': 'N/A', 'pub_date': 'N/A', 'field_1': '53', 'field_2': '60', 'field_3': '82', 'field_4': '71', 'field_5': '37', 'field_6': '64', 'field_7': '6', 'field_8': '92'},
    {'device': 100, 'pk': 'N/A', 'pub_date': 'N/A', 'field_1': '66', 'field_2': '27', 'field_3': '27', 'field_4': '85', 'field_5': '81', 'field_6': '24', 'field_7': '56', 'field_8': '28'},
    {'device': 100, 'pk': 'N/A', 'pub_date': 'N/A', 'field_1': '27', 'field_2': '62', 'field_3': '15', 'field_4': '87', 'field_5': '37', 'field_6': '26', 'field_7': '17', 'field_8': '16'},
    {'device': 100, 'pk': 'N/A', 'pub_date': 'N/A', 'field_1': '14', 'field_2': '77', 'field_3': '80', 'field_4': '70', 'field_5': '17', 'field_6': '54', 'field_7': '4', 'field_8': '31'},
    {'device': 100, 'pk': 'N/A', 'pub_date': 'N/A', 'field_1': '39', 'field_2': '47', 'field_3': '95', 'field_4': '64', 'field_5': '38', 'field_6': '95', 'field_7': '69', 'field_8': '83'},
    {'device': 100, 'pk': 'N/A', 'pub_date': 'N/A', 'field_1': '19', 'field_2': '23', 'field_3': '79', 'field_4': '87', 'field_5': '71', 'field_6': '71', 'field_7': '30', 'field_8': '79'}
]

def home(request):
    return render(request, 'home.html')

def generate_plot(x, y, plot_type, example):
    fig, ax = plt.subplots()

    if isinstance(y[0], (list, np.ndarray)):
        y = np.array(y)

    if example == 'Compare temperature data from three different days':
        if len(y) == 3 and len(set(len(day_data) for day_data in y)) == 1:
            for day_data in y:
                ax.plot(x[:len(day_data)], day_data)
            ax.set_xlabel('Day')
            ax.set_ylabel('Temperature')
            ax.legend(['Day 1', 'Day 2', 'Day 3'])
        else:
            raise ValueError("Data for comparison must contain exactly three lists of the same length")
    elif example == 'Plot temperature and wind speed on two different y-axes':
        if len(y) == 2 and len(y[0]) == len(x) and len(y[1]) == len(x):
            ax.plot(x, y[0], 'r-', label='Temperature')
            ax.set_xlabel('Day')
            ax.set_ylabel('Temperature', color='r')
            ax2 = ax.twinx()
            ax2.plot(x, y[1], 'b-', label='Wind Speed')
            ax2.set_ylabel('Wind Speed', color='b')
            ax.legend(loc='upper left')
            ax2.legend(loc='upper right')
        else:
            raise ValueError("Data sizes must match for temperature and wind speed")
    elif example == 'Visualize correlation between temperature and humidity':
        if len(x) == len(y[0]):
            ax.scatter(x, y[0], label='Temperature vs Humidity')
            ax.set_xlabel('Temperature')
            ax.set_ylabel('Humidity')
        else:
            raise ValueError("Data sizes do not match for correlation")
    elif example == 'Use a histogram to understand variation in data':
        if len(y) == 1:
            ax.hist(y[0], bins='auto')
        else:
            raise ValueError("Histogram requires one dataset")
    else:
        raise ValueError("Invalid example")

    plt.title(f'{plot_type} using {example}')
    plt.legend()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close(fig)
    return img_str

def visualize_data(request):
    if request.method == 'POST':
        form = DataOptionsForm(request.POST)
        if form.is_valid():
            example = form.cleaned_data['example']
            
            # Prepare sample data for plotting
            x = np.arange(1, len(data) + 1)  # Days or index
            temperature = [int(d['field_1']) for d in data]
            wind_speed = [int(d['field_3']) for d in data]
            humidity = [int(d['field_2']) for d in data]
            
            plot_img = None
            code_snippet = ""

            # Generate plot based on user selection
            if example == 'Compare temperature data from three different days':
                day1 = temperature[:3]  # Example data for Day 1
                day2 = temperature[3:6] # Example data for Day 2
                day3 = temperature[6:9] # Example data for Day 3
                x_days = np.arange(1, 4)  # Assuming 3 data points per day
                plot_img = generate_plot(x_days, [day1, day2, day3], 'Temperature Comparison', example)
                code_snippet = """
import matplotlib.pyplot as plt
import numpy as np

def generate_plot(x, y, plot_type, example):
    fig, ax = plt.subplots()
    if example == 'Compare temperature data from three different days':
        if len(y) == 3 and len(set(len(day_data) for day_data in y)) == 1:
            for day_data in y:
                ax.plot(x[:len(day_data)], day_data)
            ax.set_xlabel('Day')
            ax.set_ylabel('Temperature')
            ax.legend(['Day 1', 'Day 2', 'Day 3'])
        else:
            raise ValueError("Data for comparison must contain exactly three lists of the same length")
    plt.title(f'{plot_type} using {example}')
    plt.legend()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close(fig)
    return img_str
"""
            elif example == 'Plot temperature and wind speed on two different y-axes':
                plot_img = generate_plot(x, [temperature, wind_speed], 'Temperature and Wind Speed', example)
                code_snippet = """
import matplotlib.pyplot as plt
import numpy as np

def generate_plot(x, y, plot_type, example):
    fig, ax = plt.subplots()
    if example == 'Plot temperature and wind speed on two different y-axes':
        if len(y) == 2 and len(y[0]) == len(x) and len(y[1]) == len(x):
            ax.plot(x, y[0], 'r-', label='Temperature')
            ax.set_xlabel('Day')
            ax.set_ylabel('Temperature', color='r')
            ax2 = ax.twinx()
            ax2.plot(x, y[1], 'b-', label='Wind Speed')
            ax2.set_ylabel('Wind Speed', color='b')
            ax.legend(loc='upper left')
            ax2.legend(loc='upper right')
        else:
            raise ValueError("Data sizes must match for temperature and wind speed")
    plt.title(f'{plot_type} using {example}')
    plt.legend()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close(fig)
    return img_str
"""
            elif example == 'Visualize correlation between temperature and humidity':
                plot_img = generate_plot(temperature, [humidity], 'Temperature and Humidity Correlation', example)
                code_snippet = """
import matplotlib.pyplot as plt
import numpy as np

def generate_plot(x, y, plot_type, example):
    fig, ax = plt.subplots()
    if example == 'Visualize correlation between temperature and humidity':
        if len(x) == len(y[0]):
            ax.scatter(x, y[0], label='Temperature vs Humidity')
            ax.set_xlabel('Temperature')
            ax.set_ylabel('Humidity')
        else:
            raise ValueError("Data sizes do not match for correlation")
    plt.title(f'{plot_type} using {example}')
    plt.legend()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close(fig)
    return img_str
"""
            elif example == 'Use a histogram to understand variation in data':
                plot_img = generate_plot(x, [temperature], 'Temperature Histogram', example)
                code_snippet = """
import matplotlib.pyplot as plt
import numpy as np
# Here as example temperature data is used.
def generate_plot(x, y, plot_type, example):
    fig, ax = plt.subplots()
    if example == 'Use a histogram to understand variation in data':
        if len(y) == 1:
            ax.hist(y[0], bins='auto')
        else:
            raise ValueError("Histogram requires one dataset")
    plt.title(f'{plot_type} using {example}')
    plt.legend()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close(fig)
    return img_str
"""
            return render(request, 'visualize.html', {'form': form, 'plot_img': plot_img, 'code_snippet': code_snippet})
    else:
        form = DataOptionsForm()

    return render(request, 'visualize.html', {'form': form})


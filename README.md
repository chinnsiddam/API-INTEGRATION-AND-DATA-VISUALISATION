# API-INTEGRATION-AND-DATA-VISUALISATION

*COMPANY*:CODTECH IT SOLUTIONS

*NAME*:SIDDAM NAVYATHA

*INTERN ID*:CT08HIN

*DOMAIN*:PYTHON PROGRAMMING

*DURATION*:10TH JAN 2025 TO 10TH FEB 2025

*MENTOR*:NEELA SANTHOSH

#DESCRIPTION
*I have done my first task of my internship on "API INTEGRATION AND DATA VISUALISATION" using python.I used the openweathermap website to fetch the temperature of a city in INDIA for api keys and api url.
The main steps I performed in this task is Fetching the data from the API,Process the API data for Visualisation and then Visualise the processed data and we obtain a visualised output.
The task I performed  demonstrates how to process and visualize weather data using the matplotlib.pyplot library, a powerful tool for creating visualizations in Python. The code starts by importing the matplotlib.pyplot module, aliased as plt, which provides a flexible interface for creating plots, graphs, and other data visualizations.

The data variable contains weather information for a location (Hyderabad, India). The data includes details like coordinates, temperature, humidity, wind speed, and a description of the weather. This data is extracted from an API.
These are the following main steps:

i)Data Processing:
1. Extract Key Information: The code extracts specific weather details such as city name, country, temperature, humidity, wind speed, and a short description of the weather condition.

2. Unit Conversion: The temperature values are converted from Kelvin to Celsius.

3. Console Output: The extracted data is printed to the console, providing a quick summary of the weather conditions in Hyderabad.

ii)Visualization:

The focus of the code is on visualizing the extracted weather data using a bar chart. This is achieved through the following steps:
1. Prepare Data for Visualization: Labels and corresponding values are defined for the bar chart. Labels include "Temperature (°C)", "Feels Like (°C)", "Humidity (%)", and "Wind Speed (m/s)", while the values are taken from the weather data.

2. Set Up the Plot: The plt.figure() function initializes the figure with a specified size (8x5 inches). This ensures the chart has adequate space for clear visualization.

3. Create the Bar Chart: The plt.bar() function is used to generate the bar chart. Different colors are assigned to each bar using the color parameter.

4. Add Titles and Labels: The title of the chart is  generated to include the city and country name. Labels for the y-axis and a tight layout are added to ensure the plot looks clean and professional.

5. Display the Plot: The plt.show() function renders the chart, allowing the user to visually interpret the weather data.

Advantages of Using matplotlib.pyplot:

1. Simplicity: The library is easy to use and allows for quick visualization of data with minimal code.

2. Customization: Users can customize every aspect of the chart, including colors, labels, sizes, and titles.

3. Integration: matplotlib.pyplot integrates seamlessly with data manipulation libraries like pandas, making it ideal for projects involving large data.
Real-World Applications:

The code we executed can be extended to dynamically fetch real-time weather data from APIs like OpenWeatherMap. It can also be adapted to visualize additional metrics such as cloud coverage, visibility, and pressure. Visualizing data helps users understand patterns and make informed decisions, making this approach highly useful in weather forecasting, climate studies, and other data-driven fields.

In conclusion, this code demonstrates how matplotlib.pyplot can transform raw weather data into an informative and visually appealing representation, making it accessible and useful for various audiences.*

*OUTPUT*:
![Image](https://github.com/user-attachments/assets/f86a5f81-5174-4774-b8b0-5d782c3b5404)

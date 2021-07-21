import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()

#justpy converts this to a python dictionary for highcharts to use
chart_def = """ 
  {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Analysis of Course Reviews'
    },
    subtitle: {
        text: 'These graphs represent course review analysis'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Day'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
  }
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes ="text-p1 text-center")
    hc = jp.HighCharts(a=wp, options=chart_def) #uses HighCharts JS framework, so code fed in is JS
    # print(hc.options)
    # print(type(hc.options)) these lines prove that it is now a python dictionary from a JS object
    hc.options.title.text = "Average Raying by Day" #because its a python dictionary you can use python to dynamically change it
    #series is a key in the chart_def dictionary that contains the data for the graph, so you can replce the template code with what you need

    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])
    return wp



jp.justpy(app)
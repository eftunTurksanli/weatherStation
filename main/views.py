# coding=utf-8
# import simplejson as simplejson
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

from main.models import Station


def index(request):
    stations = Station.objects.all()
    return render(request, "index.html", {'stations': stations})


@csrf_exempt
def add_station(request):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        loc = json.loads(request.POST['loc'])
        station = Station.objects.filter(name=name)
        if station:
            return JsonResponse({'message': u'Ayni istasyon ismini kullanamazsınız', 'type': 'warning'})
        else:
            Station.objects.create(name=name, address=address, location_lat=loc['lat'], location_lng=loc['lng'])
            return JsonResponse({"name": name, "address": address, "lat": loc["lat"], "lng": loc["lng"]})
    return render(request, "index.html")


def show_station(request):
    if request.method == "GET":
        stations = Station.objects.all()
        return JsonResponse(serializers.serialize('json', stations), safe=False)


def detail(request):
    if request.method == "GET":
        details = {
        "units":
        {
            "time": "YYYY-MM-DD hh:mm",
            "temperature": "C",
            "windspeed": "ms-1",
            "precipitation_probability": "percent",
            "pressure": "hPa",
            "relativehumidity": "percent",
            "precipitation": "mm",
            "winddirection": "degree",
            "predictability": "percent"
        },
        "data_1h":
        {
            "time": ["2016-04-26 04:00", "2016-04-26 05:00", "2016-04-26 06:00", "2016-04-26 07:00", "2016-04-26 08:00", "2016-04-26 09:00", "2016-04-26 10:00", "2016-04-26 11:00", "2016-04-26 12:00", "2016-04-26 13:00", "2016-04-26 14:00", "2016-04-26 15:00", "2016-04-26 16:00", "2016-04-26 17:00", "2016-04-26 18:00", "2016-04-26 19:00", "2016-04-26 20:00", "2016-04-26 21:00", "2016-04-26 22:00", "2016-04-26 23:00", "2016-04-27 00:00", "2016-04-27 01:00", "2016-04-27 02:00", "2016-04-27 03:00", "2016-04-27 04:00", "2016-04-27 05:00", "2016-04-27 06:00", "2016-04-27 07:00", "2016-04-27 08:00", "2016-04-27 09:00", "2016-04-27 10:00", "2016-04-27 11:00", "2016-04-27 12:00", "2016-04-27 13:00", "2016-04-27 14:00", "2016-04-27 15:00", "2016-04-27 16:00", "2016-04-27 17:00", "2016-04-27 18:00", "2016-04-27 19:00", "2016-04-27 20:00", "2016-04-27 21:00", "2016-04-27 22:00", "2016-04-27 23:00", "2016-04-28 00:00", "2016-04-28 01:00", "2016-04-28 02:00", "2016-04-28 03:00", "2016-04-28 04:00", "2016-04-28 05:00", "2016-04-28 06:00", "2016-04-28 07:00", "2016-04-28 08:00", "2016-04-28 09:00", "2016-04-28 10:00", "2016-04-28 11:00", "2016-04-28 12:00", "2016-04-28 13:00", "2016-04-28 14:00", "2016-04-28 15:00", "2016-04-28 16:00", "2016-04-28 17:00", "2016-04-28 18:00", "2016-04-28 19:00", "2016-04-28 20:00", "2016-04-28 21:00", "2016-04-28 22:00", "2016-04-28 23:00", "2016-04-29 00:00", "2016-04-29 01:00", "2016-04-29 02:00", "2016-04-29 03:00", "2016-04-29 04:00", "2016-04-29 05:00", "2016-04-29 06:00", "2016-04-29 07:00", "2016-04-29 08:00", "2016-04-29 09:00", "2016-04-29 10:00", "2016-04-29 11:00", "2016-04-29 12:00", "2016-04-29 13:00", "2016-04-29 14:00", "2016-04-29 15:00", "2016-04-29 16:00", "2016-04-29 17:00", "2016-04-29 18:00", "2016-04-29 19:00", "2016-04-29 20:00", "2016-04-29 21:00", "2016-04-29 22:00", "2016-04-29 23:00", "2016-04-30 00:00", "2016-04-30 01:00", "2016-04-30 02:00", "2016-04-30 03:00", "2016-04-30 04:00", "2016-04-30 05:00", "2016-04-30 06:00", "2016-04-30 07:00", "2016-04-30 08:00", "2016-04-30 09:00", "2016-04-30 10:00", "2016-04-30 11:00", "2016-04-30 12:00", "2016-04-30 13:00", "2016-04-30 14:00", "2016-04-30 15:00", "2016-04-30 16:00", "2016-04-30 17:00", "2016-04-30 18:00", "2016-04-30 19:00", "2016-04-30 20:00", "2016-04-30 21:00", "2016-04-30 22:00", "2016-04-30 23:00", "2016-05-01 00:00", "2016-05-01 01:00", "2016-05-01 02:00", "2016-05-01 03:00", "2016-05-01 04:00", "2016-05-01 05:00", "2016-05-01 06:00", "2016-05-01 07:00", "2016-05-01 08:00", "2016-05-01 09:00", "2016-05-01 10:00", "2016-05-01 11:00", "2016-05-01 12:00", "2016-05-01 13:00", "2016-05-01 14:00", "2016-05-01 15:00", "2016-05-01 16:00", "2016-05-01 17:00", "2016-05-01 18:00", "2016-05-01 19:00", "2016-05-01 20:00", "2016-05-01 21:00", "2016-05-01 22:00", "2016-05-01 23:00", "2016-05-02 00:00", "2016-05-02 01:00", "2016-05-02 02:00", "2016-05-02 03:00", "2016-05-02 04:00", "2016-05-02 05:00", "2016-05-02 06:00", "2016-05-02 07:00", "2016-05-02 08:00", "2016-05-02 09:00", "2016-05-02 10:00", "2016-05-02 11:00", "2016-05-02 12:00", "2016-05-02 13:00", "2016-05-02 14:00", "2016-05-02 15:00", "2016-05-02 16:00", "2016-05-02 17:00", "2016-05-02 18:00", "2016-05-02 19:00", "2016-05-02 20:00", "2016-05-02 21:00", "2016-05-02 22:00", "2016-05-02 23:00", "2016-05-03 00:00", "2016-05-03 01:00", "2016-05-03 02:00", "2016-05-03 03:00"],
            "temperature": [6.50, 5.90, 6.21, 8.55, 11.64, 12.53, 12.96, 13.52, 14.09, 14.41, 15.70, 16.80, 16.88, 16.15, 14.89, 13.03, 10.99, 8.74, 7.35, 6.32, 5.53, 4.98, 4.26, 3.87, 4.27, 3.90, 3.83, 4.16, 5.17, 6.49, 7.98, 9.69, 11.22, 12.53, 13.50, 14.12, 14.31, 14.05, 13.20, 11.71, 9.23, 7.66, 6.55, 5.84, 5.36, 5.03, 4.83, 4.47, 3.83, 3.28, 3.33, 4.76, 7.76, 9.91, 11.38, 12.88, 14.04, 15.10, 15.98, 16.57, 16.73, 16.40, 15.45, 13.54, 10.90, 9.33, 8.42, 7.99, 7.77, 7.57, 7.16, 6.49, 5.63, 5.11, 5.19, 6.31, 9.05, 11.34, 13.23, 14.57, 15.63, 16.62, 17.34, 17.76, 17.81, 17.61, 16.69, 15.36, 12.82, 11.52, 10.79, 10.37, 9.94, 10.14, 10.03, 9.50, 8.76, 7.87, 8.07, 9.31, 11.56, 13.66, 15.58, 17.24, 18.45, 19.51, 20.27, 20.60, 20.69, 20.37, 19.45, 17.78, 15.42, 14.08, 13.21, 12.76, 12.56, 12.27, 11.51, 10.73, 9.86, 9.20, 9.20, 11.03, 13.91, 16.74, 19.09, 20.96, 22.35, 23.61, 24.72, 25.39, 25.44, 23.99, 21.86, 20.10, 18.04, 16.92, 16.45, 16.23, 16.39, 15.54, 15.22, 15.17, 14.99, 15.00, 15.13, 15.07, 14.92, 14.16, 15.27, 15.86, 15.92, 15.88, 16.29, 16.91, 16.37, 16.33, 15.67, 14.25, 12.97, 12.08, 10.71, 8.94, 8.20, 7.07, 6.25, 5.50],
            "felttemperature": [2.68, 2.43, 3.04, 5.74, 7.10, 6.31, 7.05, 8.32, 8.82, 9.76, 12.40, 11.64, 11.43, 9.85, 8.75, 6.63, 5.15, 4.29, 2.22, 1.30, 1.30, 1.03, 0.76, -0.12, -0.59, -1.13, -0.68, -0.31, 0.78, 2.36, 4.06, 5.93, 8.68, 10.71, 11.66, 11.66, 11.17, 10.07, 8.90, 7.41, 5.39, 3.72, 2.79, 2.23, 1.89, 1.77, 1.58, 1.22, 0.27, -0.30, -0.29, 1.51, 3.67, 5.54, 7.24, 9.15, 10.86, 11.84, 12.81, 12.87, 12.42, 11.50, 10.29, 8.67, 6.33, 5.03, 4.10, 3.61, 3.43, 3.43, 3.20, 2.78, 2.01, 1.74, 2.09, 3.42, 6.52, 8.38, 9.83, 11.08, 12.60, 13.98, 13.58, 13.48, 12.59, 12.39, 11.26, 10.25, 8.82, 7.65, 6.35, 5.24, 5.05, 5.12, 5.94, 5.97, 5.47, 4.91, 5.33, 7.09, 8.20, 10.27, 13.39, 15.04, 15.90, 16.91, 17.57, 16.46, 17.09, 16.78, 16.21, 15.16, 12.14, 10.61, 9.53, 9.36, 9.76, 9.55, 8.90, 8.03, 7.08, 6.38, 6.36, 8.44, 11.45, 13.61, 16.34, 18.63, 20.21, 21.48, 21.88, 21.67, 21.35, 18.15, 15.07, 16.49, 16.04, 15.17, 14.54, 13.39, 13.16, 11.74, 12.91, 13.05, 12.45, 11.63, 10.43, 9.98, 9.61, 9.32, 9.87, 8.78, 7.86, 7.90, 7.75, 8.68, 8.10, 8.03, 7.54, 7.16, 6.79, 5.15, 3.72, 2.97, 3.33, 2.92, 2.88, 2.48],
            "windspeed": [3.08, 2.68, 2.47, 2.15, 4.69, 7.65, 7.79, 6.35, 6.73, 6.51, 6.01, 6.41, 6.38, 7.48, 7.23, 7.46, 6.57, 4.48, 5.19, 4.94, 3.78, 3.38, 2.76, 3.43, 4.50, 4.73, 4.01, 4.02, 4.10, 3.81, 3.52, 3.45, 3.19, 2.97, 2.81, 2.98, 3.03, 2.99, 3.01, 3.02, 2.55, 2.68, 2.49, 2.35, 2.22, 1.93, 1.83, 1.70, 2.01, 1.97, 2.07, 1.72, 2.77, 3.27, 3.70, 3.99, 3.83, 3.87, 3.67, 3.69, 3.65, 3.32, 3.39, 3.12, 2.66, 2.23, 2.25, 2.32, 2.27, 2.07, 1.91, 1.63, 1.54, 1.24, 0.94, 0.91, 0.74, 1.22, 2.18, 3.35, 3.47, 3.24, 4.29, 4.52, 4.25, 3.79, 4.04, 3.56, 2.00, 1.69, 2.58, 3.76, 3.90, 4.31, 3.30, 2.62, 2.33, 1.70, 1.48, 0.95, 2.52, 2.66, 1.49, 2.62, 3.71, 4.02, 3.96, 4.19, 3.59, 2.78, 2.13, 1.40, 1.92, 2.15, 2.58, 2.36, 1.69, 1.50, 1.22, 1.24, 1.21, 1.25, 1.40, 1.34, 1.31, 2.38, 2.69, 3.07, 3.26, 3.52, 4.28, 5.01, 4.71, 6.26, 7.78, 3.75, 1.72, 1.30, 1.40, 2.74, 3.08, 4.26, 2.46, 2.10, 2.45, 3.14, 4.66, 5.10, 5.48, 5.33, 6.03, 8.34, 9.93, 10.16, 10.64, 9.88, 9.80, 9.75, 9.16, 7.53, 6.10, 7.12, 7.37, 6.26, 4.87, 3.81, 2.77, 2.29],
            "precipitation_probability": [0, 5, 10, 14, 19, 24, 28, 33, 38, 50, 55, 61, 61, 61, 60, 51, 51, 51, 44, 38, 31, 24, 17, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 12, 12, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 13, 14, 14, 15, 16, 16, 16, 16, 15, 15, 15, 14, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 23, 23, 24, 24, 24, 24, 23, 23, 23, 23, 22, 21, 20, 20, 19, 18]
        },
        "data_day":
        {
            "time": ["2016-04-26", "2016-04-27", "2016-04-28", "2016-04-29", "2016-04-30", "2016-05-01", "2016-05-02"],
            "temperature_max": [16.88, 14.31, 16.73, 17.81, 20.69, 25.44, 16.91],
            "temperature_min": [5.90, 3.83, 3.28, 5.11, 7.87, 9.20, 8.94],
            "precipitation_probability": [61, 31, 11, 12, 13, 19, 24],
            "precipitation": [4.09, 0.00, 0.00, 0.00, 0.00, 0.20, 0.00],
            "windspeed_max": [7.79, 4.73, 3.99, 4.52, 4.31, 7.78, 10.64],
            "windspeed_mean": [5.61, 3.31, 2.80, 2.55, 2.69, 2.75, 6.51],
            "windspeed_min": [2.15, 2.35, 1.70, 0.74, 0.95, 1.21, 2.10],
            "relativehumidity_max": [85, 95, 77, 60, 68, 59, 67],
            "relativehumidity_min": [49, 39, 23, 24, 30, 24, 41],
            "relativehumidity_mean": [68, 68, 49, 39, 47, 43, 51]
        }
    }

        return JsonResponse(details)

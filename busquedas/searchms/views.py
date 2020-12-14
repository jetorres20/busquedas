from django.shortcuts import render
from django.http import JsonResponse
import pymongo
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId


# Create your views here.
@api_view(["GET"])
def busqueda(request):
    client = pymongo.MongoClient(settings.MONGO_CLI)
    db = client.booklick
    contenidos = db['contenidos']
    result = []
    buscado=input("Ingrese el titulo o el autor del documento")
    data = contenidos.find({ "$text": { "$search": buscado } } )
    for dto in data:
        jsonData = {
            'id': str(dto['_id']),
            "nombre": dto['nombre'],
            'autor': dto['autor'],
            'anio': dto['anio'],
            'edicion':dto['edicion'],
            'cuerpo':dto['cuerpo']
         }
        result.append(jsonData)
    client.close()
    return JsonResponse(result, safe=False)
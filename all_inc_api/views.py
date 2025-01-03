from django.shortcuts import render

import requests
from pprint import pprint
from rest_framework.request import HttpRequest, Request
from rest_framework.decorators import api_view
from .helpers import get_response, create_query_params
from .serializers import (
    CountrySerializer,
    DepartCitySerializer,
    ResortSerializer,
    HotelCategoriesSerializer,
    MealsTypesSerializer,
    HotelsSerializer,
    TourOperatorsSerializer,
)


# Create your views here.


API = "https://module.sletat.ru/Main.svc"


# страны
@api_view(["GET"])
def get_all_countries(request: Request):
    """
    параметр ?townFromId = id города вылета из представления get_departCities
    для фильтра стран
    """

    query_config = {"townFromId": request.query_params.get("townFromId", None)}

    query_params = create_query_params(query_config)

    response = requests.get(f"{API}/GetCountries{query_params}")

    return get_response(
        response=response,
        nested_keys=["GetCountriesResult", "Data"],
        serializer=CountrySerializer,
    )


# города вылета
@api_view(["GET"])
def get_depart_cities(request: Request):
    response = requests.get(f"{API}/GetDepartCities")

    return get_response(
        response=response,
        nested_keys=["GetDepartCitiesResult", "Data"],
        serializer=DepartCitySerializer,
    )


# курорты
@api_view(["GET"])
def get_resorts(request: Request):
    """
    параметр ?countryId = id страны из представления get_all_countries
    для фильтра курортов
    """

    query_config = {"countryId": request.query_params.get("countryId", None)}

    query_params = create_query_params(query_config)

    response = requests.get(f"{API}/GetCities{query_params}")

    return get_response(
        response=response,
        nested_keys=["GetCitiesResult", "Data"],
        serializer=ResortSerializer,
    )


# категории отелей
@api_view(["GET"])
def get_hotel_categories(request: Request):
    """
    параметр ?countryId = id страны из представления get_all_countries
    параметр ?towns = ids - идентификаторы (через запятую) курортов из представления get_resorts
    для фильтра категорий отелей
    """

    query_config = {
        "countryId": request.query_params.get("countryId", None),
        "towns": request.query_params.get("towns", None),
    }

    query_params = create_query_params(query_config)

    response = requests.get(f"{API}/GetHotelStars{query_params}")

    return get_response(
        response=response,
        nested_keys=["GetHotelStarsResult", "Data"],
        serializer=HotelCategoriesSerializer,
    )


# типы питания
@api_view(["GET"])
def get_meals_types(request: Request):

    response = requests.get(f"{API}/GetMeals ")

    return get_response(
        response=response,
        nested_keys=["GetMealsResult", "Data"],
        serializer=MealsTypesSerializer,
    )


# отели
@api_view(["GET"])
def get_hotels(request: Request):
    """
    параметр ?countryId = id страны из представления get_all_countries
    параметр ?towns = ids - идентификаторы (через запятую) курортов из представления get_resorts
    параметр ?stars = ids - идентификаторы (через запятую) категории отелей get_hotel_categories
    параметр ?filter - str по названию отеля
    параметр ?all - int, количество отелей в выдаче. Возможные значения: “-1” – в выдачу попадают все отели; любое положительное целое число – точное количество отелей.
    для фильтра отелей
    """

    query_config = {
        "countryId": request.query_params.get("countryId", None),
        "towns": request.query_params.get("towns", None),
        "stars": request.query_params.get("stars", None),
    }
    search_by_name = request.query_params.get("filter", "")

    query_params = create_query_params(query_config)

    response = requests.get(
        f"{API}/GetHotels{query_params}&filter={search_by_name}&all=-1"
    )

    return get_response(
        response=response,
        nested_keys=["GetHotelsResult", "Data"],
        serializer=HotelsSerializer,
    )


# туроператоры
@api_view(["GET"])
def get_tour_operators(request: Request):
    """
    параметр ?townFromId = id города вылета из представления get_departCities
    параметр ?countryId = id страны из представления get_all_countries
    для фильтра туроператоров
    """

    query_config = {
        "townFromId": request.query_params.get("townFromId", None),
        "countryId": request.query_params.get("countryId", None),
    }

    query_params = create_query_params(query_config)

    response = requests.get(f"{API}/GetTourOperators{query_params}")

    return get_response(
        response=response,
        nested_keys=["GetTourOperatorsResult", "Data"],
        serializer=TourOperatorsSerializer,
    )


# даты вылета для выбранного города.
@api_view(["GET"])
def get_tour_dates(request: Request):
    """
    параметр ?dptCityId = id города вылета из представления get_departCities
    параметр ?countryId = id страны из представления get_all_countries
    параметр ?resorts = ids идентификаторы (через запятую) страны из представления get_resorts
    параметр ?sources = ids идентификаторы (через запятую) туроператоров из представления get_tour_operators
    доступные даты тура
    """

    query_config = {
        "dptCityId": request.query_params.get("dptCityId", None),
        "countryId": request.query_params.get("countryId", None),
        "resorts": request.query_params.get("resorts", None),
    }

    query_params = create_query_params(query_config)
    response = requests.get(f"{API}/GetTourDates{query_params}")

    return get_response(
        response=response,
        nested_keys=["GetTourDatesResult", "Data", "dates"],
    )

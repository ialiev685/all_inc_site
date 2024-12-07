import humps
from rest_framework.response import Response

import requests
from rest_framework import serializers, exceptions

from typing import Type


def checked_nested_keys(object: dict, keys: list[str]):

    key = keys[0]
    if key in object:
        if isinstance(object[key], dict):
            return checked_nested_keys(object[key], keys[1:])
        elif len(keys) == 1:
            return True
        else:
            return False
    else:
        return False


def depascalize_list_object(list_object: list[dict]):
    if isinstance(list_object, list) and len(list_object) > 0:
        formatted_list = map(lambda object: humps.depascalize(object), list_object)
        return list(formatted_list)
    return []


def get_response(
    response: requests.Response,
    nested_keys: list[str],
    serializer: Type[serializers.Serializer],
):
    try:
        if response.status_code == 200:
            result_data = response.json()

            if checked_nested_keys(object=result_data, keys=nested_keys):

                raw_data = result_data

                for key in nested_keys:
                    raw_data = raw_data[key]

                formatted_data = depascalize_list_object(raw_data)
                # print("formatted_data", formatted_data)
                serialized_data = serializer(data=formatted_data, many=True)
                if serialized_data.is_valid():

                    return Response(
                        data=serialized_data.data, status=response.status_code
                    )

                # print("serialized_data.errors", serialized_data.errors)
                return Response(
                    data=serialized_data.errors, status=response.status_code
                )
        # print("response", response)
        return Response(data=[], status=response.status_code)
    except exceptions.ValidationError:

        return Response(data=response, status=response.status_code)
    except Exception:

        return Response(data=response, status=response.status_code)


def create_query_params(query_params: dict[str, str]) -> str:
    params: list[str] = []
    for key, value in query_params.items():
        if value:
            params.append(f"{key}={value}")

    convert_to_string = "&".join(params) if len(params) > 0 else None

    return f"?{convert_to_string}" if convert_to_string else ""

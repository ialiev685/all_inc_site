from rest_framework import serializers


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=50, required=False, allow_blank=True)
    alias = serializers.CharField(max_length=50, required=False, allow_blank=True)
    flags = serializers.IntegerField(required=False)
    has_tickets = serializers.BooleanField(required=False, default=False)
    hotel_is_not_in_stop = serializers.BooleanField(required=False, default=False)
    is_visa = serializers.BooleanField(required=False, default=False)
    is_pro_visa = serializers.BooleanField(required=False, default=False)
    original_name = serializers.CharField(
        max_length=100, required=False, allow_blank=True
    )
    rank = serializers.IntegerField(required=False)
    tickets_included = serializers.BooleanField(required=False, default=False)


class DepartCitySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=50, required=False, allow_blank=True)
    default = serializers.BooleanField(required=False, default=False)
    descriptionUrl = serializers.CharField(
        max_length=50, required=False, allow_blank=True
    )
    isPopular = serializers.BooleanField(required=False, default=False)
    parentId = serializers.IntegerField(required=False)


class ResortSerializer(DepartCitySerializer):
    pass


class HotelCategoriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=50, required=False, allow_blank=True)


class MealsTypesSerializer(HotelCategoriesSerializer):
    pass


class HotelsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    beachLineId = serializers.IntegerField(required=False)
    commonRate = serializers.FloatField(required=False)
    isInBonusProgram = serializers.BooleanField(required=False, default=False)
    originalName = serializers.CharField(
        max_length=100, required=False, allow_blank=True
    )
    popularityLevel = serializers.IntegerField(required=False)
    photosCount = serializers.IntegerField(required=False)
    searchCount = serializers.IntegerField(required=False)
    rate = serializers.FloatField(required=False)
    starId = serializers.IntegerField(required=False)
    starName = serializers.CharField(max_length=50, required=False, allow_blank=True)
    townId = serializers.IntegerField(required=False)


class TourOperatorsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    enabled = serializers.BooleanField(required=False, default=False)

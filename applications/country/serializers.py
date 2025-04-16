from rest_framework import serializers
from .models import Country


# modelSerializer
# class CountrySerializer(serializers.Serializer):
#     short_name = serializers.CharField(max_length=20)
#     full_name = serializers.CharField(max_length=100)
#     capital = serializers.CharField(max_length=100)
#     president = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     population = serializers.IntegerField()
#     currency = serializers.CharField(max_length=10)
#     no_of_states = serializers.IntegerField()


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        # fields = "__all__"
        exclude = ["id"]
        #read_only, write_only

    # def create(self, validated_data):
    #     pass
    # update, to_representation, to_internal_value

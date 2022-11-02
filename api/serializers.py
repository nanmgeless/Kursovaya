from rest_framework import serializers


class StatisticsSerializer(serializers.Serializer):
    symbol_count = serializers.DictField()
    str_len = serializers.IntegerField()

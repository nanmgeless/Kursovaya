import collections

from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Statistics
from api.serializers import StatisticsSerializer


class StatisticsView(APIView):
    def get(self, request, s):
        stat = Statistics(s=s, symbol_count=collections.Counter(s), str_len=len(s))
        return Response(StatisticsSerializer(instance=stat).data)

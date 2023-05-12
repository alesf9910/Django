from rest_framework.serializers import ModelSerializer
from ..models.prettykeyword import PrettyKeyWord

class PrettyKeyWordSerializer(ModelSerializer):

    class Meta:
        depth = 0
        model = PrettyKeyWord
        exclude = ['task']
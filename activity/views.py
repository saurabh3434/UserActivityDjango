# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from activity.models import User
from activity.serializers import UserSerializer


class ActivityController(APIView):
    """
    Controller to fetch user activity details
    """
    def get(self, request):
        try:
            users = User.objects.all()
            user_ser = UserSerializer(users, many=True)
            return Response({"ok": True,
                             "members": user_ser.data
                             }, 200)
        except Exception as e:
            return Response(str(e), 400)

import io

from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer, CharField, IntegerField
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import Project, Todo, User


# client -> [url] -> [view] -> [serializer] -> [model]

class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

class ProjectModelViewSet(ModelViewSet):
    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()


class TodoModelViewSet(ModelViewSet):
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()




 #сюреализатор
class ProjectSerializer(Serializer):

    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
    #     instance.save()
    #     return instance

    def create(self, validated_data):
        author = Project(**validated_data)
        author.save()
        return author




def get_view2(request):
    #book = Book.objects.get(pk=1)
    #serializer = BookSerializer(book)
    render = JSONRenderer()
    json_data = render.render(serializer.data)
    return HttpResponse(json_data)


    # author = Author.objects.get(pk=1)
    # return render_author(author)


@csrf_exempt
def post_view2(request):
    data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':
        serializer = ProjectSerializer(data=data)
    elif request.method == 'PUT':
        author = Project.objects.get(pk=3)
        serializer = ProjectSerializer(author, data=data)
    elif request.method == 'PATCH':
        author = Project.objects.get(pk=3)
        serializer = ProjectSerializer(author, data=data, partial=True)

    if serializer.is_valid():
        print(serializer.validated_data)

        author = serializer.save()
        return render_author(author)
    else:
        return HttpResponseServerError(serializer.errors['non_field_errors'])


def render_author(author):
    serializer = ProjectSerializer(author)
    render = JSONRenderer()
    json_data = render.render(serializer.data)
    return HttpResponse(json_data)
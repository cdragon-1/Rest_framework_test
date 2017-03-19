from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import serializers
from rest_framework.generics import GenericAPIView

from blog.models import Post


def blog_page(request):
    post_list = Post.objects.all()

    return HttpResponse('Hello World!' + post_list[2].title)


class PostSerializer(serializers.ModelSerializer):
    #Serializer는 REST로 데이터를 주고 받을 때, 모델을 어떻게 주고 받을 것인가를 정의하기 위한 클래스이다. 여기서는 데이터 모델 그 자체를
    #주고 받을 것이니, 기본적으로 모델 전체를 자동으로 변환해주는 ModelSerializer의 힘을 빌릴 것이다.
    class Meta:
        model = Post
        # ModelSerializer는 Meta 클래스를 요구한다. 여기서는 model데이터만 넘겨줘도 충분함.
        fields = ('id', 'reg_date', 'title', 'content', )

class blog_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    # queryset은 어떠한 모델을 보여줄 것인가?를 정의한다.
    serializer_class = PostSerializer
    # ListModelMixin은 GeneicAPIView에 queryset과 serializer_class를 기반으로 하여 데이터 List를 만들어주는 기능을 한다.

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)







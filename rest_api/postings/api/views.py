from django.db.models import Q

from rest_framework import generics, mixins

from postings.models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly



# class BlogPostAPIView(generics.ListCreateAPIView):
class BlogPostAPIView(mixins.CreateModelMixin ,generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = BlogPostSerializer

	def get_queryset(self):
		query = self.request.GET.get('q')
		qs = BlogPost.objects.all()
		if query:
			qs = qs.filter(Q(title__icontains = query)|Q(content__icontains = query)).distinct()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = BlogPostSerializer
	permission_classes = [IsOwnerOrReadOnly]

	def get_queryset(self):
		return BlogPost.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {'request': self.request}

	# def get_object(self):
	# 	pk = self.kwargs.get('pk')
	# 	return self.get_queryset().get(pk = pk)
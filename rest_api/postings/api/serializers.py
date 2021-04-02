from rest_framework import serializers

from postings.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField(read_only = True)
	class Meta:
		model = BlogPost
		fields = ('url', 'user', 'title', 'content', 'timestamp',)
		read_only_fields = ('user',)

	def get_url(self, obj):
		request = self.context.get('request')
		return obj.get_api_url(request)

	def validate_title(self, value):
		qs = BlogPost.objects.filter(title=value)
		if self.instance:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise serializers.ValidationError('This title has already been used')

		return value

>>> ```from rest_framework.renderers import JSONRenderer```
       
>>> from blog.models import Category

>>> from blog.models import Article

>>> from blog.serializers import ArticleSerializer

>>> cors = Article.objects.latest('title')

>>> cors

<Article: elasticserch>

>>> cors.title
'elasticserch'

>>> cors.craeted

datetime.datetime(2020, 8, 20, 17, 27, 32, 82000, tzinfo=<UTC>)

>>> cors.updated

datetime.datetime(2020, 9, 6, 3, 22, 47, 288000, tzinfo=<UTC>)

>>> cors.thumbnail
<ImageFieldFile: media/1F2E4Ek23N5tNXKLuIQaWQA.png>

>>> serializ =  ArticleSerializer(cors)

>>> serializ

ArticleSerializer(<Article: elasticserch>):

    title = CharField(max_length=250)
    slug = SlugField(allow_unicode=False, max_length=100, validators=[<UniqueValidator(queryset=Article.objects.all())>])
    describtion = CharField(style={'base_template': 'textarea.html'})
    publish = DateTimeField(required=False)
    craeted = DateTimeField(read_only=True)

>>> serializ.data

{'title': 'elasticserch', 'slug': 'elastic', 'describtion': 'hello elastic', 'publish': '2020-08-20T17:26:30Z', 'craeted': '2020-08-20T17:27:32.082000Z'}

>>> JSONRenderer().render(serializ.data)

b'{"title":"elasticserch","slug":"elastic","describtion":"hello elastic","publish":"2020-08-20T17:26:30Z","craeted":"2020-08-20T17:27:32.082000Z"}'
>>> 
>>> 
>>> 
>>> 
>>> JSONRenderer().render(serializ.data)
b'{"title":"elasticserch","slug":"elastic","describtion":"hello elastic","publish":"2020-08-20T17:26:30Z","craeted":"2020-08-20T17:27:32.082000Z"}'
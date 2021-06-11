from blog.models import Post
from django.contrib.auth.models import User
from datetime import datetime
import json

# python3 manage.py runscript post_load



def run():
    # Opening JSON file
    f = open('data-back-up/blog/Post-2021-06-07.json',)

    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    Post.objects.all().delete()    

    # Format 10 col
    # 'id', 'title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status', 'tags'

    for i in data:       
        post = Post.objects.create(
            id = i['id'],
            title = i['title'],
            slug = i['slug'],
            author = User.objects.get(id=i['author']),
            body = i['body'],
            #publish = datetime.strptime(i['publish'],  "%Y-%m-%d %H:%M:%S"),
            publish = i['publish'],
            created = i['created'],
            updated = ['updated'],
            status = i['status'],
            tags = i['tags']
        )
        post.save()

    # Closing file
    f.close()

    print("Finished \n")
    print("Count of inserted rows : ", len(Post.objects.all()))

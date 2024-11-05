# api/management/commands/import_data.py
import requests
from django.core.management.base import BaseCommand
from blog.models import Post, Comment
import ipdb

class Command(BaseCommand):
    help = "Import data from JSONPlaceholder API"

    def handle(self, *args, **kwargs):
        # Importar posts
        posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")
        posts_data = posts_response.json()

        for post_data in posts_data:
            Post.objects.update_or_create(
                id=post_data["id"],
                defaults={
                    "user_id": post_data["userId"],
                    "title": post_data["title"],
                    "body": post_data["body"],
                },
            )

        # Importar comentarios
        comments_response = requests.get("https://jsonplaceholder.typicode.com/comments")
        comments_data = comments_response.json()

        for comment_data in comments_data:
            Comment.objects.update_or_create(
                id=comment_data["id"],
                defaults={
                    "post_id": comment_data["postId"],
                    "name": comment_data["name"],
                    "email": comment_data["email"],
                    "body": comment_data["body"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))

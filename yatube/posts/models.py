from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "группы"

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name="текст публикации")
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата публикации"
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="автор"
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        null=True,
        blank=True,
        verbose_name="группа",
    )
    class Meta:
        verbose_name_plural = "посты"
        ordering = ("-pub_date",)

    def __str__(self):
        return self.text

# Generated by Django 4.1.7 on 2023-07-14 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_author_online_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='LikedArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='articleTheUserLiked', to='web.article')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='userWhoLikedTheArticle', to='web.user')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='articleTheUserCommentedOn', to='web.article')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='commenter', to='web.user')),
            ],
        ),
    ]

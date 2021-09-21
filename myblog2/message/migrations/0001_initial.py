# Generated by Django 2.2 on 2021-09-16 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20210911_1756'),
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50, verbose_name='留言内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='留言创建时间')),
                ('parent_message', models.IntegerField(verbose_name='父留言ID')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile', verbose_name='发布者')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic', verbose_name='文章')),
            ],
        ),
    ]
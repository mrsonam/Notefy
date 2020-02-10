from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_audio',
            field=models.FileField(blank=True, null=True, upload_to='audios'),
        ),
    ]

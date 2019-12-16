from django.db import migrations, models

import djangocms_link.validators


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_link', '0013_fix_hostname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='external_link',
            field=models.CharField(blank=True, help_text='Provide a link to an external source.', max_length=2040, validators=[djangocms_link.validators.IntranetURLValidator(intranet_host_re=None)], verbose_name='External link'),
        ),
    ]

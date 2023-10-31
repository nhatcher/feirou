# Generated by Django 4.2.5 on 2024-03-15 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(max_length=100)),
                ('document_number', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('postal_code', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=100)),
                ('reference_location', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('association_name', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(upload_to='community_logos/')),
                ('presentation', models.TextField()),
                ('bylaws', models.FileField(blank=True, null=True, upload_to='community_bylaws/')),
                ('letter_of_principles', models.FileField(blank=True, null=True, upload_to='community_principles/')),
            ],
        ),
        migrations.CreateModel(
            name='ConsumerGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('postal_code', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=10)),
                ('neighborhood', models.CharField(max_length=100)),
                ('reference_location', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to='consumer_logos/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProducerGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(max_length=100)),
                ('document_number', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('postal_code', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=10)),
                ('neighborhood', models.CharField(max_length=100)),
                ('reference_location', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('association_name', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(upload_to='producer_logos/')),
                ('production_method', models.CharField(choices=[('conventional', 'Conventional'), ('agroecology', 'Agroecological'), ('in_transition', 'In transition to agroecological'), ('organic_cert', 'Organic (certified)'), ('other', 'Other')], max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('agricultural', 'Agricultural'), ('handicraft', 'Handicraft'), ('industrial', 'Industrial'), ('artisanal_food', 'Artisanal Food Production')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProducerInvitations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('sent', 'Sent'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='sent', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('invited_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_producer_invitations', to=settings.AUTH_USER_MODEL)),
                ('inviting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_producer_invitations', to=settings.AUTH_USER_MODEL)),
                ('producer_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.producergroup')),
            ],
        ),
        migrations.CreateModel(
            name='UserConsumerInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('sent', 'Sent'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='sent', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('consumer_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.consumergroup')),
                ('invited_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_consumer_invitations', to=settings.AUTH_USER_MODEL)),
                ('inviting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_consumer_invitations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProducerGroupUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField()),
                ('producer_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.producergroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProducerGroupCommunityInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.community')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.producergroup')),
            ],
        ),
        migrations.AddField(
            model_name='producergroup',
            name='production_types',
            field=models.ManyToManyField(related_name='producers', to='groups.productiontype'),
        ),
        migrations.CreateModel(
            name='GenericSocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('url', models.URLField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('platform_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.platformtype')),
            ],
        ),
        migrations.CreateModel(
            name='ConsumerGroupUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField()),
                ('consumer_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.consumergroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumerGroupCommunityInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.community')),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.consumergroup')),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='consumer_groups',
            field=models.ManyToManyField(to='groups.consumergroup'),
        ),
        migrations.AddField(
            model_name='community',
            name='producer_groups',
            field=models.ManyToManyField(to='groups.producergroup'),
        ),
        migrations.AddField(
            model_name='community',
            name='users_admin',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='userproducerinvitations',
            constraint=models.UniqueConstraint(fields=('producer_group', 'inviting_user', 'invited_user'), name='unique_user_producer_invitation'),
        ),
        migrations.AddConstraint(
            model_name='userconsumerinvitation',
            constraint=models.UniqueConstraint(fields=('consumer_group', 'inviting_user', 'invited_user'), name='unique_user_consumer_invitation'),
        ),
        migrations.AddConstraint(
            model_name='producergroupusers',
            constraint=models.UniqueConstraint(fields=('producer_group', 'user'), name='unique_producer_group_user'),
        ),
        migrations.AlterUniqueTogether(
            name='genericsociallink',
            unique_together={('content_type', 'object_id', 'platform_type')},
        ),
        migrations.AddConstraint(
            model_name='consumergroupusers',
            constraint=models.UniqueConstraint(fields=('consumer_group', 'user'), name='unique_consumer_group_user'),
        ),
    ]

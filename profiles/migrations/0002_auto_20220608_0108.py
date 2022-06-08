# Generated by Django 3.0 on 2022-06-08 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
                INSERT INTO profiles_profile (
                    id,
                    user_id,
                    favorite_city
                )
                SELECT
                    id,
                    user_id,
                    favorite_city
                FROM
                    oc_lettings_site_profile;
            """, reverse_sql="""
                INSERT INTO oc_lettings_site_profile (
                    id,
                    user_id,
                    favorite_city
                )
                SELECT
                    id,
                    user_id,
                    favorite_city
                FROM
                    profiles_profile;
            """)
    ]

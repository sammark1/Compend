# Generated by Django 4.0.4 on 2022-05-07 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('location_type', models.CharField(choices=[('Village', 'Village'), ('Town', 'Town'), ('City', 'City'), ('Region', 'Region'), ('State', 'State'), ('Country', 'Country'), ('Province', 'Province'), ('Sea', 'Sea'), ('Lake', 'Lake'), ('Ocean', 'Ocean'), ('Continent', 'Continent'), ('World', 'World')], max_length=32)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.campaign')),
                ('geo_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geolocation', to='main_app.location')),
                ('political_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.location')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(max_length=32)),
                ('family_name', models.CharField(blank=True, max_length=32)),
                ('alignmnet', models.CharField(choices=[('LG', 'Lawful Good'), ('LN', 'Lawful Neutral'), ('LE', 'Lawful Evil'), ('NG', 'Neutral Good'), ('TN', 'True Neutral'), ('NE', 'Neutral Evil'), ('CG', 'Chaotic Good'), ('CN', 'Chaotic Neutral'), ('CE', 'Chaotic Evil')], max_length=32)),
                ('pronoun', models.CharField(choices=[('they', 'They/Them'), ('she', 'She/Her'), ('he', 'He/Him')], max_length=32)),
                ('npc_class', models.CharField(choices=[('Commoner', 'Commoner'), ('Barbarian', 'Barbarian'), ('Bard', 'Bard'), ('Cleric', 'Cleric'), ('Druid', 'Druid'), ('Fighter', 'Fighter'), ('Monk', 'Monk'), ('Paladin', 'Paladin'), ('Ranger', 'Ranger'), ('Rogue', 'Rogue'), ('Sorcerer', 'Sorcerer'), ('Warlock', 'Warlock'), ('Wizard', 'Wizard'), ('Artificer', 'Artificer'), ('Blood Hunter', 'Blood Hunter')], default='Commoner', max_length=32)),
                ('npc_race', models.CharField(choices=[('Dragonborn', 'Dragonborn'), ('Dwarf', 'Dwarf'), ('Elf', 'Elf'), ('Gnome', 'Gnome'), ('Half-Elf', 'Half-Elf'), ('Halfling', 'Halfling'), ('Half-Orc', 'Half-Orc'), ('Human', 'Human'), ('Teifling', 'Teifling'), ('Aarakocra', 'Aarakocra'), ('Genasi', 'Genasi'), ('Goliath', 'Goliath'), ('Aasimar', 'Aasimar'), ('Bugbear', 'Bugbear'), ('Firbolg', 'Firbolg'), ('Goblin', 'Goblin'), ('Hobgoblin', 'Hobgoblin'), ('Kenku', 'Kenku'), ('Kobold', 'Kobold'), ('Lizardfolk', 'Lizardfolk'), ('Orc', 'Orc'), ('Tabaxi', 'Tabaxi'), ('Triton', 'Triton'), ('Yuan-ti Pureblood', 'Yuan-ti Pureblood'), ('Tortle', 'Tortle'), ('Gith', 'Gith')], max_length=32)),
                ('age', models.IntegerField(default=20)),
                ('physical', models.TextField(blank=True)),
                ('profession', models.CharField(blank=True, max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.campaign')),
                ('home', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main_app.location')),
            ],
            options={
                'ordering': ['family_name'],
            },
        ),
    ]

from django.db import models
from django.contrib.auth.models import User

# REVIEW WHEN IMPLEMENTING GLOBAL LIST, MAKE DELETE=PRESERVE

class Campaign(models.Model):
    name = models.CharField(max_length = 32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# REVIEW CONSIDER MAKING THIS AN INPUT FIELD
# REVIEW CONSIDER MORE OPTIONS
LOCATION_CHOICES = (
    ("Village", "Village"),
    ("Town", "Town"),
    ("City", "City"),
    ("Region", "Region"),
    ("State", "State"),
    ("Country", "Country"),
    ("Province", "Province"),
    ("Sea", "Sea"),
    ("Lake", "Lake"),
    ("Ocean", "Ocean"),
    ("Continent", "Continent"),
    ("World", "World"),
)

class Location(models.Model):
    name = models.CharField(max_length = 32)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    location_type = models.CharField(max_length = 32, choices=LOCATION_CHOICES)
    geo_location = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name = 'geolocation')
    political_location = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

ALIGNMENT_CHOICES = (
    ("LG", "Lawful Good"),
    ("LN", "Lawful Neutral"),
    ("LE", "Lawful Evil"),
    ("NG", "Neutral Good"),
    ("TN", "True Neutral"),
    ("NE", "Neutral Evil"),
    ("CG", "Chaotic Good"),
    ("CN", "Chaotic Neutral"),
    ("CE", "Chaotic Evil"),
)

PRONOUN_CHOICES = (
    ("they", "They/Them"),
    ("she", "She/Her"),
    ("he", "He/Him"),
)

CLASS_CHOICES = (
    ("Commoner", "Commoner"),
    ("Barbarian", "Barbarian"),
    ("Bard", "Bard"),
    ("Cleric", "Cleric"),
    ("Druid", "Druid"),
    ("Fighter", "Fighter"),
    ("Monk", "Monk"),
    ("Paladin", "Paladin"),
    ("Ranger", "Ranger"),
    ("Rogue", "Rogue"),
    ("Sorcerer", "Sorcerer"),
    ("Warlock", "Warlock"),
    ("Wizard", "Wizard"),
    ("Artificer", "Artificer"),
    ("Blood Hunter", "Blood Hunter"),
)

RACE_CHOICES = (
    ("Dragonborn", "Dragonborn"),
    ("Dwarf", "Dwarf"),
    ("Elf", "Elf"),
    ("Gnome", "Gnome"),
    ("Half-Elf", "Half-Elf"),
    ("Halfling", "Halfling"),
    ("Half-Orc", "Half-Orc"),
    ("Human", "Human"),
    ("Teifling", "Teifling"),
    ("Aarakocra", "Aarakocra"),
    ("Genasi", "Genasi"),
    ("Goliath", "Goliath"),
    ("Aasimar", "Aasimar"),
    ("Bugbear", "Bugbear"),
    ("Firbolg", "Firbolg"),
    ("Goblin", "Goblin"),
    ("Hobgoblin", "Hobgoblin"),
    ("Kenku", "Kenku"),
    ("Kobold", "Kobold"),
    ("Lizardfolk", "Lizardfolk"),
    ("Orc", "Orc"),
    ("Tabaxi", "Tabaxi"),
    ("Triton", "Triton"),
    ("Yuan-ti Pureblood", "Yuan-ti Pureblood"),
    ("Tortle", "Tortle"),
    ("Gith", "Gith"),
)

class NPC(models.Model):
    given_name = models.CharField(max_length = 32)
    family_name = models.CharField(max_length = 32, blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    alignmnet = models.CharField(max_length= 32, choices=ALIGNMENT_CHOICES)
    pronoun = models.CharField(max_length= 32, choices = PRONOUN_CHOICES)
    npc_class = models.CharField(max_length= 32, choices = CLASS_CHOICES, default='Commoner')
    npc_race = models.CharField(max_length= 32, choices = RACE_CHOICES)
    age = models.IntegerField(default=20)
    physical = models.TextField(blank=True)
    profession = models.CharField(max_length=64, blank=True)
    home = models.ForeignKey(Location, blank=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.given_name} {self.family_name}"

    class Meta:
        ordering = ['family_name']

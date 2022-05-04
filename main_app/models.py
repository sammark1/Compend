from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    name = models.CharField(max_length = 32)

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
    ("he", "he/him"),
)

CLASS_CHOICES = (
    ("Commoner"),
    ("Barbarian"),
    ("Bard"),
    ("Cleric"),
    ("Druid"),
    ("Fighter"),
    ("Monk"),
    ("Paladin"),
    ("Ranger"),
    ("Rogue"),
    ("Sorcerer"),
    ("Warlock"),
    ("Wizard"),
    ("Artificer"),
    ("Blood Hunter"),
)

RACE_CHOICES = (
    ("Dragonborn"),
    ("Dwarf"),
    ("Elf"),
    ("Gnome"),
    ("Half-Elf"),
    ("Halfling"),
    ("Half-Orc"),
    ("Human"),
    ("Teifling"),
    ("Aarakocra"),
    ("Genasi"),
    ("Goliath"),
    ("Aasimar"),
    ("Bugbear"),
    ("Firbolg"),
    ("Goblin"),
    ("Hobgoblin"),
    ("Kenku"),
    ("Kobold"),
    ("Lizardfolk"),
    ("Orc"),
    ("Tabaxi"),
    ("Triton"),
    ("Yuan-ti Pureblood"),
    ("Tortle"),
    ("Gith"),
)

class NPC(models.Model):
    given_name = models.CharField(max_length = 32)
    family_name = models.CharField(max_length = 32 blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    alignmnet = models.CharField(choices=ALIGNMENT_CHOICES)
    pronoun = models.CharField(choices = PRONOUN_CHOICES)
    npc_class = models.CharField(choices = CLASS_CHOICES, default='Commoner')
    npc_race = models.CharField(choices = RACE_CHOICES)
    age = models.IntegerField(default=20)
    physical = models.CharField(max_length=1024, blank=True)
    profession = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.given_name} {self.family_name}"

    class Meta:
        ordering = ['designation']
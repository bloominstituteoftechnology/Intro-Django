# MTG Card

### Fields

ID = UUID
Card Name = models.CharField(max_length=128)
Card Cost = models.CharField(max_length=16) 1G
<!-- Card Color = RED GREEN BLUE BLACK WHITE -->
Card Color =  (
    ('red", 'Red'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('black', 'Black'),
    ('white', 'White'),
)
Card CMC = models.IntegerField()
<!-- Card Type = models.CharField() restrict to = Sorcery instand and Creature -->
Card Type = (
    ('sorcery', 'Sorcery'),
    ('instant', 'Instant'),
    ('land', 'Land'),
    ('creature, 'Creature'),
)
Card SubType = models.Charfield(max_length=32)
Card Set = models.Charfield(max_length = 128)
Card Rules Text = models.TextField()
<!-- Card Flavor Text = models.TextField() -->


*To be added later*

Card Attack = models.IntegerField
    -Only relevant for 'Creature' Types

Card Defense = models.IntegerField()

Quantity owned = models.IntegerField
Decks it is in =

Decks = modals.ManyToManyField('Deck')
## Deck

### Fields

ID = UUID
Deck Name = model.Charfield(max_length=120)
Cards within deck = 

# Relationships between Data Models

Deck -> Card
1 -> Many //a deck can have many cards

Card -> Decks
1 -> Many  //a card can be in many decks

Deck <-> Card
Many <-> Many


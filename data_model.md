
# Data Models

## MTG Card

### Fields

ID = UUID
Card Name = models.CharField(max_length=128)
Card Cost = models.CharField(max_length=16)
<!-- Card Color = models.CharField() restrict to = RED GREEN BLUE BLACK WHITE -->
Card Color = (
    ('red', 'Red'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('black', 'Black'),
    ('white', 'White'),
)
Card CMC = models.IntegerField()
<!-- Card Type = models.CharField() 
restrict to = Sorcery Instant Land Creature -->
Card Type = (
    ('sorcery', 'Sorcery'),
    ('instant', 'Instant'),
    ('land', 'Land'),
    ('creature', 'Creature'),
)
Card SubType = models.CharField(max_length=32)
Card Set = models.CharField(max_length=128)
Card Rules Text = models.TextField()
<!-- Card Flavor Text = models.TextField() -->

*To be added later*

Card Attack = models.IntegerField()
Card Defense = models.IntegerField()
    - Only relevant for `Creature` Types

Qty owned = models.IntegerField()
<!-- Decks it is in = [ DeckIDs ] -->
Decks = models.ManyToManyField('Deck')

## Deck

### Fields

*To be added later*

ID = UUID
Deck Name = model.CharField(max_length=128)
<!-- Cards within deck = [ CardIDs ] -->
Cards= models.ManyToManyField('Card')

# Relationships between Data Models

Deck -> Card
  1  -> Many

Card -> Decks
 1   -> Many

Deck <-> Card
Many <-> Many
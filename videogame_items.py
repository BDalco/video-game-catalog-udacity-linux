from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///videogamecatalog.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd\
             694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Items for PS4
category1 = Category(name="Playstation 4",
                     user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Horizon Zero Dawn",
                     user_id=1,
                     description="The plot revolves around Aloy, a hunter and "
                     "archer living in a world overrun by robots. Having been "
                     "an outcast her whole life, she sets out to discover the "
                     "dangers that kept her sheltered.",
                     category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="The Witcher 3: Wild Hunt",
                     user_id=1,
                     description="With the Empire attacking the Kingdoms of "
                     "the North and the Wild Hunt, a cavalcade of ghastly "
                     "riders, breathing down your neck, the only way to "
                     "survive is to fight back.",
                     category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Uncharted 4: A Thief's End",
                     user_id=1,
                     description="Following Uncharted 3: Drake's Deception, "
                     "it is the final Uncharted game to feature protagonist "
                     "Nathan Drake (portrayed by Nolan North).",
                     category=category1)

session.add(item3)
session.commit()

# Items for PS3
category2 = Category(name="Playstation 3",
                     user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="The Last of Us",
                     user_id=1,
                     description="Twenty years after a pandemic radically "
                     "transformed known civilization, infected humans run "
                     "amuck and survivors kill one another for sustenance "
                     "and weapons.",
                     category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Grand Theft Auto V",
                     user_id=1,
                     description="Los Santos is a vast, sun-soaked metropolis "
                     "full of self-help gurus, starlets and once-important, "
                     "formerly-known-as celebrities.",
                     category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Batman: Arkham City",
                     user_id=1,
                     description="Batman: Arkham City builds upon the "
                     "intense, atmospheric foundation of Batman: Arkham "
                     "Asylum, sending players soaring into Arkham City.",
                     category=category2)

session.add(item3)
session.commit()

# Items for XBox360
category3 = Category(name="XBox 360",
                     user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Bioshock",
                     user_id=1,
                     description="After your plane crashes into "
                     "icy uncharted waters, you discover a rusted "
                     "bathysphere and descend into Rapture, a city "
                     "hidden beneath the sea.",
                     category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Mass Effect 2",
                     user_id=1,
                     description="The game takes place "
                     "within the Milky Way galaxy during the 22nd "
                     "century, where humanity is threatened by an "
                     "insectoid species known as the Collectors.",
                     category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Halo 3",
                     user_id=1,
                     description="The Master Chief is returning to Earth "
                     "to finish the fight.",
                     category=category3)

session.add(item3)
session.commit()

# Items for Wii
category4 = Category(name="Wii",
                     user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="Super Mario Galaxy",
                     user_id=1,
                     description="Join Mario as he ushers in a new era "
                     "of video games, defying gravity across "
                     "all the planets in the galaxy.",
                     category=category4)

session.add(item1)
session.commit()

item2 = CategoryItem(name="The Legend of Zelda: Twilight Princess",
                     user_id=1,
                     description="When an evil darkness enshrouds "
                     "the land of Hyrule, a young farm boy named Link "
                     "must awaken the hero - and the "
                     "animal - within.",
                     category=category4)

session.add(item2)
session.commit()

item3 = CategoryItem(name="New Super Mario Bros. Wii",
                     user_id=1,
                     description="New Super Mario Bros. Wii follows "
                     "Mario as he fights his way through Bowser's henchmen "
                     "to rescue Princess Peach.",
                     category=category4)

session.add(item3)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name

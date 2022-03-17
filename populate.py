import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feliney.settings')
import django
django.setup()

from cats.models import CatProfile
def populate():
    cat_pages=[
        {
            'breed': 'Ragdoll',
            'price_range': '500-600',
            'description': 'The Ragdoll is a cat breed with a color point coat and blue eyes. It is a moderately large cat with a compact, muscular body. Ragdolls are all-white cats with blue eyes and a variety of spotted markings, from solid patches of white on the back of the ears, muzzle, nose, legs, chest, shoulders, and legs to sporadic striped patches. Ragdolls are intelligent and will talk when you walk by and rub on your legs. Ragdolls are the English wildcat cat.'
        },
        {
            'breed': 'Persian cat',
            'price_range': '400-800',
            'description': 'The Persian Cat is a long-haired breed originating in Iran. The Persian was bred in Iran, where the feline community has achieved the highest international recognition for the Persian breed. Today, the Persian Cat has come to be very popular in Iran. During the 1970s, the population of the Persian was considered to be small and the Persian was used in commercial animal rearing for its fur.'
        },
        {
            'breed': 'Sphynx cat',
            'price_range': '1500-4500',
            'description': 'The Sphynx cat is a breed of cat known for its lack of fur. The breed has been in existence for hundreds of years. The breed is known for its ability to catch mice and other small animals and, therefore, it has the name "Mouse Killer." The Sphynx cat has one black ear and one brown ear. The fur on the black ears is known to give off a certain warmth that attracts mice and other small animals. The blackness in the fur goes to the nose and the pupils of.'
        },
         {
            'breed': 'Maine Coon',
            'price_range': '400-800',
            'description': 'The Maine Coon is a medium-sized breed of domestic cat. At a minimum, they weigh about but can exceed .Maine Coon dimensions vary from person to person depending on age, personality and other attributes of the individual. The average Maine Coon has a compact, muscular body, and a long, sleek coat. Covers may be solid black, solid orange, or solid cream. Some Coons exhibit white markings on their coats (for example, Darby, a cream Coon listed on Maine Coons come in a variety of colors including white, black, silver, blue, tortoiseshell, and cream.'
        },
        {
            'breed': 'Scottish Fold',
            'price_range': '250-300',
            'description': "The Scottish Fold is a medium-sized cat, usually ash in color. Males typically weigh 4–6 kg (8.8–13.2 lb), and females weigh 2.7–4 kg (6.0–8.8 lb). The Fold's entire body structure, especially the head and face, is generally rounded, and the eyes large and round. The nose is short with a gentle curve, and the cat's body is well-rounded with a padded look and medium-to-short legs. The head is domed at the top, and the neck very short. The broadly-spaced eyes give the Scottish Fold"
        },
        {
            'breed': 'Abyssinian',
            'price_range': '1500-2000',
            'description': 'Abyssinian is a domestic breed of cat, popularly known as "black cat" or "tabby". It is derived from the Abyssinian breed (originally from the region around the White Nile), which was developed in Egypt in the 18th century from crosses of British Shorthair and Abyssinian cats. Although the Abyssinian cat has a similar appearance to the now-defunct Munchkin breed (the son of a mother and father from different breeds, resulting in'
        },
        {
            'breed': 'Siamese cat',
            'price_range': '600-1200',
            'description': 'Siamese cat originate in Asia and they were imported to Europe in the 19th Century. The earliest account of a Siamese cat as a toy was in 1855 and cats were seen as a symbol of good luck. Many British people have acquired Siamese cats as pets, although the cats became particularly popular during the Second World War. By the 1960s they had become rarer pets, with their popularity returning to the 20th Century in the 1970s.'
        },
        {
            'breed': 'American Shorthair',
            'price_range': '1000-1500',
            'description': 'American shorthair is a popular breed of cat, with a small but solid body.They have long legs and a long-bodied build. American shorthair cats are born with tails that tend to be shorter than the rest of their bodies, with only a little fur between the two tufts of fur at the very top of the tail. This is why they are more commonly referred to as "neuters", as they usually begin to display tail growth by age 2 months.'
        },
        {
            'breed': 'Exotic Shorthair',
            'price_range': '1200-2200',
            'description': 'Exotic shorthair is a peculiar breed of cat, born in our population as a result of interaction between domestic shorthairs and their ancestors in other parts of the world. The majority of these cats are born around the late spring, or early summer. They come into the world light brown in color with a slightly darker green dorsal stripe on a tan background. Their whiskers are white with black tips, the forehead and underbelly is darker.'
        },
         {
            'breed': 'Devon Rex',
            'price_range': '600-1000',
            'description': "Devon Rex is a breed of cat, originating in Scotland, where there are various colour and pattern varieties. They are small, and slender and dainty. They are very friendly, docile, and loving. Often they are found on the lap of a human as a small kitten. Rexes are hard to breed, as the females will usually stop having kittens after 5 to 7 years of age, and don't ovulate or respond to the pituitary gland stimulation"
        },
         {
            'breed': 'Russian Blue',
            'price_range': '800-1200',
            'description': "Russian blue is a cat breed which originated in Russia and Ukraine in the early 20th century. It is also called Moskvitch (Москвич) after the automobile company. The origin of this breed is obscure. It has been known since the 1920s and probably had a breeding foundation by that time. The original Russian blue has a body type somewhat like a tabby, with an upright head and a short square tail. It is larger and heavier than the United Kingdom tabby."
        },
         {
            'breed': 'Birman',
            'price_range': '600-1000',
            'description': "Birman is a breed of cat originating from the island of Mindanao in the southern Philippines. This breed is known as Birman Boyz in Germany, the Philippines and the Netherlands. The origins of the Birman breed may be dated back to the early to mid 19th century. Early Birman cats were first imported to the US around the 1900s. The breed was officially recognized by the Fédération Internationale Féline (FIFe) in 1983,"
        },
         {
            'breed': 'Himalayan cat',
            'price_range': '200-2500',
            'description': 'Himalayan cat is a breed of cat originally from India. It is rare outside its native country and is the only surviving species of the genus "Leopardus", a subfamily of Felidae. It is also sometimes called the Himalayan wild cat. It is listed as a vulnerable species by the IUCN Red List. The Himalayan cats scientific name is Felis frigida. They are close relatives of the Barbary cat (Felis silvestris silvestris), which was once considered a separate species. The Himalayan cat has a larger head than most other cat breeds.'
        },
         {
            'breed': 'Turkish Angora',
            'price_range': '900-1500',
            'description': 'Turkish Angora is a breed of cat originated in Turkey and also known as "Kanuni Angora" (, ) or "Kanuni Angora", "Ciziran Angora" ("Ciziran" meaning Angora in Turkish), or "Altay Angora". The original Angora cats were bred in and around the town of Konya (also known as "Konya Oğulları" ), in Central Anatolia, in the late 19th and early 20th centuries. It was developed from a Turkish Angora cat, named "Ali Özkon", through the breeding of individuals in the type club with foreign Angoras.'
        }
    ]
    add_cat(cat_pages)

def add_cat(cat_pages):
    for c in cat_pages:
        p = CatProfile.objects.get_or_create(breed=c['breed'])[0]
        p.price_range=c['price_range']
        p.description=c['description']
        p.save()

if __name__ == '__main__':
    populate()
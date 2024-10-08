import streamlit as st
from openai import OpenAI

st.title("DawanAI")

key = st.text_input("Entrez votre API key", type="password")
client = OpenAI(api_key=key)

class traduction:
    def respond(self, message):
        response = client.chat.completions.create(
          model="gpt-3.5-turbo-0125",
          messages=[
            {
              "role": "system",
              "content": [
                {
                  "text": "Tu es un traducteur de langue international. Lorsqu'un texte est envoyé, fournis la traduction dans plusieurs langues différentes sous la forme \"key: langue, value: texte traduit\".",
                  "type": "text"
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Hello everyone !"
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "key: français, value: Bonjours tous le mondes !\nkey: espagnol, value: Hola a todos !"
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "My name is Enzo."
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "key: français, value: Mon nom est Enzo.\nkey: espagnol, value: Mi nombre es Enzo."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Je vis a Toulouse."
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "key: anglais, value: I live in Toulouse.\nkey: espagnol, value: Vivo en Toulouse."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "J'ai 25 ans"
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "key: anglais, value: I am 25 years old.\nkey: espagnol, value: Tengo 25 años."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "I'm french"
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "key: espagnol, value: Soy francés."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "I'm french"
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "key: français, value: Je suis français.\nkey: espagnol, value: Soy francés."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "I like football"
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "key: français, value: J'aime le football.\nkey: espagnol, value: Me gusta el fútbol."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Et aussi le handball"
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "key: anglais, value: And also handball.\nkey: espagnol, value: Y también el balonmano."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": message
                }
              ]
            }
          ],
          temperature=1,
          max_tokens=2048,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          response_format={
            "type": "text"
          }
        )
        return response.choices[0].message.content

class generateur:
    def respond(self, message):
        response = client.chat.completions.create(
          model="gpt-3.5-turbo-0125",
          messages=[
            {
              "role": "system",
              "content": [
                {
                  "text": "Tu es un générateur de contenu, a partir d'une thématique données tu rédigera un contenu texte sur le sujet avec approximativement 500 mots.",
                  "type": "text"
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "League of legends"
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "League of Legends est un jeu vidéo sorti en 2009 de type arène de bataille en ligne, free-to-play, développé et édité par Riot Games. Deux équipes de 5 joueurs s'affrontent en temps réel dans des parties, chaque équipe occupant et défendant sa propre base sur la carte. Les joueurs controlent des personnages qui gagnent en puissance au fil de la partie en amassant des points d'expérience ainsi qu'en achetant des objets, dans le but de battre l'équipe adverse. L'objectif d'une partie est de détruire le « Nexus » ennemi, une large structure située au centre de chaque base."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "World of warcraft"
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "World of Warcraft, également connu sous le sigle WoW, est un jeu de rôle en ligne massivement multijoueur (MMORPG) développé et édité par Blizzard Entertainment. Sorti en 2004, WoW est le quatrième opus de la série Warcraft et est devenu l'un des jeux les plus emblématiques de l'histoire du jeu vidéo.\n\nDans World of Warcraft, les joueurs créent un personnage en choisissant parmi différentes races et classes, chacune ayant ses propres compétences et caractéristiques. Ils évoluent dans un vaste monde ouvert fantastique appelé Azeroth, composé de différents continents, royaumes et donjons à explorer.\n\nLe jeu propose un système de quêtes variées, permettant aux joueurs de progresser dans l'aventure, de gagner de l'expérience, des équipements et de découvrir l'histoire riche et complexe du monde de Warcraft. World of Warcraft offre également la possibilité de participer à des raids et donjons en groupe, de s'affronter en JcJ (Joueur contre Joueur) ou encore de s'investir dans des métiers pour fabriquer des objets.\n\nAu fil des années, World of Warcraft a connu de nombreuses extensions apportant du contenu supplémentaire, de nouvelles zones à explorer, des races jouables inédites, des donjons épiques et des défis toujours plus relevés pour les joueurs les plus aguerris. Le jeu a su fidéliser une large communauté de joueurs à travers le monde et a marqué toute une génération de gamers par son univers immersif, sa dimension sociale et sa profondeur de gameplay.\n\nAvec ses graphismes soignés, son gameplay riche et varié, ses musiques envoûtantes et son lore étendu, World of Warcraft reste aujourd'hui l'une des références incontournables du genre MMORPG. Que l'on soit un aventurier aguerri en quête de nouveaux défis ou un novice désireux de découvrir l'univers épique de Warcraft, WoW offre une expérience de jeu unique et intemporelle, capable de captiver les joueurs de tous horizons et de les plonger dans une aventure sans fin au cœur d'un monde fantastique en perpétuelle évolution."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": message
                }
              ]
            }
          ],
          temperature=1,
          max_tokens=2048,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          response_format={
            "type": "text"
          }
        )
        return response.choices[0].message.content

class resumer:
    def respond(self, message):
        response = client.chat.completions.create(
          model="gpt-3.5-turbo-0125",
          messages=[
            {
              "role": "system",
              "content": [
                {
                  "text": "Tu as pour but de résumé en quelques phrases le texte fournis.",
                  "type": "text"
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Charles Leclerc, né le 16 octobre 1997 à Monaco, est un pilote automobile monégasque engagé en Formule 1 au sein de la Scuderia Ferrari.\nVainqueur du championnat de GP3 Series en 2016 puis du championnat de Formule 2 2017, il fait ses débuts en Formule 1 l'année suivante, lors du Grand Prix d'Australie, au sein de l'écurie Alfa Romeo Sauber F1 Team. Il marque ses premiers points en prenant la sixième place du Grand Prix d'Azerbaïdjan à Bakou. Pour sa première saison, il entre dans les points à dix reprises, terminant le championnat avec trois septièmes places consécutives, avant de rejoindre la Scuderia Ferrari ; l'écurie de Maranello l'a en effet choisi pour disputer la saison 2019 aux côtés de Sebastian Vettel, prenant la place de Kimi Räikkönen qui fait le chemin inverse.\nLeclerc est le troisième pilote monégasque à courir en Formule 1 après Louis Chiron et Olivier Beretta. Il est le premier Monégasque à obtenir une pole position, à mener une course, à réaliser un record du tour et le deuxième après Louis Chiron en 1950 à monter sur un podium, dès sa deuxième course avec Ferrari, les 30 et 31 mars 2019 à Bahreïn. Le 1er septembre 2019, il devient, à 21 ans et 10 mois, le plus jeune pilote Ferrari à s'imposer en remportant sa première victoire à l'arrivée du Grand Prix de Belgique à Spa-Francorchamps, et la semaine suivante, le premier pilote de son écurie depuis Fernando Alonso en 2010 à gagner le Grand Prix d'Italie à Monza. Il obtient dix podiums en 2019, saison où il est le pilote qui obtient le plus grand nombre de pole positions, avec sept départs en tête. En décembre, la Scuderia Ferrari annonce qu'elle prolonge son contrat jusqu'en 2024.\nPour la saison 2020, la Ferrari SF1000 ne permet pas à ses pilotes de gagner ou de mener un seul tour, Charles Leclerc n'obtient que deux podiums et termine à la huitième place du championnat. En 2021, il a Carlos Sainz Jr. comme nouveau coéquipier pour une saison où il obtient deux pole positions, un podium, termine 18 fois dans les points et termine septième du championnat. En 2022, il réalise au Grand Prix d'Australie le premier Grand chelem de sa carrière et termine vice-champion du monde. Il n'obtient pas de victoire la saison suivante entièrement dominée par Red Bull et Max Verstappen, obtenant cinq pole positions et montant sur six podiums pour finir cinquième du championnat.\nEn janvier 2024, Ferrari et Charles Leclerc annoncent que son contrat est prolongé pour plusieurs années. En 2025, il fera équipe avec Lewis Hamilton."
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "Charles Leclerc, né le 16 octobre 1997 à Monaco, est un pilote automobile monégasque engagé en Formule 1 au sein de la Scuderia Ferrari. Il est sous les couleurs de Ferrari depuis 2019 et à annoncent que son contrat est prolongé pour plusieurs années, il a notamment était vice-champion du monde en 2022."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Un jeune et timide hobbit, Frodon Sacquet, hérite d'un anneau magique. Sous ses apparences de simple bijou, il s'agit en réalité d'un instrument de pouvoir absolu qui permettrait à Sauron, le Seigneur des ténèbres, de régner sur la Terre du Milieu et de réduire en esclavage ses peuples. Frodon doit parvenir, avec l'aide de la Communauté de l'Anneau, composée de huit compagnons venus de différents royaumes, jusqu'à la Montagne du Destin pour le détruire."
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "Frodon, un hobbit, hérite d'un anneau magique et doit, à l'aide de la communauté de l'anneau, aller jusqu'à la Montagne du Destin pour le détruire afin de stopper Sauron de régner sur la Terre du Milieu."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Harry Potter, un jeune orphelin, est élevé par son oncle et sa tante qui le détestent. Alors qu'il était haut comme trois pommes, ces derniers lui ont raconté que ses parents étaient morts dans un accident de voiture. Le jour de son onzième anniversaire, Harry reçoit la visite inattendue d'un homme gigantesque se nommant Rubeus Hagrid, et celui-ci lui révèle qu'il est en fait le fils de deux puissants magiciens et qu'il possède lui aussi d'extraordinaires pouvoirs."
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "Harry Potter, un jeune orphelin, découvre à son onzième anniversaire qu'il est en fait le fils de deux puissants magiciens et qu'il possède d'extraordinaires pouvoirs, après avoir été élevé par des parents adoptifs qui le détestent."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": message
                }
              ]
            }
          ],
          temperature=1,
          max_tokens=2048,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          response_format={
            "type": "text"
          }
        )
        return response.choices[0].message.content

class correcteur:
    def respond(self, message):
        response = client.chat.completions.create(
          model="gpt-3.5-turbo-0125",
          messages=[
            {
              "role": "system",
              "content": [
                {
                  "text": "Tu es un correcteur de code de programmation. Tu dois d'abord analyser le code reçu afin de déterminer le langage puis proposer une correction de ce code.",
                  "type": "text"
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "def additionner(a, b): \n     resultat = a + b \n     print(\"Le résultat est : \", resultat) \n\nvaleur1 = 5 \nvaleur2 = \"10\"\nadditionner(valeur1, valeur2) \n\ndef diviser(a, b):   \n    return a / b \n\nprint(diviser(10, 0))"
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "def additionner(a, b): \n     resultat = a + b print(\"Le résultat est : \", resultat) # Correction : ajout de la virgule \n\nvaleur1 = 5 \nvaleur2 = 10 # Correction : changement de la chaîne en entier \nadditionner(valeur1, valeur2) \n\ndef diviser(a, b): \n     if b == 0: \n          return \"Erreur : Division par zéro !\" # Correction : gestion de la division par zéro \n     return a / b \n\nprint(diviser(10, 2)) # Correction : éviter la division par zéro"
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "public class Main { \npublic static void main(String[] args) { int a = 5; String b = \"10\"; // Erreur : tentative d'additionner un entier et une chaîne System.out.println(\"Le résultat est : \" + additionner(a, b)); // Erreur dans l'appel de la méthode System.out.println(diviser(10, 0)); // Erreur : division par zéro } \npublic static int additionner(int a, String b) { return a + b; // Erreur : types incompatibles pour l'addition } \npublic static int diviser(int a, int b) { return a / b; // Erreur : division par zéro non gérée } \n}"
                }
              ]
            },
            {
              "role": "assistant",
              "content": [
                {
                  "type": "text",
                  "text": "```java\npublic class Main {\n    public static void main(String[] args) {\n        int a = 5;\n        int b = 10; // Correction : valeur de type int\n        System.out.println(\"Le résultat est : \" + additionner(a, b)); // Correction : Appel de la méthode avec des entiers\n        try {\n            System.out.println(diviser(10, 0)); // Correction : Division par zéro gérée avec une exception\n        } catch (ArithmeticException e) {\n            System.out.println(\"Erreur : Division par zéro !\");\n        }\n    }\n\n    public static int additionner(int a, int b) {\n        return a + b; // Correction : types compatibles pour l'addition\n    }\n\n    public static int diviser(int a, int b) {\n        if (b == 0) {\n            throw new ArithmeticException(); // Correction : lancer une exception pour gérer la division par zéro\n        }\n        return a / b;\n    }\n}\n```\n\nJ'ai corrigé les erreurs dans le code Java fourni : \n1. Changement du type de la variable `b` en `int` pour pouvoir l'additionner avec `a`.\n2. Appel des fonctions additionner et diviser avec des entiers.\n3. Ajout d'une gestion d'exception pour la division par zéro.\n4. Correction du type de retour des fonctions `additionner` et `diviser` pour correspondre aux types des paramètres et au résultat attendu."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": message
                }
              ]
            }
          ],
          temperature=1,
          max_tokens=2048,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          response_format={
            "type": "text"
          }
        )
        return response.choices[0].message.content

chatbots = {
    "Traducteur de texte": traduction(),
    "Générateur de texte": generateur(),
    "Résumé de texte": resumer(),
    "Correcteur de code": correcteur(),
}

selected_bot_name = st.selectbox("Choisissez un chatbot", list(chatbots.keys()))
selected_bot = chatbots[selected_bot_name]

if selected_bot_name == "Résumé de texte" or selected_bot_name == "Correcteur de code":
    user_message = st.text_area("Entrez votre message")
else:
    user_message = st.text_input("Entrez votre message")


if(selected_bot_name == "Traducteur de texte"):
    buttonSend = st.button("Traduire")
elif(selected_bot_name == "Générateur de texte"):
    buttonSend = st.button("Générer")
elif(selected_bot_name == "Résumé de texte"):
    buttonSend = st.button("Résumer")
elif(selected_bot_name == "Correcteur de code"):
    buttonSend = st.button("Corriger")


if buttonSend:
    if user_message:
        bot_response = selected_bot.respond(user_message)
        st.write(f"Vous: {user_message}")
        st.write(bot_response)
    else:
        st.write("Veuillez entrer un message avant d'envoyer.")

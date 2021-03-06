#!/usr/bin/python2.7

settlements = [
    "Aitos",
    "Alefgard",
    "Anor Londo",
    "Arcadia",
    "Arkovia",
    "Beacon",
    "Blackrock",
    "Blackwalk",
    "Blaviken",
    "Bleakstone",
    "Bloodbriar",
    "Bloodpool",
    "Bloodreach",
    "Bloodstone",
    "Bloodwalk",
    "Cairn",
    "Caprica",
    "Carthus",
    "Cimmeria",
    "Daggerfall",
    "Darkover",
    "Darkreach",
    "Darkvale",
    "Darill's Tomb",
    "Darunia",
    "Dawn",
    "Dawnstar",
    "Deadrock",
    "Death Heim",
    "Death Mountain",
    "Devil's Crossing",
    "Doomrock",
    "Dread",
    "Dreadrock",
    "Eastmarch",
    "Eastmost Penninsula",
    "Ember",
    "Emberguard",
    "Emberhold",
    "Emberwatch",
    "Fabul",
    "Fillmore",
    "Fireshrine",
    "First Light",
    "Founder's Rest",
    "Fourhorn",
    "Frigid River",
    "Gloom",
    "Gloomhaven",
    "Gormrange",
    "Graverock",
    "Gravestone",
    "Haven",
    "Heorot",
    "Home",
    "Hope",
    "Hyrule",
    "Irondune",
    "Izalith",
    "Kaer Morhen",
    "Kasuto",
    "Kattegat",
    "Keizaal",
    "Krondor",
    "Lantern's Reach",
    "Last Light",
    "Lightfall",
    "Lufenia",
    "Lux",
    "Melmond",
    "Mido",
    "Mist",
    "Mysidia",
    "Narshe",
    "New Londo",
    "Nilfgaard",
    "Nox",
    "Old Arkovia",
    "Old Kasuto",
    "Onrac",
    "Proudrock",
    "Pthumeria",
    "Rivia",
    "Rockall",
    "Ruto",
    "Sanctuary",
    "San Junipero",
    "Satan's Lantern",
    "Serenity Valley",
    "Sethanon",
    "Shanbar",
    "Shadow's End",
    "Silent Hill",
    "Solitude",
    "Spectacle Rock",
    "Steppinthrax",
    "Stonemarch",
    "Stonevale",
    "The Ancient Lantern",
    "The Black Lantern",
    "The Gambler's Lantern",
    "The Gold Lantern",
    "The Silver Lantern",
    "The White Lantern",
    "Three Eye Rock",
    "Tristram",
    "Vizima",
    "Westmarch",
    "White Rock",
    "Whiterun",
    "Wightmire",
    "Witchweed",
    "Zork",
]

male = [
    "Aaron",
    "Achilles",
    "Adam",
    "Aeneas",
    "Aerol",
    "Aias",
    "Ajax",
    "Akira",
    "Aldrich",
    "Alduin",
    "Alexander",
    "Alucard",
    "Allister",
    "Alva",
    "Amos",
    "Anchises",
    "Andrzej",
    "Anton",
    "Armitage",
    "Artorias",
    "Arthur",
    "Arutha",
    "Asher",
    "Astyanax",
    "Atreyu",
    "Atticus",
    "Augustus",
    "Aziz",
    "Batou",
    "Benedict",
    "Borris",
    "Brian",
    "Brooks",
    "Caleb",
    "Caliban",
    "Calvin",
    "Canuk",
    "Case",
    "Cathbad",
    "Cecil",
    "Clint",
    "Cole",
    "Conan",
    "Corbin",
    "Croesus",
    "Crono",
    "Cuchulain",
    "Cyril",
    "Cyrus",
    "Damon",
    "Dante",
    "Dashiell",
    "Declan",
    "Demetrius",
    "Demarcus",
    "Del",
    "Delekhan",
    "Delita",
    "Deltron",
    "Derek",
    "Diego",
    "Direni",
    "Donovan",
    "Draco",
    "Drizzt",
    "Duncan",
    "Edward",
    "Eirik",
    "Eli",
    "Elvis",
    "Erasmus",
    "Erdrick",
    "Errol",
    "Eskel",
    "Esteban",
    "Ezekiel",
    "Ezra",
    "Farooq",
    "Felix",
    "Fester",
    "Fidel",
    "Fingal",
    "Finn",
    "Foster",
    "Francis",
    "Frog",
    "Gabriel",
    "Gaunther",
    "Gerald",
    "Geralt",
    "Gerard",
    "Giovanni",
    "Gomez",
    "Gorath",
    "Grant",
    "Griffith",
    "Grimnir",
    "Gustavo",
    "Guy",
    "Gwyn",
    "Gyuri",
    "Haakon",
    "Hadrian",
    "Harman",
    "Hawkeye",
    "Hector",
    "Hideo",
    "Hipolito",
    "Hiram",
    "Hobbes",
    "Hugh",
    "Humbert",
    "Humberto",
    "Ian",
    "Icarus",
    "Idris",
    "Ignacio",
    "Ike",
    "Irving",
    "Israel",
    "Isaac",
    "Jacob",
    "Jacinto",
    "Jeremy",
    "Jesse",
    "Jaoquin",
    "Jon",
    "Jonah",
    "Jorge",
    "Jude",
    "Julius",
    "Kalameet",
    "Kane",
    "Karl",
    "Khalil",
    "Khoa",
    "Khorvash",
    "Killian",
    "Kieran",
    "Kirk",
    "Klaus",
    "Korben",
    "Kris",
    "Kyle",
    "Lambert",
    "Lance",
    "Lazaro",
    "Lebiodus",
    "Leif",
    "Leonard",
    "Locklear",
    "Logan",
    "Loto",
    "Liam",
    "Lincoln",
    "Link",
    "Locke",
    "Lucas",
    "Lucien",
    "Lucius",
    "Luther",
    "Lyman",
    "Lysandus",
    "Magnus",
    "Malcolm",
    "Malik",
    "Malvolio",
    "Manannan",
    "Marcus",
    "Mason",
    "Maelcum",
    "Maximo",
    "Maxwell",
    "Maynard",
    "Merlin",
    "Moadikum",
    "Modesto",
    "Mohammed",
    "Moodock",
    "Morne",
    "Mordack",
    "Morty",
    "Moshe",
    "Micah",
    "Mulder",
    "Murmandamus",
    "Nathan",
    "Naveen",
    "Nero",
    "Nestor",
    "Neville",
    "Nils",
    "Norman",
    "Noah",
    "Oberon",
    "Odin",
    "Olaf",
    "Oliver",
    "Orlando",
    "Ozelianho",
    "Owen",
    "Owyn",
    "Paul",
    "Pawel",
    "Pelagius",
    "Peter",
    "Petrus",
    "Piotr",
    "Preston",
    "Puck",
    "Pug",
    "Quentin",
    "Ramza",
    "Rashad",
    "Ravix",
    "Reuben",
    "Reed",
    "Robb",
    "Robert",
    "Rodin",
    "Reinhardt",
    "Reinaldo",
    "Rico",
    "Rick",
    "Rickert",
    "Royal",
    "Raynaldo",
    "Roland",
    "Rolondo",
    "Rolo",
    "Royce",
    "Rubicante",
    "Ruby Rhod",
    "Ryu",
    "Sean",
    "Sergei",
    "Setzer",
    "Sigi",
    "Sigmund",
    "Silas",
    "Shane",
    "Simon",
    "Santiago",
    "Solomon",
    "Sylvester",
    "Sang",
    "Seth",
    "Stammelford",
    "Stark",
    "Talos",
    "Telamon",
    "Tetsuo",
    "Teucer",
    "Thanh",
    "Theron",
    "Theseus",
    "Thor",
    "Timon",
    "Timothy",
    "Titus",
    "Tobias",
    "Trapper",
    "Trembyle",
    "Trent",
    "Trevor",
    "Trey",
    "Ulf",
    "Ulysses",
    "Umberto",
    "Unferth",
    "Uriel",
    "Valentine",
    "Vaughn",
    "Vesemir",
    "Victor",
    "Vincenzo",
    "Virgil",
    "Vimme",
    "Vivec",
    "Vlad",
    "Voltaire",
    "Ward",
    "Wallace",
    "Wiglaf",
    "William",
    "Wilfred",
    "Xavier",
    "Xerxes",
    "Yang",
    "Zachary",
    "Zane",
    "Zeke",
    "Zhu Di",
    "Zophar",
    "Zurin",
]

female = [
    "Acacia",
    "Adda",
    "Adrasteia",
    "Amaryllis",
    "Amphirite",
    "April",
    "Anna",
    "Arabella",
    "Ashlotte",
    "Alenia",
    "Alexa",
    "Alexandria",
    "Andromache",
    "Antiope",
    "Arethusa",
    "Aria",
    "Arlen",
    "Athena",
    "Audrey",
    "Aurelia",
    "Aurora",
    "Axioche",
    "Azura",
    "Ava",
    "Avalon",
    "Ayla",
    "Barbarella",
    "Barenziah",
    "Beatrice",
    "Belit",
    "Bianca",
    "Blossom",
    "Bodhmall",
    "Brianne",
    "Bridget",
    "Brooke",
    "Caitlyn",
    "Celes",
    "Camelia",
    "Camilla",
    "Carmen",
    "Casca",
    "Cassandra",
    "Cassima",
    "Cayce",
    "Celeste",
    "Cereza",
    "Charli",
    "Charlotte",
    "Cheree",
    "Chevette",
    "Ciri",
    "Cirilla",
    "Cleo",
    "Cleodora",
    "Cleopatra",
    "Dahlia",
    "Dapnhe",
    "Deichtine",
    "Delilah",
    "Delphine",
    "Demeter",
    "Desdemona",
    "Diana",
    "Eir",
    "Eirwen",
    "Electra",
    "Elena",
    "Elisif",
    "Eliza",
    "Emer",
    "Emilia",
    "Erica",
    "Ezra",
    "Esmerelda",
    "Esti",
    "Eve",
    "Fade",
    "Fern",
    "Fiona",
    "Florence",
    "Flynne",
    "Frances",
    "Freya",
    "Gabrielle",
    "Genevieve",
    "Gillian",
    "Gloria",
    "Goneril",
    "Grace",
    "Gwaelin",
    "Gwen",
    "Haifa",
    "Heather",
    "Hecuba",
    "Hecate",
    "Harper",
    "Heidrun",
    "Hilary",
    "Hinata",
    "Hollis",
    "Hope",
    "Ida",
    "Igraine",
    "Iola",
    "Iman",
    "Ingrid",
    "Iphigeneia",
    "Ira",
    "Irina",
    "Iris",
    "Isabella",
    "Isolde",
    "Ivy",
    "Jaclyn",
    "Janet",
    "Jayne",
    "Jasmine",
    "Jeanne",
    "Jennifer",
    "Joi",
    "Jolyne",
    "Julia",
    "Juliet",
    "Kalliope",
    "Kara",
    "Katarina",
    "Kei",
    "Kendall",
    "Kendra",
    "Kestrel",
    "Kiyoko",
    "Kira",
    "Keira",
    "Kumiko",
    "Kyra",
    "Lana",
    "Lavender",
    "Laverne",
    "Lavinia",
    "Leeloo",
    "Leia",
    "Leigh",
    "Leuce",
    "Lexi",
    "Libby",
    "Lily",
    "Lilvani",
    "Linda Lee",
    "Lisa",
    "Lola",
    "Lolita",
    "Lolotte",
    "Lucca",
    "Lucille",
    "Lucy",
    "Luna",
    "Lydia",
    "Mab",
    "Mabel",
    "Marigold",
    "Maeve",
    "Magdalena",
    "Maleficent",
    "Mallory",
    "Malvina",
    "Marle",
    "Mary",
    "Maria",
    "Maya",
    "Megha",
    "Melitele",
    "Mephala",
    "Michiko",
    "Minerva",
    "Miranda",
    "Misty",
    "Mitsuko",
    "Molly",
    "Moana",
    "Mona",
    "Monika",
    "Morgana",
    "Morticia",
    "Nadia",
    "Narcissa",
    "Nenneke",
    "Nia",
    "Naomi",
    "Noriko",
    "Nulfaga",
    "Nyx",
    "Odette",
    "Ophelia",
    "Olive",
    "Olivia",
    "Olwen",
    "Opal",
    "Orchid",
    "Paetra",
    "Paige",
    "Patricia",
    "Pauline",
    "Pearl",
    "Pepper",
    "Phaedra",
    "Phoebe",
    "Polly Jean",
    "Potema",
    "Quelana",
    "Quinn",
    "Quirina",
    "Rachna",
    "Rachel",
    "Rada",
    "Raina",
    "Rasha",
    "Regan",
    "Regina",
    "Renee",
    "Rhea",
    "Rhianon",
    "Rhys",
    "Ria",
    "Rosa",
    "Rosalind",
    "Rosaria",
    "Rosario",
    "Rose",
    "Rosella",
    "Ruby",
    "Sabrina",
    "Sakura",
    "Samantha",
    "Sansa",
    "Sara",
    "Scarlet",
    "Scarlett",
    "Scheherazade",
    "Scully",
    "Scylla",
    "Senua",
    "Serafina",
    "Setsuka",
    "Shyma",
    "Sibyl",
    "Sif",
    "Sigrun",
    "Simone",
    "Six",
    "Sonja",
    "Sophia",
    "Sophitia",
    "Skyy",
    "Stella",
    "Suki",
    "Summer",
    "Sybil",
    "Tamara",
    "Tamiko",
    "Tara",
    "Thalia",
    "Themis",
    "Triss",
    "Ume",
    "Undine",
    "Unice",
    "Valencia",
    "Valeriya",
    "Vee",
    "Vena",
    "Velka",
    "Veronica",
    "Vesta",
    "Viola",
    "Violet",
    "Vylette",
    "Wednesday",
    "Winona",
    "Wiola",
    "Wynter",
    "Xandra",
    "Xochitl",
    "Xianghua",
    "Xiu",
    "Yana",
    "Yennefer",
    "Ylva",
    "Yoko",
    "Yuan-Xiao",
    "Yuki",
    "Yuria",
    "Yvonne",
    "Zahara",
    "Zelda",
    "Zoe",
]

neuter = [
    "Addison",
    "Anri",
    "Ash",
    "Bishop",
    "Blackthorn",
    "Blake",
    "Blue",
    "Caelan",
    "Dana",
    "Drew",
    "Error",
    "Ghost",
    "Hayden",
    "Hunter",
    "Jones",
    "Justice",
    "Lindsey",
    "Parker",
    "Lane",
    "Mac",
    "Morgan",
    "Oakley",
    "Phoenix",
    "Quinn",
    "Raven",
    "Red",
    "Reese",
    "Revan",
    "Robin",
    "Roan",
    "Rook",
    "Sage",
    "Scout",
    "Shadow",
    "Shannon",
    "Starbuck",
    "Storm",
    "Stormy",
    "Toto",
    "Thorne",
    "Winter",
    "Wolf",
]

surname = [
    "Black",
    "Bloodmoon",
    "O'Connell",
    "Poots",
    "Steele",
    "Steelesoul"
    "Waylander",
]

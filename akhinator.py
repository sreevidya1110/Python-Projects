f=["HarryPotter",
    "HermioneGranger",
    "LordVoldemort",
    "Winniethepooh",
    "Elsa",
    "SeverusSnape",
    "Willywonka",
    "AlbusDumbledore",
    "Death",
    "Mowgli",
    "Simba",
    "Anna",
    "Mufasa",
    "SherKhan",
    "PercyJackson",
    "Alice(wonderland)",
    "Devasena",
    "LaraCroft",
    "BellatrixLestange",
    "Catwoman",
    "Wonderwoman",
    "RachelGreen",
    "ProfessorMc.Gonagall",
    "MonicaGeller",
    "CedricDiggory",
    "DracoMalfoy",
    "PhoebeBuffay",
    "AmarendraBAHUBALI",
    "Joker",
    "Belle(Beauty And The Beast)"]
r=["NarendraModi",
    "M.S.Dhoni",
    "ViratKohli",
    "K.L.Rahul",
    "SmritiMandana",
    "MaryKom",
    "PriyaPrakashVarrier",
    "ShahRukhKhan",
    "Kajol",
    "Vijay",
    "SUPERSTARRajinikanth",
    "Aravind SA",
    "Einstein",
    "Newton",
    "RaniLakshmiBai",
    "LakshmiAgarwal(acid attack victim)",
    "Nayanthara(actress)",
    "KanganaRanaut",
    "Jayalalitha",
    "AdolfHitler",
    "A.P.JAbdulKalam",
    "Dr.Radhakrishnan",
    "MahtmaGandhi",
    "R.DSharma",
    "A.R.RAHMAN",
    "Anirudh(Music Director)",
    "ThomasAlvaEdison",
    "LionalMessi",
    "ChrisGayle",
    "RogerFederer"]
opening=input("HI FRIENDS DO U WANT TO PLAY A GAME OF AKHINATOR????(type yes to continue,no to exit)")
if opening=="no":
    print("OK BYE BYE!!")
if opening=="yes":
    print("AKHINATOR WELCOMES YOU TO HIS RESIDENCY")
    print("RULES AND REGULATIONS:")
    print("""The game is very simple, think of a character from the list i am going to give u,choose whether u want me to guess a fictional or real life character
             and go on typing yes or no to the questions i ask u based on the character u thought of
             and see if i end up guessing the character u thought of!!!!!!""")
    choice=input("type r/R for real life characters and f/F for fictional characters")
    if choice=="f" or choice=="F":
        for i in range(0,30):
            print(f[i])
    elif choice=="r"or choice=="R":
        for i in range(0,30):
            print(r[i])
                    
                
             
    



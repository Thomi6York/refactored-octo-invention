# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python: 
    bad_words = ["piss","cunt","dick","shit","arse","bitch","tard","fuck","bollock","twat","shag","wank","slut","jew","fag","tranny"]

    gen_con1 = "" 

    con1_list = ["sp","spr","sl","sk","sch","pl","pr","wr","r","t","h","p","m","n","ph","cr","kr","x","qu","sh","str","br","bl","b","v","vr","fr","fl","f","d","dr","tr","ts","gr","gl","kl","h","z","pf","sw","th","ch","chr","j"]

    gen_vowel = "" 

    vowel_list = ["ua","au","oo","ee","ia","ai","er","ar","ah","eh","ii","a","e","i","o","u","ur","ir","or","ih","uh","oh","y","ui","iu","uo","ou","ae","ea","ew","aw","iw","oi","io"]

    gen_con2 = "" 

    con2_list = ["ck","c","nt","mt","rd","rg","p","l","ll","w","q","rq","b","mn","m","n","lk","tch","ch","d","s","ss","g","ff","f","dd","r","rr","z","zz","wn","ct","ft","lt","ldt","pt","wt","ht","hd","gh","h","k","c","ng","th","ch","rc"]

    syl_structure = ["v","cv","vc","cvc"]

    NPCName1 =""

    NPCName2 =""

    NPCName3 =""

    NPCName4 =""

    def GetSyllable(allow_cvc = True):
        structure = renpy.random.choice(syl_structure)
        while not allow_cvc and structure == "cvc":
            structure = renpy.random.choice(syl_structure) 
        if structure == "v":
            return renpy.random.choice(vowel_list)
        elif structure == "cv": 
            return renpy.random.choice(con1_list)+renpy.random.choice(vowel_list) 
        elif structure == "vc":
            return renpy.random.choice(vowel_list)+renpy.random.choice(con2_list) 
        elif structure == "cvc": 
            return renpy.random.choice(con1_list)+renpy.random.choice(vowel_list)+renpy.random.choice(con2_list) 
        else: 
            return "?" 
    def GetName(): 
        no_syllables = renpy.random.randint(1,4)
        name = "" 
        for i in range (no_syllables): 
            name = name+GetSyllable(allow_cvc = no_syllables < 4)
        while name in vowel_list: 
            name = name+GetSyllable(allow_cvc = no_syllables < 4) 
        for word in bad_words: 
            if word in name: 
                return GetName()
        return name 

    store.NPCName1 = GetName().capitalize()
    store.NPCName2 = GetName().capitalize()
    store.NPCName3 = GetName().capitalize()
    store.NPCName4 = GetName().capitalize()

define mc = Character("MainChar")
define bt = Character("Bartender")
define li1 = DynamicCharacter("NPCName1")
define li2 = DynamicCharacter ("NPCName2")
define li3 = DynamicCharacter ("NPCName3")
define li4 = DynamicCharacter ("NPCName4")




# The game starts here.

label start:
    jump Inn

label Inn:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bgcoastalexterior

    # A DARK STORMY NIGHT IN A COASTAL TOWN.

    "It's getting late.  I need to find somewhere to stay.  This inn looks good."

    scene bginn

    # A DARK INN, LIT ONLY BY CANDLES ON THE TABLES AND LANTURNS ON THE BAR

    show chbartender

    "The bartender looks at you."

    bt "Are you here for the event?"

    menu: 
        "What event?":
            jump inn01
        "Yes":
            jump inn01
        "Just a room, please":
            jump inn02

label inn01:
    
    "The bartender looks at you with suspcion.  It is apparent he does not believe you are associated with this event and he does not want to give you any details."

    bt "You can have a room."

    jump inn02

label inn02:
    "The bartender slams a key on the bar.  He gestures across to a wooden set of stairs in the corner."

    bt "Upstairs.  First on the right."

    "You take the keys and head towards the stairs when raised voices catch your attention.  You turn to see a group of hooded figures \
    sat around a table by the window.  You pause to listen to their conversation."

    hide chbartender
    
    show chli1
    
    li1 "I just don't think it's a good idea.  We just don't know what we are getting involved in."

    hide chli1
    show chli2

    li2 "But perhaps the issue is that if we don't get involved, we wont know what we are missing out on.  What if the risk is bigger if we don't get involved?"

    hide chli2
    show chli1

    li1 "Do the Gods even know who we are at this point?"

    hide chli1
    show chli3

    li3 "Of course they do.  They know all.  Are you seriously that naive?"

    hide chli3
    show chli4

    "The fourth figure takes a wary look around the room.  You lock eyes for a second before they turns back to the others."

    li4 "We are being observed.  We need to leave."

    hide chli4

    "At this point all four figures stood up and walked out the room.  The bartender looked at you and sighed."

    show chbartender

    bt "Well there goes my night's takings.  Do not cause trouble in this town.  I don't know why you're here, but if you know what's good for you, get on with your business and leave first thing."

    hide chbartender

    "Feeling this is all a bit weird, you decide to head to bed."

    jump Chapter1

label Chapter1:

    scene bgbedroom

    # BASIC AND CREEPY

    "You wake up having had the best sleep of your life.  Everything that had set you on edge last night seems a horrible memory \
    which you are sure was just brought on by a lack of sleep."

    "You decide to head out and find some breakfast."

    scene bgstreet

    # SAME AS costalExteriorNight BUT DAYIME VIBES AND CLEAR WEATHER

    "As you walk outside, you see someone running directly towards you.  They notice you too late, trip and land at your feet."

    show chli1

    li1 "Ugh.  Sorry.  I didn't mean to"

    menu:
        "It's okay.":
            jump Chapter1_1_2
        "Don't worry about it.":
            jump Chapter1_1_2
        "It was a bit rude.":
            jump Chapter1_1_1

label Chapter1_1_1:

    li1 "Um.  I didn't mean to."

    jump Chapter1_1_2

label Chapter1_1_2:
    
    li1 "Sorry, I guess I was a little distracted."
    
    "As soon as the stranger starts speaking, you recognise them as being from the inn the previous night.  You decide at this point not to mention anything."
    
    li1 "My friends and I are having a bit of a disagreement about..."

    "There is a long pause as the stranger seems to be trying to work out how to phrase the next sentence."

    li1 "About some acquaintances we are thinking of spending time with.  I'm not sure they're nice people."

    hide chli1

    "At this point three more beings arrive."

    show chli3
    
    li3 "What do you think you were doing running off like that?"

    hide chli3
    show chli2

    li2 "It could have been dangerous.  You don't know who you might have run into."

    hide chli2
    show chli1

    li1 "Yeah, run into is probably the best way to put it.."

    hide chli1
   
    "Your eyes lock with the same individual as last night."

    show chli4

    li4 "It's you again.  What are you doing here?"

    menu:
        "I was just getting some breakfast.":
            jump Chapter2_2_1
        "I have business in town.":
            jump Chapter2_2_2
        "Uh..  Nothing.":
            jump Chapter2_2_3

label Chapter2_2_1:

    li4 "No, I meant what are you doing in this town?"

    menu:
        "I have business here.":
            jump Chapter2_2_2
        "I'm on vacation.":
            jump Chapter2_2_4
        "Nothing?":
            jump Chapter2_2_3

    jump Chapter2_2_4

label Chapter2_2_2:

    li4 "What sort of business?  Who are you?"

    jump Chapter2_2_4

label Chapter2_2_3:

    hide chli4
    show chli3

    li3 "What do you mean nothing?  Why did you even leave your bed if it was to do nothing?"

    hide chli3

    jump Chapter2_2_4

label Chapter2_2_4:
    show chli4

    li4 "Enough.  I am tired of this nonsense.  Anyway.  We all have things to do so we should bid this individual farewell and get on with them."

    "You feel relived you have escaped the questioning.  For now."

    li4 "We are busy today.  We were just about to split up and do different things when this interuption occurred."

    li4 "Actually, maybe to compensate for your interruption, you can help us out."
    
    "You feel a deep concern in your lower stomach."

    hide chli4
    show chli1

    li1 "Actually, that would be really helpful.  I need to go and buy some cupcakes for my grandmother.  It's her birthday!"

    "This doesn't seem so bad."

    hide chli1
    show chli2

    li2 "I want to go and pray.  I guess you can come and help, but it may not be your kind of thing."

    hide chli2
    show chli4

    li4 "That is something that must be done alone.  You should go now."

    menu:
        "Stop [NPCName2]":
            jump Chapter2_3_1
        "Let [NPCName2] go":
            jump Chapter2_3_4

label Chapter2_3_1:
    
    hide chli4
    show chli2

    "You grab [NPCName2]'s arm as they turn to leave."

    menu:
        "I'd like to help you":
            jump Chapter2_3_2
        "I'm just super into prayer so I think it'd be cool if I came along..":
            jump Chapter2_3_2

label Chapter2_3_2:

    "[NPCName2] gives you a strange look."
    li2 "I suppose that would be okay."

    "You live happily ever after."
    "The end."

    # This needs more.

    return
    

label Chapter2_3_4:








    # This ends the game.

    return

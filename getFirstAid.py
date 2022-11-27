import re
from nltk.corpus import wordnet

#동의어 처리

list_words = ['cuts', 'Abrasions', 'strings', 'stings', 'splinter', 'sprains', 'strains', 'fever', 'congestion', 'cough', 'throat', 'gastrointestinal', 'skin', 'bruises', 'broken', 'choking','wound', 'frost']
list_syn = {}

for word in list_words:
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            # Remove any special characters from synonym strings
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)
    list_syn[word]=set(synonyms)

    
#Keyword dictionay 생성
keywords = {}
keywords_dict = {}
for word in list_words:
    keywords[word] = []
    for synonym in list(list_syn[word]):
        keywords[word].append('.*\\b'+synonym+'\\b.*')
for intent, keys in keywords.items():
    keywords_dict[intent] = re.compile('|'.join(keys))
    

#상황에 맞는 응답 생성
responses = {
    'cuts':"Wash the cut properly to prevent infection and stop the bleeding by applying pressure for 1-2minutes until bleeding stops. \nApply Petroleum Jelly to make sure that the wound is moist for quick healing.\nFinally cover the cut with a sterile bandage.\nPain relievers such as acetaminophen can be applied.",
    'Abrasions':"Begin with washed hands.\nGently clean the area with cool to lukewarm water and mild soap.\n Remove dirt or other particles from the wound using sterilized tweezers.\nFor a mild scrape that’s not bleeding, leave the wound uncovered.\nIf the wound is bleeding, use a clean cloth or bandage, and apply gentle pressure to the area to stop any bleeding.\nCover a wound that bled with a thin layer of topical antibiotic ointment, like Bacitracin, or a sterile moisture barrier ointment, like Aquaphor.\n Cover it with a clean bandage or gauze. Gently clean the wound and change the ointment and bandage once per day.\nWatch the area for signs of infection, like pain or redness and swelling.\n See your doctor if you suspect infection.",
    'strings':"Remove any stingers immediately.\n Some experts recommend scraping out the stinger with a credit card.\n Applying ice to the site may provide some mild relief.\n Apply ice for 20 minutes once every hour as needed.\n Wrap the ice in a towel or keep a cloth between the ice and skin to keep from freezing the skin.\n Taking an antihistamine such as diphenhydramine (Benadryl) or a nonsedating one such as loratadine (Claritin) will help with itching and swelling.\n Take acetaminophen (Tylenol) or ibuprofen (Motrin)for pain relief as needed.\n Wash the sting site with soap and water. Placing hydrocortisone cream on the sting can help relieve redness, itching, and swelling.",
    'splinter':"1. SOAK IT IN EPSOM SALTS.\n Dissolve a cup of the salts into a warm bath and soak whatever part of the body has the splinter.\n Failing that, you can also put some of the salts onto a bandage pad and leave it covered for a day; this will eventually help bring the splinter to the surface. \n2. VINEGAR OR OIL. Another simple way to draw out that stubborn splinter is to soak the affected area in oil (olive or corn) or white vinegar. Just pour some in a bowl and soak the area for around 20 to 30 minutes,",
    'sprains':"Use an ice pack or ice slush bath immediately for 15 to 20 minutes and repeat every two to three hours while you're awake.\n To help stop swelling, compress the ankle with an elastic bandage until the swelling stops.\n In most cases, pain relievers — such as ibuprofen (Advil, Motrin IB, others) or naproxen sodium (Aleve, others) or acetaminophen (Tylenol, others) are enough to manage the pain of a sprained ankle.",
    'strains':"Rest,Ice,Compression and Elevation can be used to cure strains.\n Avoid using your muscle for a few days, especially if movement causes an increase in pain and also Apply ice immediately after injuring your muscle.\n This will minimize swelling. Don’t put ice directly on your skin.\n Use an ice pack or wrap ice in a towel. \nTo reduce swelling, wrap the affected area with an elastic bandage until swelling comes down.",
    'fever':"To treat a fever at home: 1)Drink plenty of fluids to stay hydrated. 2)Dress in lightweight clothing. 3)Use a light blanket if you feel chilled, until the chills end. 4)Take acetaminophen (Tylenol, others) or ibuprofen (Advil, Motrin IB, others). 5) Get medical help if the fever lasts more than five days in a row.",
    'nasal congestion':"When you’re stuffed up, focus on keeping your nasal passages and sinuses moist. To keep your nasal passages moist, you can: 1)Use a humidifier or vaporizer. 2)Drink lots of fluids. This will thin out your mucus, which could help prevent blocked sinuses. 3)Place a warm, wet towel on your face. It may relieve discomfort and open your nasal passages.",
    'cough':"1) Honey:- Use honey to treat a cough, mix 2 teaspoons (tsp) with warm water or an herbal tea. Drink this mixture once or twice a day. Do not give honey to children under 1 year of age. 2) Ginger:- Brew up a soothing ginger tea by adding 20–40 grams (g) of fresh ginger slices to a cup of hot water. Allow to steep for a few minutes before drinking. Add honey or lemon juice to improve the taste and further soothe a cough. 3) Fluids:- Staying hydrated is vital for those with a cough or cold. Research indicates that drinking liquids at room temperature can alleviate a cough, runny nose, and sneezing.",
    'sore throat':"1) Make sure you get plenty of rest and drink a lot of fluids. 2)Inhale steam,Run hot water in a sink.Drape a towel over you to trap the steam, and have the person lean over the sink with the water running. Tell him to breathe deeply through his mouth and nose for 5 to 10 minutes. Repeat several times a day. 3)Have him sip chicken broth or warm tea with honey. Don’t give honey to a child under 12 months of age.",
    'gastrointestinal problems':"1) Replenish body fluids 2)Do not take antidiarrheal drugs or laxatives or pain medication, unless specified by a medical professional.3)Taking antacids may help, per recommendation of a healthcare professional. 4)If prone to frequent heartburns, seek medical help. 5)Taking meals that are not spicy regularly, can relieve ulcer pains. 6)Seek medical help, if conditions persist or continue to worsen",
    'skin':"1)Hydrocortisone cream. 2)Ointments like calamine lotion. 3)Antihistamines. 4)Cold compresses. 5)Oatmeal baths. 6)Talk to your doctor about what's best for your specific rash.",
    'abdonominal':"1)Provide clear fluids to sip, such as water, broth, or fruit juice diluted with water. 2)Serve bland foods, such as saltine crackers, plain bread, dry toast, rice, gelatin, or applesauce. 3)Avoid spicy or greasy foods and caffeinated or carbonated drinks until 48 hours after all symptoms have gone away. ",
    'bruises':"1)Ice the bruise with an ice pack wrapped in a towel. 2)Leave it in place for 10 to 20 minutes. 3)Repeat several times a day for a day or two as needed. 4)Compress the bruised area if it is swelling, using an elastic bandage. ",
    'broken':"1)To help decrease pain and swelling in a broken toe, elevate the foot, ice the injury, and stay off the foot. 2)Depending on the severity of the fracture, the toe may need to be put back into place (reduced), and some compound toe fractures may require surgery.3) Most broken toes heal without complications in six weeks.",
    'choking':"1)Encourage them to keep coughing to try to clear the blockage. 2)Ask them to try to spit out the object if it's in their mouth. 3)If coughing doesn't work, start back blows and Abdonominal thrusts",
    'wound':"1)Rinse the cut or wound with water and apply pressure with sterile gauze, a bandage, or a clean cloth. 2)If blood soaks through the bandage, place another bandage on top of the first and keep applying pressure. 3)Raise the injured body part to slow bleeding. 4)When bleeding stops, cover the wound with a new, clean bandage."
}

def get_response(user_response):
    user_input = user_response.lower()
    matched_intent = None
    for intent,pattern in keywords_dict.items():
        if re.search(pattern,user_input):
            matched_intent = intent
    key = 'fallback'
    if matched_intent in responses:
        key = matched_intent
    if key == "fallback":
        return "I can't help You"
    else:
        return responses[key]
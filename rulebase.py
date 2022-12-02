import re
from nltk.corpus import wordnet

symptomList =[
        {"tag": "Burn",
         "responses": ["1. Sun burn: Burn by Sunlight \n2. Chemical burn: Chemical burn \n3. Fire burn: Burn by fire."]
         },
        {"tag": "Dizziness",
         "responses": ["1. Vertigo : Symptoms such as rotation of oneself or surroundings \n2. Fainting : Symptoms that make one lose one's mind"]
         },
        {"tag": "Bleeding",
         "responses": ["1. Nose bleed : Bleeding from the nose \n2. Normal Bleeding : Bleeding from areas other than the nose \n3. Rectal Bleeding: Bleeding from the anus."]
        },
        {"tag": "Hot",
         "responses": ["1. Heat exhaustion : lethargy, temporary dizziness and headaches and vomiting \n2. Strains : Body temperature above 40 degrees, pulse rate, headache, dizziness, nausea, convulsions, and visual impairment symptoms"]
         }]

firstaidList=[
        {"tag": "Cuts",
         "responses": ["Wash the cut properly to prevent infection and stop the bleeding by applying pressure for 1-2minutes until bleeding stops. \nApply Petroleum Jelly to make sure that the wound is moist for quick healing. \nFinally cover the cut with a sterile bandage. \nPain relievers such as acetaminophen can be applied."]
        },
        {"tag": "Abrasions",
         "responses": ["Begin with washed hands.\nGently clean the area with cool to lukewarm water and mild soap. \nRemove dirt or other particles from the wound using sterilized tweezers.For a mild scrape that’s not bleeding, leave the wound uncovered.\nIf the wound is bleeding, use a clean cloth or bandage, and apply gentle pressure to the area to stop any bleeding.\nCover a wound that bled with a thin layer of topical antibiotic ointment, like Bacitracin, or a sterile moisture barrier ointment, like Aquaphor. \nCover it with a clean bandage or gauze. \nGently clean the wound and change the ointment and bandage once per day.\nWatch the area for signs of infection, like pain or redness and swelling. \nSee your doctor if you suspect infection."]
        },
        {"tag": "Stings",
         "responses": ["Remove any stingers immediately. \nSome experts recommend scraping out the stinger with a credit card. \nApplying ice to the site may provide some mild relief. \nApply ice for 20 minutes once every hour as needed. \nWrap the ice in a towel or keep a cloth between the ice and skin to keep from freezing the skin. \nTaking an antihistamine such as diphenhydramine (Benadryl) or a nonsedating one such as loratadine (Claritin) will help with itching and swelling. \nTake acetaminophen (Tylenol) or ibuprofen (Motrin)for pain relief as needed. \nWash the sting site with soap and water. \nPlacing hydrocortisone cream on the sting can help relieve redness, itching, and swelling."]
        },
        {"tag": "Splinter",
         "responses": ["1. SOAK IT IN EPSOM SALTS. Dissolve a cup of the salts into a warm bath and soak whatever part of the body has the splinter. Failing that, you can also put some of the salts onto a bandage pad and leave it covered for a day; this will eventually help bring the splinter to the surface. \n2. VINEGAR OR OIL. Another simple way to draw out that stubborn splinter is to soak the affected area in oil (olive or corn) or white vinegar. Just pour some in a bowl and soak the area for around 20 to 30 minutes,"]
        },
        {"tag": "Sprains",
         "responses": ["Use an ice pack or ice slush bath immediately for 15 to 20 minutes and repeat every two to three hours while you're awake. \nTo help stop swelling, compress the ankle with an elastic bandage until the swelling stops. \nIn most cases, pain relievers — such as ibuprofen (Advil, Motrin IB, others) or naproxen sodium (Aleve, others) or acetaminophen (Tylenol, others) are enough to manage the pain of a sprained ankle."]
        },
        {"tag": "Strains",
         "responses": ["Rest,Ice,Compression and Elevation can be used to cure strains. \nAvoid using your muscle for a few days, especially if movement causes an increase in pain and also Apply ice immediately after injuring your muscle. \nThis will minimize swelling. \nDon’t put ice directly on your skin. \nUse an ice pack or wrap ice in a towel. \nTo reduce swelling, wrap the affected area with an elastic bandage until swelling comes down."]
        },
        {"tag": "Fever",
         "responses": ["To treat a fever at home: \n1)Drink plenty of fluids to stay hydrated. \n2)Dress in lightweight clothing. \n3)Use a light blanket if you feel chilled, until the chills end. \n4)Take acetaminophen (Tylenol, others) or ibuprofen (Advil, Motrin IB, others). \n5) Get medical help if the fever lasts more than five days in a row."]
        },
        {"tag": "Nasal congestion",
         "responses": ["When you’re stuffed up, focus on keeping your nasal passages and sinuses moist. \nTo keep your nasal passages moist, you can: \n1)Use a humidifier or vaporizer. \n2)Drink lots of fluids. This will thin out your mucus, which could help prevent blocked sinuses. \n3)Place a warm, wet towel on your face. It may relieve discomfort and open your nasal passages."]
        },
        {"tag": "Cough",
         "responses": ["1) Honey:- Use honey to treat a cough, mix 2 teaspoons (tsp) with warm water or an herbal tea. Drink this mixture once or twice a day. Do not give honey to children under 1 year of age. \n2) Ginger:- Brew up a soothing ginger tea by adding 20–40 grams (g) of fresh ginger slices to a cup of hot water. Allow to steep for a few minutes before drinking. Add honey or lemon juice to improve the taste and further soothe a cough. \n3) Fluids:- Staying hydrated is vital for those with a cough or cold. Research indicates that drinking liquids at room temperature can alleviate a cough, runny nose, and sneezing."]
        },
        {"tag": "Sore throat",
         "responses": ["1) Make sure you get plenty of rest and drink a lot of fluids. \n2)Inhale steam,Run hot water in a sink.Drape a towel over you to trap the steam, and have the person lean over the sink with the water running. Tell him to breathe deeply through his mouth and nose for 5 to 10 minutes. Repeat several times a day. \n3)Have him sip chicken broth or warm tea with honey. Don’t give honey to a child under 12 months of age."]
        },
        {"tag": "Gastrointestinal problems",
         "responses": ["1) Replenish body fluids \n2)Do not take antidiarrheal drugs or laxatives or pain medication, unless specified by a medical professional.\n3)Taking antacids may help, per recommendation of a healthcare professional. \n4)If prone to frequent heartburns, seek medical help. \n5)Taking meals that are not spicy regularly, can relieve ulcer pains. \n6)Seek medical help, if conditions persist or continue to worsen"]
        },
        {"tag": "Skin problems",
         "responses": ["1)Hydrocortisone cream. \n2)Ointments like calamine lotion. \n3)Antihistamines. \n4)Cold compresses. \n5)Oatmeal baths. \n6)Talk to your doctor about what's best for your specific rash."]
        },
        {"tag": "Abdominal pain",
         "responses": ["1)Provide clear fluids to sip, such as water, broth, or fruit juice diluted with water. \n2)Serve bland foods, such as saltine crackers, plain bread, dry toast, rice, gelatin, or applesauce. \n3)Avoid spicy or greasy foods and caffeinated or carbonated drinks until 48 hours after all symptoms have gone away."]
        },
        {"tag": "Bruises",
         "responses": ["1)Ice the bruise with an ice pack wrapped in a towel. \n2)Leave it in place for 10 to 20 minutes. \n3)Repeat several times a day for a day or two as needed. \n4)Compress the bruised area if it is swelling, using an elastic bandage. "]
        },
        {"tag": "Broken toe",
         "responses": ["1)To help decrease pain and swelling in a broken toe, elevate the foot, ice the injury, and stay off the foot. \n2)Depending on the severity of the fracture, the toe may need to be put back into place (reduced), and some compound toe fractures may require surgery.\n3) Most broken toes heal without complications in six weeks."]
        },
        {"tag": "Choking",
         "responses": ["1)Encourage them to keep coughing to try to clear the blockage. \n2)Ask them to try to spit out the object if it's in their mouth. \n3)If coughing doesn't work, start back blows and Abdominal thrusts"]
        },
        {"tag": "Wound",
         "responses": ["1)Rinse the cut or wound with water and apply pressure with sterile gauze, a bandage, or a clean cloth. \n2)If blood soaks through the bandage, place another bandage on top of the first and keep applying pressure. \n3)Raise the injured body part to slow bleeding. \n4)When bleeding stops, cover the wound with a new, clean bandage."]
        },
        {"tag": "Diarrhea",
         "responses": ["1)Hydrating the body is essential for recovering from diarrhea.This causes the body to lose electrolytes such as sodium and chloride. \n2)It is highly recommended to avoid dairy products, as they may worsen diarrhea in some people. \n3)However, if diarrhea lasts for more than 2 days, seek medical advice to avoid complications."]
        },
        {"tag": "Frost bite",
         "responses": ["1)Check for hypothermia. Get emergency medical help if you suspect hypothermia. Signs of hypothermia include intense shivering, drowsiness, confusion, fumbling hands and slurred speech. \n2)Check for hypothermia. Get emergency medical help if you suspect hypothermia. Signs of hypothermia include intense shivering, drowsiness, confusion, fumbling hands and slurred speech. \n3) Get out of the cold. Once you're in a warm space, remove wet clothes and wrap up in a warm blanket. \n4)Gently rewarm frostbitten areas. Soak frostbitten fingers, toes or other extremities in warm water — 105 to 110 F (about 40 to 43 C). \n5).Don't rewarm frostbitten skin with direct heat, such as a stove, heat lamp, fireplace or heating pad. This can cause burns. \n6)Drink warm liquids. Tea, coffee, hot chocolate or soup can help warm you from the inside. Don't drink alcohol."]
        },
        {"tag": "Heat exhaustion",
         "responses": ["1)Call Doctor. \n2)Do not try to thaw frostbite unless you're in a warm place. \n3)Remove wet clothing. \n4)Don't rub frostbitten areas \n5)Don't use dry heat \n6)Don't break any blisters. \n7)Warm the frostbitten parts in warm (not hot) water for about 30 minutes. \n8)Place clean cotton balls between frostbitten fingers and toes after they've been warmed. \n9)Loosely wrap warmed areas with clean bandages to prevent refreezing."]
        },
        {"tag": "Heat stroke",
         "responses": ["1)call 119 \n2)Put the person in a cool tub of water or a cool shower. \n3) Spray the person with a garden hose \n4) Sponge the person with cool water. \n5)Fan the person while misting with cool water. \n6)Place ice packs or cool wet towels on the neck, armpits and groin. \n7)Cover the person with cool damp sheets."]
        },
        {"tag": "Insect bites",
         "responses": ["1)Move to a safe area to avoid more bites or stings. \n2)Remove any stingers. \n3)Gently wash the area with soap and water. \n4)Apply a cloth dampened with cold water or filled with ice to the area of the bite or sting for 10 to 20 minutes. This helps reduce pain and swelling. \n5)If the injury is on an arm or leg, raise it. 6)Apply to the affected area calamine lotion, baking soda paste, or 0.5% or 1% hydrocortisone cream. Do this several times a day until your symptoms go away. \n7)Take an anti-itch medicine (antihistamine) by mouth to reduce itching. Options include nonprescription cetirizine, fexofenadine (Allegra Allergy, Children's Allegra Allergy), loratadine (Claritin). \n8)Take a nonprescription pain reliever as needed. "]
        },
        {"tag": "Nose bleed",
         "responses": ["1)Sit upright and lean forward to discourages further bleeding. \n2)Gently blow your nose to clear your nose of blood clots. \n3)Pinch your nose. Use your thumb and index finger to pinch your nostrils shut. Breathe through your mouth. Continue to pinch for 10 to 15 minutes. \n4)To prevent re-bleeding, don't pick or blow your nose and don't bend down for several hours. Keep your head higher than the level of your heart. You can also gently apply some petroleum jelly to the inside of your nose using a cotton swab or your finger. \n5)If re-bleeding occurs, go through these steps again. Call your doctor if the bleeding continues."]
        },
        {"tag": "Pulled muscle",
         "responses": ["1)Remove all constrictive clothing, including jewelry, in the area of muscle strain. \n2)Protect the strained muscle from further injury. \n3)Rest the strained muscle. \n4)Ice the muscle area. Ice should not be applied to bare skin. Always use a protective covering such as a towel between the ice."]
        },
        {"tag": "Rectal bleeding",
         "responses": ["1)Keep track of the bleeding. \n2)If it happens one time and then stops, it most likely is not an emergency. Just take note of it. \n3)If you have heavy rectal bleeding you must reach out to your doctor for immediate care. Rectal bleeding may be symptoms for other diseases like hemorrhoids or even colorectal cancer."]
        },
        {"tag": "Sun burn",
          "responses": ["1)Cool down the burn with cold running water. \n2) Apply cool wet compresses until the pain subsides. \n3)Remove tight items from burned areas. \n4)Avoid breaking blisters. \n5)If a blister breaks apply antibiotic ointment. \n6)After the burned areas has been cooled. \n7)Loosely bandage the burn using sterilize gauze."]
        },
        {"tag": "Testicle pain",
         "responses": ["1)Take an over-the-counter pain reliever such as aspirin. Aspirin is approved for use in children older than age 3. \n2)However children and teenagers recovering from chickenpox or flu-like symptoms should never take aspirin. \n3)Advil, Motrin IB, Tylenol is also recommended \n4)Seek immediate medical attention if you have sudden, severe testicle pain or testicle pain accompanied by nausea, fever, chills or blood in your urine"]
        },
        {"tag": "Vertigo",
         "responses": ["1)Go see a doctor. You need medication that requires a doctors prescription."]
        },
        {"tag": "Normal bleeding",
         "responses": ["1)For severe bleeding first call 119 and remove any clothing or debris from the wound. Look for the source of the bleeding. There could be more than one injury. Remove any obvious debris but don't try to clean the wound. Don't remove large or deeply embedded objects, and don't probe the wound. \n2)Stop the bleeding. Cover the wound with sterile gauze or a clean cloth. Press on it firmly with the palm of your hand until bleeding stops. But don't press on an eye injury or embedded object. Don't press on a head wound if you suspect a skull fracture. \n3)Help the injured person lie down. If possible, place the person on a rug or blanket to prevent loss of body heat. Elevate the feet if you notice signs of shock, such as weakness, clammy skin or a rapid pulse. Calmly reassure the injured person. \n4)Keep the person still. If you're waiting for emergency help to arrive, try to keep the injured person from moving. \n5)Keep the person still. If you're waiting for emergency help to arrive, try to keep the injured person from moving. \n6)Wash your hands. After helping the injured person, wash your hands, even if it doesn't look like any blood got on your hands."]
        },
        {"tag": "Eye injury",
         "responses": ["1)Cold compresses: Icepacks reduce swelling and relieve pain. \n2)Eye flushing: Flush chemicals and other irritants with clean water for about 15 minutes. \n3)Eyedrops: Your provider may prescribe eyedrops to help your eye heal. \n4)Eye patch: By covering your eye, you’ll allow it to rest while it’s healing."]
        },
        {"tag": "Chemical burn",
         "responses": ["1)put on gloves and brush off any remaining chemicals. \n2)remove contaminated clothing or jewelry. \n3)cover the burn with clean bandage. \n4)If you feel more burning rinse the burned area again."]
        },
        {"tag": "Poison",
         "responses": ["1)Call 119. Actions while waiting vary from how the poison was entered into the person's system.  \n2)Swallowed poison. Remove anything remaining in the person's mouth. If the suspected poison is a household cleaner or other chemical, read the container's label and follow instructions for accidental poisoning. \n3)Poison on the skin. Remove any contaminated clothing using gloves. Rinse the skin for 15 to 20 minutes in a shower or with a hose. \n4)Poison in the eye. Gently flush the eye with cool or lukewarm water for 20 minutes or until help arrives. \n5)Inhaled poison. Get the person into fresh air as soon as possible. \n6)If the person vomits, turn his or her head to the side to prevent choking."]
        },
        {"tag": "Seizure",
         "responses": ["1)Call 119 \n2)Stay with the person until the seizure ends and he or she is fully awake. After it ends, help the person sit in a safe place. Once they are alert and able to communicate, tell them what happened in very simple terms. \n3)Comfort the person and speak calmly. \n4)Keep yourself and other people calm."]
        },
        {"tag": "Head injury",
         "responses": ["1)Call 119. \n2)For the first 24 hours after the injury, it's important for someone to stay with the injured person to keep an eye out for any new symptoms that develop. \n3)Most people are discharged fairly soon and should be able to recover at home."]
        },
        {"tag": "Fainting",
         "responses": ["1)Call 119 \n2)Make sure the person’s airway is clear. \n3)Check that the person is breathing. \n4)If a person is not breathing perform CPR."]
        },
        {"tag": "Headache",
         "responses": ["Give ibuprofen (Advil, Motrin), aspirin, or acetaminophen (Tylenol) for pain. \nAvoid ibuprofen and other NSAIDs if the person has heart failure or kidney failure. \nDo not give aspirin to a child under age 18."]
        },
        {"tag": "Cold",
         "responses": ["1)Keeping hydrated is absolutely vital to help 'flush' out the cold, as well as to break down congestion and keep your throat lubricated. \n2)Vitamin C is extremely helpful when fighting infection, so at the first sign of a cold be sure to increase your intake by eating plenty of berries, citrus fruits, papayas, broccoli and red peppers which will help keep you protected. \n3)When it comes to combating a cold,Vitamin D is essential in helping to regulate immune response."]
        },
        {"tag": "Rash",
         "responses": ["1)Olive oil helps in healing and promotes skin renewal given it is packed with vitamin E and antioxidants. It also soothes the skin and reduces itching. \n2)Baking soda is useful in drying skin rashes as also in relieving itching and inflammation. \n3)Aloe Vera,Thanks to its antibacterial, antifungal, anti-inflammatory and emollient properties, aloe vera is excellent for treating a number of skin ailments including rashes as also soothing the skin."]
        },
        {"tag": "Snake bite",
         "responses": ["While waiting for medical help: \n1)Move the person beyond striking distance of the snake. \n2)Have the person lie down with wound below the heart. \n3)Keep the person calm and at rest, remaining as still as possible to keep venom from spreading. \n4)Cover the wound with loose, sterile bandage. \n5)Remove any jewelry from the area that was bitten. \n6)Remove shoes if the leg or foot was bitten."]
        },
        {"tag": "Animal bite",
         "responses": ["1)Wash the wound with soap and warm water. \n2)Gently press a clean cloth over the wound to stop the flow of blood. \n3)Apply an antibacterial ointment to the wound. \n4)Cover with a sterile bandage. \n5)Watch for signs of infection. \n6)Seek help if you suspect infection or possible exposure to rabies, or if the wound is severe."]
        },
        {"tag": "Drowning",
         "responses": ["1)Place your ear next to the person's mouth and nose. Do you feel air on your cheek? \n2)Look to see if the person's chest is moving.If the Person is Not Breathing, Check Pulse. \n3)Check the person's pulse for 10 seconds.If There is No Pulse, Start CPR."]
        },
        {"tag": "CPR",
         "responses": ["1)For an adult or child, place the heel of one hand on the center of the chest at the nipple line. You can also push with one hand on top of the other. For an infant, place two fingers on the breastbone. \n2)For an adult or child, press down at least 2 inches. Make sure not to press on ribs. For an infant, press down about 1 and 1/2 inches. Make sure not to press on the end of the breastbone. \n3)Do chest compressions only, at the rate of 100-120 per minute or more. Let the chest rise completely between pushes. \n4)Check to see if the person has started breathing."]
        },
        {"tag": "Fracture",
         "responses": ["1)Stop any bleeding. Apply pressure to the wound with a sterile bandage, a clean cloth or a clean piece of clothing. \n2)Immobilize the injured area. Don't try to realign the bone or push a bone that's sticking out back in. If you've been trained in how to splint and professional help isn't readily available, apply a splint to the area above and below the fracture sites. Padding the splints can help reduce discomfort. \n3)Apply ice packs to limit swelling and help relieve pain. Don't apply ice directly to the skin. Wrap the ice in a towel, piece of cloth or some other material. \n4)Treat for shock. If the person feels faint or is breathing in short, rapid breaths, lay the person down with the head slightly lower than the trunk and, if possible, elevate the legs."]
        },
         {"tag": "Fire burn",
         "responses": ["1)Cool down the burn with cold running water. \n2) Apply cool wet compresses until the pain subsides. \n3)Remove tight items from burned areas. \n4)Avoid breaking blisters. \n5)If a blister breaks apply antibiotic ointment. \n6)After the burned areas has been cooled. \n7)Loosely bandage the burn using sterilize gauze."]
         }]

symptomTagList=[]
for tag in symptomList:
    symptomTagList.append(tag['tag'])
#print(symptomTagList)

firstaidTagList=[]
for faTag in firstaidList:
    firstaidTagList.append(faTag['tag'])
#print(firstaidTagList)

dict_syn={}
for word in symptomTagList:
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)
    dict_syn[word]=set(synonyms)
    dict_syn[word].add(word.lower())
dict_syn["Burn"].remove("sunburn")
dict_syn["Dizziness"].remove("vertigo")
dict_syn["Burn"].remove("cut")
#print(dict_syn)

dict_syn1={}
for word in firstaidTagList:
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)
    dict_syn1[word]=set(synonyms)
    dict_syn1[word].add(word.lower())
dict_syn1["Vertigo"].remove("dizziness")
#print(dict_syn1)

keywords={}
keywords_dict={}
for key in dict_syn:
    keywords[key]=[]
    for synonym in list(dict_syn[key]):
        keywords[key].append('.*\\b'+synonym+'\\b.*')

for intent, keys in keywords.items():
    keywords_dict[intent]=re.compile('|'.join(keys))
#print (keywords_dict)

keywords1={}
keywords_dict1={}
for key in dict_syn1:
    keywords1[key]=[]
    for synonym in list(dict_syn1[key]):
        keywords1[key].append('.*\\b'+synonym+'\\b.*')

for intent, keys in keywords1.items():
    keywords_dict1[intent]=re.compile('|'.join(keys))
#print (keywords_dict1)

def chatbot_answer(user_response):
    #print ("Where does it hurt?")
    user_input = user_response.lower()
    matched_intent = None 
    matched_intent1=None
    for intent,pattern in keywords_dict.items():
        if re.search(pattern, user_input): 
            matched_intent=intent
    for intent,pattern in keywords_dict1.items():
        if re.search(pattern, user_input): 
            matched_intent1=intent
    key='fallback' 
    if (((matched_intent in symptomTagList) and (matched_intent1 not in firstaidTagList)) or ((matched_intent=="Burn") and (matched_intent1=="Stings"))):
        key = symptomTagList.index(matched_intent)
        #print("Select the correct disease name from the following and enter it.")
        #print(symptomList[key]["responses"])
        #firstQ()
        return "Select the correct disease name from the following and enter it.\n" + str(symptomList[key]["responses"]).lstrip('[').rstrip(']')
    elif matched_intent1 in firstaidTagList:
        key = firstaidTagList.index(matched_intent1)
        #print(firstaidList[key]["responses"])
        return str(firstaidList[key]["responses"]).lstrip('[').rstrip(']')
    else:
        #print("Sorry, no data")
        return "Sorry, I don't have Data."
    
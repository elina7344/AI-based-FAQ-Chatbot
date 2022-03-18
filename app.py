# pip install Flask>=1.0.0 chatterbot>=1.0.0 chatterbot-corpus>=1.2.0 SQLAlchemy>=1.2
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

 # Creating ChatBot Instance
chatbot = ChatBot('FAQBot')

conversation = [
    "What is your name?",
    "My name is FAQbot",
    "Are you a robot?",
    "Yes, I am a robot",
    "Who made you?",
    "Team bugs and bots made me",
    "How can you help me?"
    "I can give you all answers to your queries about AICTE",
    "Are you real?",
    "I am a chatbot which can answer FAQs on AICTE",
    "What do you do?",
    "I am there to assist you with your questions regarding AICTE organisation."
]


AICTE=[
    "What is AICTE?",
    "AICTE stands for all India council for technical education.",
    "When did AICTE act came into existence?",
    "It was found in 1987",
    "what are the objectives of AICTE?",
    "Quality promotion in Technical education.",
    "what are the mission of AICTE?",
    "Emphasis on developing high quality institutions, academic excellence and innovative research.",
    "What are some initiatives undertaken by AICTE?",
    "Jal shakti abhyan, One person one tree, Smart India Hackathon, SWAYAM (Any time anywhere learning)",
    "What is the motive of Startup contest by AICTE?",
    "To promote student driven innovation and startups",
    "What is Smart India Hackathon?",
    "It is an innovative product development competition.",
    "First chairman of AICTE was appointed on?",
    "2nd July, 1993.",
    "what is AICTE-Yuvak Scheme?",
    "It stands for YOUTH UNDERTAKING VISIT FOR ACQUIRING KNOWLEDGE.",
    "What is meant by AICTE LILAVATI AWARD?",
    "This award is given to AICTE approved institutions, who have undertaken remarkable intervention for the cause and made an impact.",
    "In which year was first smart India Hackathon held?",
    "First Smart India Hackathon was conducted in the year 2017.",
    "Why is Smart India Hackathon held every year?",
    "A unique initiative to identify new and disruptive digital solutions for solving the challenges faced by our country under the program of Smart India Hackathon 2017.",
    "What is PMSSS scheme J&K 2021-22?",
    "The Prime Ministers Special Scholarship Scheme(PMSSS) is provided to J&K Students to pursue undergraduate studies outside the State of Jammu and Kashmir.",
    "What is AICTE Environment policy?",
    "It includes environment conservation policy to create awareness about natural resources.",
    "Where is the head office of AICTE located?",
    "Head office of AICTE is located in New-Delhi.",
    "How to contact AICTE?",
    "011-26131576-78.",
    "Which year was the Right to education act passed?",
    "The Right to Education Bill came into existence in August 2009.",
    "What is the full form of AICTE KARMA?",
    "Kaushal Augmentation and Restructuring Mission of AICTE.",
    "Motive of AICTE KARMA policy?",
    "Kaushal Augmentation and Restructuring Mission of AICTE” (KARMA)  is for all AICTE approved institutions in the country to overcome the dual challenge of scarcity of skilled manpower in jobs and low skill level of those who are presently in jobs."

]

Initiatives=[
    #SIH
    "What is Smart India Hackathon?",
    "Smart India Hackathon is a nationwide initiative to provide students a platform to solve some of pressing problems we face in our daily lives, and thus inculcate a culture of product innovation and a mindset of problem solving.",
    "How can I participate in SIH?",
    "For more details please visit https://sih.gov.in/",
    "How many people participate in Smart India Hackathon",
    "The last edition of the hackathon saw over 5 million+ students from various engineering colleges compete for the top prize at 35+ locations.",
    "What oppotunities does students get?",
    "In SIH, the students would also have the opportunity to work on challenges faced within the private sector organisations and create world class solutions for some of the top companies in the world.",
    #startUPS
    "What is Start-up policy?",
    "AICTE’s Student Start-up Policy launched by Shri Pranab Mukherjee,to guide and promote student driven innovations & start-ups in more than 10,000 AICTE approved institutions across the country.",
    "Where can I get more information about Start-up Policy",
    "For more information you can visit  the website: https://www.startup.aicte-india.org",
    "What is scope of Start-ups in India",
    "India has the potential and is on the track of becoming the global powerhouse of innovation and entrepreneurship activities in the world. With a dynamic growth in the number of start-ups in the country, corresponding numbers of stakeholders like, investors, incubators, mentors, accelerators, etc",
    "What are the strategies taken up by government of India for the growth of startups?",
    "Encouraging students to take up entrepreneurship as a preferred choice of carrer, Engaging investors and shareholders towards supporting programmes on innovation, Provide exposure and leadership opportunities for students, Advocate policy measures and guidelines regarding increased participation of students in innovation",
    #AICTE Vishwakarma Award 2020
    "What is Vishwakarma Award",
    "Vishwakarma Awards are given to encourage and motivate young students and institutions to raise their performance in their specific domains leading to significant contribution towards the growth and development of the nation as a whole.",
    #Clean and smart campus award
    "What is Clean and smart campus award?",
    "The award aims to seek engagement with all stakeholders, primarily the student community to draw their attention towards immense scope and potential that the Technology offers for abstract objectives such as cleanliness, sustainability, environment etc.",
    "Where to apply for clean and smart campus award?",
    "Visit: https://www.aicte-india.org/Initiatives/clean-green-campus",
    #national level programs
    "What are the national level programs conducted by AICTE?",
    "NEAT Sensitisation Webinar, NEAT Cell (For Faculty Members & Students), AICTE FIT India Challenge, IPC (For Faculty Members & Students), AICTE Quality Initiatives Webinar, FDC (For Faculty Members & Students), Student Projects Webinar, SDC Cell (For Students), SKILL India Mission by GOI , SDC (For Faculty Members & Students)",
    "Where can I get details about AICTE national level programs?",
    "Visit: https://aicte-india.org/exam-reforms",
    "What is AICTE-UKIERI?",
    "This workshops will provide an overview of the key leadership and management challenges facing educational practitioners today, with a focus on the application of effective leadership and management techniques and their beneficial impact on departmental and institutional performance."
    "Where can I apply for AICTE-UKIERI?",
    "Visit: https://facilities.aicte-india.org/ukieri/public/Information",
    "Where are the details for AICTE-UKIERI?",
    "Visit: https://www.aicte-india.org/Initiatives/ukieri2020"
]

Stats=[
    "Where can I check the approved Institutes by AICTE?",
    "Visit: https://facilities.aicte-india.org/dashboard/pages/dashboardaicte.php"
]

FAQAICTE=[
"Where I can find the information related to Approval Process ?",
"Information related to Approval Process 2020-21 available on AICTE Website's Home page>Quick Links>Approval Process.",
"Forgotten password for logging in AICTE Web Portal. What is the procedure to recover this?",
"Refer User Manual for Forgotten Password available at https://www.aicte-india.org",
"I have made Online Payment but amount is not updated in portal.",
"Generally, payment receipt gets updated immediately. In case, your payment receipt is not updated then click on View Transaction Button under Payment tab. Otherwise, it will get updated in 48 to 72 working hours (2 to 3 working days).",
"We want to change details which are non-editable / read-only?",
"Contact the Approval Bureau or Regional Office?",
"How to get New User-id and password (login credentials) for AICTE Web Portal?",
"Click on Sign Up link on AICTE Web-portal.",
"Is PAN No. field mandatory for 'Forgot Password' form?",
"No, PAN No. is not mandatory. Only User Id or any one of the Application Ids is required.",
"I am not able to generate report?",
"Refer User Manual for Report Generation”to generate Reports",
"Is Aadhaar/PAN details mandatory to update faculty details in AICTE Web Portal?",
"Yes.",
"I have saved my data. But same is not reflecting in Calculate Deficiency tab?",
"Click on calculate deficiency button, refresh the page and check."
 ]

Schemes=[
     "What are the various schemes offered by AICTE ?", 
     "AICTE offers Students Development schemes, Faculty Development schemes, Institutional Development schemes, Research & Innovation Development schemes and General Schemes",
     "What are the various student developments schemes available for students?",
     "The various schemes for Student development can be accessed with this link https://www.aicte-india.org/schemes/students-development-schemes",
     "What are the various Faculty development schemes?",
     "The various schemes for Faculty development can be accessed with this link https://www.aicte-india.org/schemes/staff-development-schemes",
     "What are the various Institutional Development Schemes offered by AICTE?",
     "The various schemes for Institutional development can be accessed with this link https://www.aicte-india.org/schemes/institutional-development-schemes",
     "What are the various Research & Innovations development schemes?",
     "The various schemes for Research & Innovation development can be accessed with this link https://www.aicte-india.org/schemes/research-innovations-development-schemes",
     "What are the various General development schemes?",
     "The various schemes for Research & Innovation development can be accessed with this link https://www.aicte-india.org/schemes/other-schemes"
]

OPPORTUNITIES=[
    "What is AICTE-IDEA LAb?",
    "AICTE has decided to establish AICTE-IDEA (Idea Development, Evaluation & Application) Lab in AICTE approved institutions, encouraging students for application of science, technologies, engineering and mathematics (STEM) fundamentals towards enhanced hands-on experience, learning by doing and product visualisation.",
    #opportunity for students
    "What is National Apprenticeship Training Scheme (NATS)",
    "The National Apprenticeship Training Scheme in India is a one year programme equipping technically qualified youth with practical knowledge and skills required in their field of work.",
    "What are the Scholarship offered from AICTE?",
    "AICTE-Saksham Scholarship Scheme ,AICTE Pragati Scholarship for Girls,AICTE PG (GATE/GPAT) Scholarship,AICTE-National Doctoral Fellowship Scheme,Prime Minister Special Scholarship Scheme (PMSSS), J&K",
    #opportunities for specially abled
    "How AICTE facilates Diffently abled person?",
    "To provide counselling to differently - abled students on the types of courses they could study at the higher education institutions.To ensure admission of as many differently-abled students as possible through the open quota and also through the reservation meant for them.",
    "what is AICTE-QUALITY IMPROVEMENT PROGRAMME?",
    "The main objective of the programme is to upgrade the qualification of the faculty members of the degree level institutions in the country. Scholarship @Rs. 15000/-PM and Rs. 5000/ PM are given to Ph.D/ M.Tech. Scholars. Total 106 QIP centers are in the country."
    
    
]  

Education=[
    "What are the views of AICTE on Education?", 
    "Education or teaching in the broadest sense is any act or experience that has a formative effect on the mind, character or physical ability of an individual. In its technical sense,  education is the process by which society deliberately transmits its accumulated knowledge, skills and values from one generation to another.",
    "What is The Right to Education?",
    "The Right to Education has been established as a basic human right: since 1952, Article 2 of the first Protocol to the European Convention on Human Rights obliges all signatory parties to guarantee the right to education. At world level, the United Nations' International Covenant on Economic, Social and Cultural Rights of 1966 guarantees this right under its Article 13.India has passed the Right to Education Bill 2009 in August 2009",
    "What are the various collaborations by AICTE?",
    "The various collaborations can be accessed with this link https://www.aicte-india.org/education/collaborations",
    "What are the AICTE policies?",
    "All India Council for Technical Education (AICTE) is mandated by Parliament for proper planning and coordinated development of the technical education system throughout the country. It is responsible of promotion, qualitative improvement and proper maintenance of norms and standards in the technical education system and for matters connected therewith.The ‘technical education’ as defined under AICTE Act 1987, includes programme of education, research and training, engineering, technology, architecture, town planning, management, pharmacy and applied arts & crafts.AICTE has now defined the procedures and regulations for the conduct of Technical Education through Blended learning mode."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)
trainer.train(AICTE)
trainer.train(Initiatives)
trainer.train(Stats)
trainer.train(FAQAICTE)
trainer.train(Schemes)
trainer.train(OPPORTUNITIES)
trainer.train(Education)



english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer_corpus = ChatterBotCorpusTrainer(english_bot)
trainer_corpus.train("chatterbot.corpus.english.greetings",
"chatterbot.corpus.english.conversations",
"chatterbot.corpus.english.emotion",
"chatterbot.corpus.english.humor",
"chatterbot.corpus.english.Science",
"chatterbot.corpus.english.Trivia",
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == '__main__':
    app.run()

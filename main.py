import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from nltk import word_tokenize, corpus
import json
import nltk
import openai
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer 
openai.api_key = ""


nltk.download('stopwords')
nltk.download('punkt')

def chatGpt(model,question):
    response = openai.Completion.create(
        engine=model,
        prompt=(f"Question: {question}\n"
                "Answer:"
                ),
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.5
                )
    answer = response.choices[0].text.split('\n')[0]
    return answer

def get_data_settings():
    global microphone
    global stop_word
    global asisstent_name
    global action_list
    global trainData

    microphone = sr.Recognizer()
    stop_word = set(corpus.stopwords.words("portuguese"))

    with open("database.json", "r") as settings_file:
        settings = json.load(settings_file)

        asisstent_name = settings["name"]
        action_list = settings["action_list"]

        settings_file.close()

    with open("train_db.json", "r") as train_file:
        train_temp = json.load(train_file)
        trainData = train_temp["data"]
        train_file.close()



def hear_voice():
    global microphone

    phrase = None

    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)

        frase = 'Diga alguma coisa: '
        print(frase)
        audio = microphone.listen(source, timeout=5, phrase_time_limit=5)
        
        try:
            phrase = microphone.recognize_google(audio,language='pt-BR')
        except Exception as e:
            pass

    return phrase

def hear_audio(audio):
    global microphone

    command = None

    with sr.AudioFile(audio) as source:
        fala = microphone.listen(source)
        try:
            command = microphone.recognize_google(fala, language='pt-BR')
        except Exception as e:
            pass

    return command

def remove_stop_word(phrase):
    global stop_word

    token_list = []
    
    for token in phrase:
        if token not in stop_word:
            token_list.append(token)

    return token_list


def get_tokenized_command(phrase):
    global asisstent_name

    action = None
    target = None

    token_phrase = word_tokenize(phrase, 'portuguese')

    if token_phrase:
        token_phrase = remove_stop_word(token_phrase)

        if len(token_phrase) >= 3:
            if asisstent_name != token_phrase[0].lower():
                action = "nao"
                target = "reproduzir"
            else:
                action = token_phrase[1].lower()
                target = token_phrase[2].lower()

    return action, target

def run_command(action,target):
    global action_list

    is_valid = False
    response = None

    if action and target:
        for item in action_list:
            if action == item["name"]:
                print(f'{item["name"]}: {item["target"]}')
                if target in item["target"]:
                    is_valid = True
                    response = item["response"]

                break

    return is_valid,response

def run_command_two(action,target):
    global action_list

    is_valid = False
    response = None

    if action and target:
        action_list_action_filtered = list(filter(lambda item: item["name"] == action, action_list))
        action_list_filtered = list(filter(lambda item: target in item["target"], action_list_action_filtered))
        if len(action_list_filtered) > 0:
                    is_valid = True
                    response = action_list_filtered[0]["response"]


    return is_valid,response

def send_response(response):
    if response == "":
        pass
    else:
        print(response)
        play_phrase(response)

def play_phrase(audio):
    tts = gTTS(audio,lang='pt-br')
    tts.save('temp.mp3')
    playsound('temp.mp3')

if __name__ == "__main__":
    get_data_settings()

    is_alive = True
    bot = ChatBot('Bot')
    trainer = ListTrainer(bot)

    trainer.train(trainData)

    while is_alive:
        try:
            command = hear_voice()
            print(f"processando o comando: {command}")

            if command:
                action, target = get_tokenized_command(command)

                phrase = bot.get_response(command)
                if float(phrase.confidence) > 0.5:  
                    answer = chatGpt("davinci",phrase)
                    send_response(answer)
                #is_valid, response = run_command_two(action, target)
                #if is_valid:
                #    answer = chatGpt("davinci",response)
                #    send_response(answer)
                else:
                    if action == None:
                        print("audio processado sem a key ana. Ignorar.")
                    else:
                        send_response("Não entendi o comando. Repita, por favor!")
        except KeyboardInterrupt:
            print("Tchau!")
            is_alive = False

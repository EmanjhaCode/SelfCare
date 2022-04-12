from django.shortcuts import render
from .models import *
from django.http import JsonResponse,HttpResponse

# XXXXXXX---------CHAT LIB START-------XXXXXXX
import json
import random
import pickle
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import load_model
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
import random

# XXXXXXX------END------XXXXXXXX

# Create your views here.
#
# lemmatizer = WordNetLemmatizer()
# intents = json.loads(open('media/intents.json').read())
# words = []
# classes = []
# documents = []
# ignore_letters = ['!', '?', ',', '.']
# for intent in intents['intents']:
#     for pattern in intent['patterns']:
#         word = nltk.word_tokenize(pattern)
#         words.extend(word)
#         documents.append((word, intent['tag']))
#         if intent['tag'] not in classes:
#             classes.append(intent['tag'])
#
# words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
# words = sorted(list(set(words)))
# classes = sorted(list(set(classes)))
#
# training = []
# output_empty = [0] * len(classes)
#
#
# for doc in documents:
#     bag = []
#     word_patterns = doc[0]
#     word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
#     for word in words:
#         bag.append(1) if word in word_patterns else bag.append(0)
#
#     output_row = list(output_empty)
#     output_row[classes.index(doc[1])] = 1
#     training.append([bag, output_row])
#
# random.shuffle(training)
# training = np.array(training)
# train_x = list(training[:, 0])
# train_y = list(training[:, 1])
# model = Sequential()
# model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(len(train_y[0]), activation='softmax'))
#
# sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
# hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
#
# def save_model(model_name=None):
#     if model_name is None:
#         model.save(f"{model_name}.h5", hist)
#         pickle.dump(words, open(f'{model_name}_words.pkl', 'wb'))
#         pickle.dump(classes, open(f'{model_name}_classes.pkl', 'wb'))
#     else:
#         model.save(f"{model_name}.h5", hist)
#         pickle.dump(words, open(f'{model_name}_words.pkl', 'wb'))
#         pickle.dump(classes, open(f'{model_name}_classes.pkl', 'wb'))
#
#
# def load_model(model_name=None):
#     if model_name is None:
#         words = pickle.load(open(f'{model_name}_words.pkl', 'rb'))
#         classes = pickle.load(open(f'{model_name}_classes.pkl', 'rb'))
#         model = load_model(f'{model_name}.h5')
#     else:
#         words = pickle.load(open(f'{model_name}_words.pkl', 'rb'))
#         classes = pickle.load(open(f'{model_name}_classes.pkl', 'rb'))
#         model = load_model(f'{model_name}.h5')
#
# def clean_up_sentence(sentence):
#     sentence_words = nltk.word_tokenize(sentence)
#     sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
#     return sentence_words
#
#
# def bag_of_words(sentence, words):
#     sentence_words = clean_up_sentence(sentence)
#     bag = [0] * len(words)
#     for s in sentence_words:
#         for i, word in enumerate(words):
#             if word == s:
#                 bag[i] = 1
#     return np.array(bag)
#
#
# def predict_class(sentence):
#     p = bag_of_words(sentence, words)
#     res = model.predict(np.array([p]))[0]
#     ERROR_THRESHOLD = 0.1
#     results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
#
#     results.sort(key=lambda x: x[1], reverse=True)
#     return_list = []
#     for r in results:
#         return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
#     return return_list
#
#
# def get_response(ints, intents_json):
#     try:
#         tag = ints[0]['intent']
#         list_of_intents = intents_json['intents']
#         for i in list_of_intents:
#             if i['tag'] == tag:
#                 result = random.choice(i['responses'])
#                 break
#     except IndexError:
#         result = "I don't understand!"
#     return result

# XXXXXXXX



a = []
a1 = []
def chat_bot(request):
    #
    # ran = random.randint(999,999999)
    # value = request.COOKIES.get('unm')
    #
    # if value == None:
    #     response = render(request,'bot_data.html')
    #     print('not set : ')
    #     response.set_cookie('unm', ran)
    #     value1 = request.COOKIES.get('unm')
    #     print('set : ',value1,'value random : ',ran)
    # else:
    #     value = request.COOKIES.get('unm')
    #     data = bot_user.objects.values_list().filter(user_id=value)
    #
    #     if data.count() == 0:
    #         bot_user(user_id=value,user_res=['hi'],bot_res=['Welcome']).save()
    #
    #     user_id = data[0][1].strip('][').split(', ')
    #     user_res = data[0][2].strip('][').split(', ')
    #     bot_res = data[0][3].strip('][').split(', ')
    #
    #     user_res1 = [ ]
    #     bot_res1 = [ ]
    #     for us in user_res:
    #         u = us.replace("\\", "").replace("'", ' ')
    #         user_res1.append(u)
    #     for bs in bot_res:
    #         b = bs.replace("\\", "").replace("'", ' ')
    #         bot_res1.append(b)
    # # print('print data',bot_res)
    # # print('print data',type(bot_res1))
    #
    #     if request.method == "POST":
    #         s=request.POST['feed']
    #         a1.append(s)
    #         user_res1.append(s.replace(",", ' '))
    #
    #         bot_user.objects.filter(user_id=value).update(user_res=user_res1)
    #         if s == '0526cs1234':
    #             a.clear()
    #             a1.clear()
    #         else:
    #             ints = predict_class(s)
    #             res = get_response(ints, intents)
    #
    #             a.append(res)
    #             bot_res1.append(res.replace(",", ' '))
    #
    #         bot_user.objects.filter(user_id=value).update(bot_res=bot_res1)
    #
    #     mylist = zip(bot_res,user_res)
    # # bid = request.META['HTTP_USER_AGENT']

        # response = render(request,'bot_data.html',{'data':'mylist'})


    # max_age=60*60*24*1
    return response


def chat_detail(request):
    return render(request,'bot.html',{'data':'here is msg'})

from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def Home(request):
    return render(request, 'home.html')

def count(request):
    text_value = request.GET['txt']
    word_list = text_value.split()
    word_count = len(word_list)
    word_dic = SetWordDic(word_list)
    return render(request, 'count.html',{'count':word_count,'totalword':word_dic})

def About(request):
    return render(request, 'about.html')

def SetWordDic(word_list):
    word_dic ={}
    for word in word_list:
        if word_dic.__contains__(word):
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    word_dic = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)
    return word_dic


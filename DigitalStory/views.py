from django.shortcuts import render
from django.urls import reverse
# Create your views here.

list_links = [
    {"url":"", "name":"Home", "top":1, "urlName":"DS_entrance"},
    {"url":"partI_1", "name":"I: Finance", "top":1, "urlName":"partI_1"},
    {"url":"partII_1", "name":"II: Crypto", "top":1, "urlName":"partII_1"},
    {"url":"partIII_1", "name":"III: Logic", "top":1, "urlName":"partIII_1"},
    {"url":"about", "name":"About", "top": 1},
]

def entrance(request):
    context = {
        'list_links':list_links,
        'active':"Home",
    }
    return render(request, 'cover.html', context)



def partI_1(request):
    context = {
        'list_links':list_links,
        'active':"I: Finance",
    }
    return render(request, 'part1/1_1.html', context)

def partI_2(request):
    context = {
        'list_links':list_links,
        'active':"I: Finance",
    }
    return render(request, 'part1/1_2.html', context)

def partI_3(request):
    context = {
        'list_links':list_links,
        'active':"I: Finance",
    }
    return render(request, 'part1/1_3.html', context)



def partII_1(request):
    context = {
        'list_links':list_links,
        'active':"II: Crypto",
    }
    return render(request, 'part2/2_1.html', context)

def partII_2(request):
    context = {
        'list_links':list_links,
        'active':"II: Crypto",
    }
    return render(request, 'part2/2_2.html', context)

def partII_3(request):
    encrypt = ['s', 'n', 's', 'y', 'y', 'l', 'p', 'h', 'n', 'x', 'j', 'd', 'd', 'l', 'u', 'h', 'c', 'y']
    encrypt_number = []
    for letter in encrypt:
        encrypt_number.append(ord(letter)-97)

    key = ['s', 'a', 'm', 'g', 'y', 'u', 'p', 's', 'a', 'r', 'a', 'p']
    key_number = []
    for letter in key:
        key_number.append(ord(letter)-97)

    key_extended = []
    key_number_extended = []
    for x in range(0, len(encrypt)):
        key_extended.append(key[x%len(key)])
        key_number_extended.append(key_number[x%len(key)])

    decrypt = []
    decrypt_number = []
    for x in range(0, len(encrypt)):
        decryption = encrypt_number[x] - key_number_extended[x]
        if (decryption<0):
            decryption += 26
        decrypt_number.append(decryption)
        decrypt.append(chr(decryption+97))

    print(decrypt)
    print(decrypt_number)

    context = {
        'list_links':list_links,
        'active':"II: Crypto",
        'key':key,
        'key_number':key_number,
        'encrypt':encrypt,
        'encrypt_number':encrypt_number,
        'key_extended':key_extended,
        'key_number_extended':key_number_extended,
        'decrypt':decrypt,
        'decrypt_number':decrypt_number,
    }
    return render(request, 'part2/2_3.html', context)

def partIII_1(request):
    context = {
        'list_links':list_links,
        'active':"III: Logic",
    }
    return render(request, 'part3/3_1.html', context)

def partIII_2(request):
    context = {
        'list_links':list_links,
        'active':"III: Logic",
    }
    return render(request, 'part3/3_2.html', context)

def partIII_3(request):
    context = {
        'list_links':list_links,
        'active':"III: Logic",
    }
    return render(request, 'part3/3_3.html', context)


def about(request):
    context = {
        'list_links':list_links,
        'active':"About"
    }
    return render(request, 'About.html', context)

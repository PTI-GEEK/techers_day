from flask import Flask
from os import environ
from random import choice
from functions import *

CITATIES = [
    [
        "Każdemu człowiekowi jest dany klucz do bram raju. Tym samym kluczem otwiera się bramy piekła.",
        "– Richard P. Feynman",
    ],
    [
        "Nie widzimy rzeczy takimi, jakie są. Widzimy je takimi, jakimi my jesteśmy.",
        "– Anais Nin",
    ],
    [
        "Dobro jest dobrem, nawet gdy nikt go nie czyni. Zło jest złem, nawet gdy wszyscy je czynią.",
        "– Augustyn z Hippony",
    ],
    [
        "W życiu każdego człowieka są dwa wielkie dni – pierwszy, w którym się rodzimy i drugi, w którym odkrywamy po co.",
        "– William Barclay",
    ],
    [
        "Życiowe wyzwania nie powinny Cię paraliżować. Powinny pomóc Ci odkryć, kim naprawdę jesteś.",
        "– Bernice Johnson Reagon",
    ],
    [
        "Istnieją dwa sposoby na łatwe prześliźnięcie się przez życie: wierzyć we wszystko lub wątpić we wszystko. Oba chronią nas przed samodzielnym myśleniem.",
        "– Alfred Korzybski",
    ],
    ["Każdy człowiek powinien żyć tak, by stanowić wzór dla innych.", "– Rosa Parks"],
    [
        "Życie jest jak jazda na rowerze. Żeby utrzymać równowagę, musisz być w ciągłym ruchu.",
        "– Albert Einstein",
    ],
    [
        "Człowiek, który w wieku pięćdziesięciu lat widzi świat tak samo, jak widział go mając dwadzieścia lat, zmarnował trzydzieści lat życia.",
        "– Muhammad Ali",
    ],
    [
        "Statek stojący w porcie jest bezpieczny, ale nie po to buduje się statki, by stały w portach.",
        "– John Augustus Shedd",
    ],
    [
        "Jeden dzień na raz – to wystarczy. Nie oglądaj się za siebie i nie martw się przeszłością, ponieważ jej już nie ma. I nie niepokój się o przyszłość, bo ta jeszcze nie nadeszła. Żyj teraźniejszością i rób to tak pięknie, by była warta wspominania.",
        "– Ida Scott Taylor",
    ],
    ["Nie licz dni, spraw by dni się liczyły.", "– Muhammad Ali"],
    [
        "Życia nie mierzy się ilością oddechów, ale ilością zapierających dech chwil.",
        "– Michael Vance",
    ],
    ["Jeśli idziesz przez piekło, nie zatrzymuj się.", "– Winston Churchill"],
    [
        "Tragedią życia nie jest śmierć, ale to czemu pozwalamy umrzeć w sobie, kiedy żyjemy.",
        "– Norman Cousins",
    ],
    [
        "Tragedią życia nie jest to, że tak szybko się kończy, ale że tak długo czekamy, by je zacząć.",
        "– W. M. Lewis",
    ],
    [
        "Śpiewaj jakby nikt nie słuchał. Kochaj jakby nikt nigdy Cię nie zranił. Tańcz jakby nikt nie patrzył. I żyj tak jakby to było niebo na ziemi.",
        "– Mark Twain",
    ],
    [
        "Gdyby życie było sprawiedliwe Elvis by żył, a wszystkie jego sobowtóry byłyby martwe.",
        "– Johnny Carson",
    ],
    [
        "Dwie rzeczy są nieskończone: wszechświat i ludzka głupota. Choć nie jestem pewien, co do wszechświata.",
        "– Albert Einstein",
    ],
    [
        "Najlepszy czas na sadzenie drzew był dwadzieścia lat temu. Drugi najlepszy czas jest teraz.",
        "– Anonim",
    ],
    [
        "Istnieją tylko dwa sposoby na życie – żyć tak jakby nic nie było cudem lub tak jakby cudem było wszystko.",
        "– Albert Einstein",
    ],
    [
        "Bóg jest komikiem grającym dla publiczności zbyt przestraszonej, by się śmiać.",
        "– Wolter",
    ],
    [
        "Lepiej jest być nienawidzonym za to, kim jesteś, niż być kochanym za to, kim nie jesteś.",
        "– Andre Gide",
    ],
    [
        "W życiu nie chodzi o to, by siebie odnaleźć. W życiu chodzi o to, aby siebie samego stworzyć.",
        "– George Bernard Shaw",
    ],
    [
        "Mamy skłonność, by oceniać innych poprzez ich zachowanie, a siebie poprzez nasze intencje.",
        "– Albert F. Schlieder",
    ],
    [
        "Jesteśmy tym, co wielokrotnie powtarzamy. Doskonałość zatem nie jest jednorazowym aktem, a nawykiem.",
        "– Will Durant",
    ],
    [
        "Zwycięzcy nigdy się nie poddają. Ci, którzy się poddają, nigdy nie zwyciężają.",
        "– Vince Lombardi",
    ],
    [
        "Różnica pomiędzy niemożliwym a możliwym leży w determinacji człowieka.",
        "– Tommy Lasorda",
    ],
    [
        "Czy nie przyjemnie wiedzieć, że jest tak dużo rzeczy, które jeszcze poznamy? To właśnie sprawia, że tak cieszę się życiem…",
        '– L. M. Montgomery „Ania z Zielonego Wzgórza"',
    ],
    [
        "Jeżeli robisz to, co łatwe, Twoje życie będzie trudne. Jeśli robisz to, co trudne, Twoje życie będzie łatwe.",
        "– Les Brown",
    ],
    [
        "Prawdziwie żyć to najrzadsza rzecz na świecie. Większość ludzi jedynie egzystuje.",
        "– Oscar Wilde",
    ],
    [
        "Najważniejszą rzeczą jest, aby cieszyć się swoim życiem – być szczęśliwym – tylko to się liczy.",
        "– Audrey Hepburn",
    ],
    [
        "Jesteśmy tym, co w swoim życiu powtarzamy. Doskonałość nie jest jednorazowym aktem, lecz nawykiem.",
        "– Arystoteles",
    ],
    [
        "Życia nie należy brać zawsze tak śmiertelnie poważnie, inaczej nie jest godne tego, aby je przeżyć.",
        "– Licia Troisi",
    ],
    [
        "Życie jest jak jazda na rowerze. Żeby utrzymać równowagę, musisz być w ciągłym ruchu.",
        "– Albert Einstein",
    ],
    ["Nie odnajdziesz spokoju, unikając życia.", "– Virginia Woolf"],
    ["Życie zaczyna się po opuszczeniu wygodnego kokonu.", "– Neale Donald Walsh"],
    [
        "Sprawdź przed ważną decyzją, czy nie bierzesz twoich życzeń za rzeczywistość.",
        "– Józef Maria Bocheński",
    ],
    [
        "Tylko głupcy szukają prawd bez żadnych wyjątków, przez co mają nieustanne kłopoty z własnym szczęściem, z żonami, a nawet z uruchomieniem samochodów. Mądrzy natomiast zdają sobie sprawę, że życie składa się niemal z samych odstępstw od rozmaitych reguł. W bezkresnej pustyni można spotkać rzekę czy oazę z życiodajną wodą, a bywali i tacy, co zmarli z pragnienia tam, gdzie wody było pod dostatkiem.",
        "– Zbigniew Nienacki",
    ],
    [
        "Od wczesnego dzieciństwa podają nam na łyżeczce całą mądrość, jaką nagromadziła ludzkość. Każdego dnia słyszymy: „Cicha woda brzegi rwie”, „Póki życia, póty nadziei”, „Nie ma tego złego, co by na dobre nie wyszło” i tym podobne, a wszystko to jak rzucanie grochem o ścianę. Dopóki człowiek sam się nie potknie o kamień, o który przewróciły się już miliony ludzi, niczego nie zrozumie i niczego się nie nauczy.",
        "– B. Akunin",
    ],
]



app = Flask(__name__)

@app.route('/')
def hello():
    citate = choice(CITATIES)
    html = "<pre>" + prepare("Adam", citate=citate) + "</pre>"
    return html



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=environ.get("PORT", 5000))

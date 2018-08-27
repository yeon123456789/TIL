import webbrowser

keywords = ["아이유", "한지민", "슬기"]
url = "https://search.naver.com/search.naver?query="

'''webbrowser.open(url + keywords[0]) #주어 동사 관계처럼 생각 A(주어).B(동사)
webbrowser.open(url + keywords[1])
webbrowser.open(url + keywords[2])'''
#DRY : DO NOT REPEAT YOURSELF

for name in keywords:
    webbrowser.open(url + name)

Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:39:00) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random as ran

def hangman(word):
    wrong = 0 #何回間違えたか記録
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word) #wordを1文字ずつリスト化
    board = ["__"] * len(word) #wordの文字数を初め隠しておく、ヒントを出す
    win = False
    print("Welcome to Hangman")
    
    while wrong<len(stages)-1:
      print("\n")
      msg="1文字を予想してね"
      char=input(msg)
      if char in rletters:
        cind=rletters.index(char)
        board[cind]=char
        rletters[cind]="$"
      else:
        wrong+=1
      print("".join(board))
      e=wrong+1
      print("\n".join(stages[0:e]))
      if "__" not in board:
        print("あなたの勝ち！")
        print("".join(board))
        win=True
        break
    if not win:
      print("\n".join(stages[0:wrong+1]))
      print("あなたの負け！正解は{}です。".format(word))

wlist=["enoki","kinoko","nintendo"]    #　ワード追加していいよby えのき
k=wlist[ran.randint(0,3)]
hangman(k)

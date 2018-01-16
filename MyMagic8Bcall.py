import random

#답변
ans1="자! 해봐!"
ans2="됐네, 이 사람아."
ans3="뭐? 다시 생각해봐."
ans4="모르니까 두려운거야."
ans5="제 정신이 아니구나?"
ans6="너라면 할 수 있어!"
ans7="하든가 말든가 상관없잖아?"
ans8="맞아, 잘했네."

print("MyMagic8Bcall에 오신 것을 환영합니다.")

#질문 입력
question=input("질문을 입력하고 Enter키를 누르세요.\n:")
print("고민 중...\n"*4)

#질문에 대한 답변
choice=random.randint(1,8)
if choice==1:
    answer=ans1
elif choice==2:
    answer=ans2
elif choice==3:
    answer=ans3
elif choice==4:
    answer=ans4
elif choice==5:
    answer=ans5
elif choice==6:
    answer=ans6
elif choice==7:
    answer=ans7
else :
    answer=ans8

print("MyMagic8Bcall:",answer)
input("\n\nEnter키로 종료")

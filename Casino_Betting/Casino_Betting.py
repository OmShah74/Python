import random
print('''Casino Royale Grand Guessing Game\n
  ****Guess a number from 1 to 6  and an alphabet from english and if the 
  guess is right, about number and wrong about alphabet,your ammount will 
  be deducted by 10$ first and then will be doubled if number is wrong and 
  alphabet is right, then your amount will be multiplied by 10 after deducting 
  10$ and if both ate wrong, 20$ will be deducted from your account***''')
l1=[1,2,3,4,5,6]
s='abcdefghijklmnopqrstuvwxyz'
l2=list(s)
bamt=int(input('Enter betting amount (min 500$)\n'))
while True:
    print('''Enter choice to:
    1. Play
    2. Exit''')
    choice=int(input())
    if choice==1:
        ninp=int(input('Enter a number between 1 to 6 (including) and an alphabet\n'))
        alinp=input()
        nout=random.choice(l1)
        alout=random.choice(l2)
        if ninp==nout and alinp!=alout:
            print('''Right choice of number! 
                  'But wrong choice of alphabet 
                  Alphabet is: ''',alout)
            bamt-=10
            bamt*=2
        elif ninp!=nout and alinp==alout:
            print('''Right choice of alphaabet! 
                  'But wrong choice of number 
                  Number is: ''',nout)
            bamt-=10
            bamt*=10
        else:
            print('Sorry wrong choice of number and alphabet!')
            print('Number: ',nout,'\nAlphabet: ',alout)
            bamt-=20
    elif choice==2:
        print('''Thank you for being with us!
        Your total balance is: ''',bamt,'$')
        break


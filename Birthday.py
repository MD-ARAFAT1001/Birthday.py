#______DARK NET HACKER BOYS_____#
#______WRITTEN BY ARAFAT_________#
#______IMPORT________#
import random 
import os
from os import system as clr

#______COLOR_________#
B="\033[1;30m"         # Black
R="\033[1;31m"            # Red
G="\033[1;32m"         # Green
Y="\033[1;33m"        # Yellow
N="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
W="\033[1;37m"         # White
my_color = [
 B,C,P,W]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#______LOGO__________#
logo=(f'''
{R} ██   ██  █████  ██████  ██████  ██    ██                     
{Y} ██   ██ ██   ██ ██   ██ ██   ██  ██  ██                      
{G} ███████ ███████ ██████  ██████    ████                       
{C} ██   ██ ██   ██ ██      ██         ██                        
{W}██   ██ ██   ██ ██      ██         ██                        
                                                             
                                                             
{W}██████  ██ ██████  ████████ ██   ██ ██████   █████  ██    ██ 
{C}██   ██ ██ ██   ██    ██    ██   ██ ██   ██ ██   ██  ██  ██  
{G}██████  ██ ██████     ██    ███████ ██   ██ ███████   ████   
{R}██   ██ ██ ██   ██    ██    ██   ██ ██   ██ ██   ██    ██    
{N}██████  ██ ██   ██    ██    ██   ██ ██████  ██   ██    ██    
__________________________________________{Y}''')
#______line____________#
def line():
	print(f' __________________________________________{Y}')
#______clear________#
def clear():
    clr('clear')
    print(logo)
    print(f"{Y}HAPPY BIRTHDAY BORO VAI")
    line()
    print(f"{G}AMAR JONNO DOYA KOREN")
    line()
    print(f"{Y}AMI ZENO APNADER MOTO HOTE PARI")
    line()
#______main_________#
def main():
    clear()
    print(f'{Y}[01] PLZ CLICK ')
    line()
    print(f'{R}[00] EXIT')    
    line()
    option=input(f'{C}[??] CHOICE MENU : ')
    if option in ['1','01']:
        Munna()
    else:
        exit('LAST OFF ALL ASSALAMUALAIKUM VAIYA AND THANKS FOR EVERYTHING:) ')
def Munna():
    print (f"""{Y}
       _   _   _   _   _              
  / \ / \ / \ / \ / \             
 ( H | A | P | P | Y )            
  \_/ \_/ \_/ \_/ \_/             
   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ 
 ( B | I | R | T | H | D | A | Y )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
 ____________________________
 | Happy birthday Vaiya      |
 _____________________________ """)   
#______end___________#
main()
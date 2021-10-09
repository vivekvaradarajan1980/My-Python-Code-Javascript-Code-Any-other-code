import sys

import csv

import random

import numpy as np

from collections import defaultdict

"""infinite deck of cards """ 

class Hand:
     
     def __init__(self,cards=None):
          if(cards!=None):
               self.cards=cards
               self.score()
          else:
               self.cards=[]

     def score(self):
          soft_ace_count=0
          """normalize the cards by casting 11,12 and 13 to 10"""
          cards=list(map(lambda each:(each>10)*10+(each<11)*each,self.cards))
          tempSum=sum(cards)
          """check for soft_ace_count by adding 10 to the sum if ace is present"""
          if(cards.count(1)>=1 and (tempSum+10)<=21):
               soft_ace_count=1
               tempSum=tempSum+10
                    
          self.total=tempSum
          self.soft_ace_count=soft_ace_count

     def add_card(self):
          self.cards.append(random.randint(1,13))
          self.score()

     def is_blackjack(self):
          if(self.total==21):
               return True
          else:
               return False
               
     def is_bust(self):
          if(self.total>21):
               return True
          else:
               return False


     def __str__(self):
          return str(self.cards)
          
          


                   


class Strategy:

     def __init__(self,stand_on_value,stand_on_soft):
          self.SoV=stand_on_value
          self.SoF=stand_on_soft

     def __str__(self):
          if(self.SoF==False):
               return "H"+str(self.SoV)
          else:
               return "S"+str(self.SoV)

     def stand(self,hand):
          
           if(hand.total<self.SoV):
               result= False

           if(self.SoF==False and hand.total==self.SoV):
               if(hand.soft_ace_count==0):
                    result= True
               if(hand.soft_ace_count==1):
                    result= False


           if(self.SoF==True and hand.total==self.SoV):
               result= True
          
                   
           # stand on values greater than threshold
           if(hand.total>self.SoV):
               result= True

           return result
          
     def play(self): 

          playHand=Hand()
          playHand.add_card()
          playHand.add_card()
          
          while(not self.stand(playHand)):
               playHand.add_card()
          

          return playHand
                   
      
      
        
          
          
if(__name__=='__main__'):

     try:
          simcount=int(sys.argv[1])
     except Exception as err:
          print(err)
          
     playerResult=defaultdict(list) # store each simulation value of each  possible combination
     for iP in range(13,21):
          for ps in [False,True]:            # loop thru player strategy 
          
               for sim in range(simcount):   # loop thru simulations
                    
               
                    pS=Strategy(iP,ps)       # choose player strategy
                    pH=pS.play()
                    
                    for iD in range(13,21):
                         for ds in [False, True]:  # loop thru dealer strategy 
                              dS=Strategy(iD,ds)   # choose dealer strategy
                              dH=dS.play()
                              
                              
                              if(pH.is_bust()):
                                   playerResult[str(pS)+str(dS)].append(0)
                               
                              
                                                            
                              if(dH.is_bust() and pH.total<21):
                                   playerResult[str(pS)+str(dS)].append(1)
                                 
                                   
                              if(pH.total<21 and dH.total<21):
                             
                             
                                   if(pH.total>dH.total):
                                        playerResult[str(pS)+str(dS)].append(1)
                                        
                                   if(pH.total==dH.total):
                                        # for push store a -1 in the simulatio1n
                                        playerResult[str(pS)+str(dS)].append(0)
                                        
                                   if(pH.total<dH.total):
                                         playerResult[str(pS)+str(dS)].append(0)
                                        
                                      
                              if(pH.is_blackjack() and not dH.is_blackjack()):
                                    playerResult[str(pS)+str(dS)].append(1)
                                 

                              if(dH.is_blackjack() and pH.total<21):
                                    playerResult[str(pS)+str(dS)].append(0)
                                    
                                   

                              if(dH.is_blackjack() and pH.is_blackjack()):
                                   playerResult[str(pS)+str(dS)].append(0)
                             

                                  
                       
                           
     playStat={}
          
     for key in playerResult.keys():          
               playStat[key]=sum(playerResult[key])/simcount
     tableresults=np.reshape(np.array(list(playStat.values())),(16,16))  
          
               
                         
                                      
     with open('Percentages.csv','w') as csvfile:
          writer=csv.writer(csvfile)
          
          rowheader=[]
          colheader=[]
          for i in range(13,21):
               for s in [False, True]:
                    dS=Strategy(i,s)
                    rowheader.append('D-'+str(dS))
                    colheader.append('P-'+str(dS))
                                               
        #  writer.writerow(header)
          tableresults=np.append(np.reshape(np.array(rowheader),(1,16)),tableresults,0)
          tableresults=np.append(np.reshape(np.array(['Strategy']+colheader),(17,1)),tableresults,1)
          
          writer.writerows(tableresults)          
                    
     
          
                    
               
          
          
          
     
     

          

     
                    
               
               
          
          




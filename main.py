#source code https://fbchat.readthedocs.io/en/stable/intro.html

from logging import currentframe
from time import sleep
from fbchat import log, Client
from fbchat.models import *

import time
import random
import json

import database
import login


# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    begin_chat = False

# evaluate when text message is received from ThreadType.USER
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        
        data = (database) # my custom dictionary
        
        fetched_msg=message_object.text.lower()         #fetches other person message and lowercase it all
        fetched_first_word=fetched_msg.split()[0]       #fetches other person first word only
        fetched_last_word=fetched_msg.split()[-1]
        fetched_firstthree_letterword = ""              #localize first three letters in word
        fetched_second_word = ""                        #localize second word

        #fetch thread details for color purposes
        thread_details = self.fetchThreadInfo(thread_id)[thread_id]

        #fetch info of other person's chat history and message detalis
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))  


        #evaluate if localized variable content is not empty
        try:
            fetched_firstthree_letterword = fetched_first_word[0:3]
        except:
            print("The firstthree_letterword is less than 3")
            fetched_firstthree_letterword = ""
        finally:
            print(fetched_firstthree_letterword)


        try: 
            fetched_second_word=fetched_msg.split()[1]
        except:
            print("Second word doesn't exist... leaving it to none")
            fetched_second_word = ""
        finally:
            print(fetched_second_word)
        

        #reply function can send 4 messages consecutively
        def reply(arg1, arg2='', arg3='', arg4=''):
            
            def delay():                        #delay set to 3 seconds           
                time.sleep(3)

            args = [arg1, arg2, arg3, arg4]     #place reply arguments to the args array
            for x in range(len(args)):          #loop and evaluate each loop if not empty then break if it is
                if(args[x] != ""):
                    self.send(Message('[Ai Jeon beta] '+args[x]), thread_id, thread_type)
                else:
                    break
            self.begin_chat = False             #to prevent constant evaluation if thread color is not green
            delay()                             #to increment time to evaluate an unrecognized dict reply from other person


        def fetchUsrMsg():
            if (author_id != self.uid):         #only read content if i didnt send message to myself id
                
                #if thread theme color is green then allow constant listener evaluating variable 
                if(thread_details.color == ThreadColor.FREE_SPEECH_GREEN and self.begin_chat == False):
                    self.begin_chat = True

                #the same function but will change thene color once
                elif (thread_details.color != ThreadColor.FREE_SPEECH_GREEN and self.begin_chat == False):
                    self.changeThreadColor(ThreadColor.FREE_SPEECH_GREEN, thread_id)
                    self.begin_chat = True

                #if evaluating variable is set to True then continuously evaluate message until reaches unrecognized
                if(self.begin_chat == True):

                    for greet_word in data.content.greet_word:
                        if(fetched_firstthree_letterword == greet_word or fetched_first_word == greet_word):
                            reply(random.choice(data.content.greet_word_reply))
                            break

                    for greet_word_day in data.content.greet_word_day:
                        if(fetched_second_word == greet_word_day or fetched_first_word == greet_word_day):
                            reply("good day! i still cant read time at the moment", "ill notify joe.. he's probably not busy", 'in the meantime he\'d come by, is there anything else i could do for you?')
                            break

                    for confused in data.content.confused:
                        if(fetched_firstthree_letterword == confused or fetched_first_word == confused):
                            reply(random.choice(data.content.confused_reply))
                            if(self.counter_confused == 0 or (self.counter_confused % 6) == 0):
                                reply('ur talking to an ai bot')
                                break
                            else:
                                break

                    for other in data.content.miscalaneous:
                        if(fetched_first_word == other):
                            reply('test works fine')
                            break
                    
                    if (fetched_first_word == '$help'):
                        reply('help is currently in development', 'sorry', 'joe will be here in a moment')

                    if(fetched_first_word == 'counter'):
                        reply(str(self.counter_confused))

                    recent_time = int(str(message_object.timestamp)[:-3])
                    current_time = int(time.time())
                    

                    if((recent_time <= current_time and recent_time >= current_time -3) and author_id != self.uid):
                        reply(random.choice(data.content.unrecognized))
                        if(random.randint(0,8) == 2):
                            reply("im an integrated Ai bot made by Joe")
                            if((self.counter_confused % 3) == 0):
                                reply(random.choice(data.content.confused_reply))
                                self.counter_confused += 1
                        elif(random.randint(0,2) == 1):
                            reply("type $help")

                self.markAsDelivered(author_id, thread_id)

        if(thread_type == ThreadType.USER and author_id != '571083554'):
            fetchUsrMsg()


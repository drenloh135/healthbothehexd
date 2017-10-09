import os
import sys
import telepot
from telepot.delegate import pave_event_space, per_chat_id, create_open, per_callback_query_origin
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
import random


urls = ['https://www.bbcgoodfood.com/recipes/artichoke-aubergine-rice',
        'https://www.bbcgoodfood.com/recipes/roast-chicken-sweet-potato-gremolata-salad-0',
        'https://www.bbcgoodfood.com/recipes/coconut-quinoa-chia-porridge',
        'https://www.bbcgoodfood.com/recipes/baked-sea-bass-lemon-caper-dressing',
        'https://www.bbcgoodfood.com/recipes/butternut-soup-crispy-sage-apple-croutons',
        'https://www.bbcgoodfood.com/recipes/1570636/quick-mushroom-and-spinach-lasagne',
        'https://www.bbcgoodfood.com/recipes/8035/smoky-bacon-pot-noodle-for-one',
        'https://www.bbcgoodfood.com/recipes/sesame-salmon-purple-sprouting-broccoli-sweet-potato-mash',
        'https://www.bbcgoodfood.com/recipes/mumsys-vegetable-soup',
        'https://www.bbcgoodfood.com/recipes/pointed-cabbage-white-wine-fennel-seeds']

tips = ['Don\'t Drink Sugar Calories', 'Eat Nuts', 'Avoid Processed Junk Food',
        'Eat Fatty Fish', 'Don\'t Fear Coffee', 'Get Enough Sleep',
        'Take Care of Your Gut Health With Probiotics and Fiber', 'Eat Vegetables and Fruits',
        'Do Some Cardio, or Just Walk More', 'Use Extra Virgin Olive Oil',
        'Don\'t Eat a Lot of Refined Carbohydrates', 'Don\'t Fear Saturated Fat']

##https://www.healthline.com/health/deskercise#overview1
headStretch = ['https://www.healthline.com/hlcmsresource/images/topic_centers/Fitness-Exercise/400x400_Stretches_to_Do_at_Work_Every_Day_Shoulder_Pec_Stretch.gif' +
               '\nClasp hands behind your back\nPush the chest outward, and raise the chin\nHold pose for 10-30s',
               'https://www.healthline.com/hlcmsresource/images/topic_centers/Fitness-Exercise/400x400_Stretches_to_Do_at_Work_Every_Day_Shoulder_Shrug.gif' +
               '\nRaise both shoulders towards the ears\nDrop them and repeat 10 times',
               'https://www.healthline.com/hlcmsresource/images/topic_centers/Fitness-Exercise/400x400_Stretches_to_Do_at_Work_Every_Day_Neck_Stretch.gif' +
               '\nRelax and lean head forward\nSlowly roll toward one side and hold for 10s' +
               '\nRepeat on the other side\nRelax and go back to starting position\nDo this 3 times']

torsoStretch = ['https://www.healthline.com/hlcmsresource/images/topic_centers/Fitness-Exercise/400x400_Stretches_to_Do_at_Work_Every_Day_Forward_Stretch.gif' +
                '\nClasp your hands in front of you and lower your head in line with your arms\nPress forward and hold for 10-30seconds',
                'https://www.healthline.com/hlcmsresource/images/topic_centers/Fitness-Exercise/400x400_Stretches_to_Do_at_Work_Every_Day_Torso_Stretch.gif' +
                '\nPlace your feet firmly on the ground\nTwist upper body in the direction of resting arm' +
                '\nHold pose for 10-30 seconds\nRepeat on the other side',
                'https://www.healthline.com/hlcmsresource/images/topic_centers/Fitness-Exercise/400x400_Stretches_to_Do_at_Work_Every_Day_Upper_Body_Stretch.gif' +
                '\nClasp hands together above head with palms facing out' +
                '\nPush your arms out, stretching upward and hold it for 10-30 seconds']

legStretch = ['https://www.healthline.com/hlcmsresource/images/topic_centers/Fitness-Exercise/400x400_Stretches_to_Do_at_Work_Every_Day_Hip_and_Knee_Flexion.gif' +
              '\nHug one knee and pull it towards your chest\nHold pose for 10-30 seconds and alternate',
              'https://www.healthline.com/hlcmsresource/images/topic_centers/Fitness-Exercise/400x400_Stretches_to_Do_at_Work_Every_Day_Hamstring_Stretch.gif' +
              '\nRemain seated, extend one leg outward\n Reach for your toes' +
              '\nHold for 10-30 seconds\nRepeat on the other side']
              


##global startKeyboard
##startKeyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard = [
##    [KeyboardButton(text='/start')]])

global dietKeyboard
dietKeyboard = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='Food of the day\U0001F957', callback_data='food')],
    [InlineKeyboardButton(text='Random tips\u2753', callback_data='tips')]])

global exerciseKeyboard
exerciseKeyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard = [
    [KeyboardButton(text='Beginner')],
    [KeyboardButton(text='Intermediate')],
    [KeyboardButton(text='Expert')],
    [KeyboardButton(text='/reset')]])

global beginnerWeeks
beginnerWeeks = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='Week 1', callback_data='beginnerweek1')],
    [InlineKeyboardButton(text='Week 2', callback_data='beginnerweek2')],
    [InlineKeyboardButton(text='Week 3', callback_data='beginnerweek3')]])

global intermediateWeeks
intermediateWeeks = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='Week 1-2', callback_data='intermediateweek1-2')],
    [InlineKeyboardButton(text='Week 3-4', callback_data='intermediateweek3-4')],
    [InlineKeyboardButton(text='Week 5-6', callback_data='intermediateweek5-6')]])

global expertWeeks
expertWeeks = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='Week 1-2', callback_data='expertweek1-2')],
    [InlineKeyboardButton(text='Week 3-4', callback_data='expertweek3-4')],
    [InlineKeyboardButton(text='Week 5-6', callback_data='expertweek5-6')]])

global stretchKeyboard
stretchKeyboard = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='Neck, shoulders', callback_data='neck')],
    [InlineKeyboardButton(text='Torso', callback_data='torso')],
    [InlineKeyboardButton(text='Legs', callback_data='legs')]])

global helpKeyboard
helpKeyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard = [
    [KeyboardButton(text='Push ups'), KeyboardButton(text='Sit ups')],
    [KeyboardButton(text='Squats'), KeyboardButton(text='Pull ups')],
    [KeyboardButton(text='Dips'), KeyboardButton(text='/reset')]])

global catKeyboard
catKeyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard = [
        [KeyboardButton(text='Diet'), KeyboardButton(text='Exercises')],
        [KeyboardButton(text='Stretches'), KeyboardButton(text='Help')],
        [KeyboardButton(text='You'), KeyboardButton(text='Endless')],
        [KeyboardButton(text='Bmi'), KeyboardButton(text='/reset')]])

global keywords
keywords = ['Diet', 'Exercises', 'Stretches', 'Help', 'You', 'Endless', 'Bmi']


class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(include_callback_query=True, *args, **kwargs)

        self.count           = 0
        self.level           = 0
        self.start           = 0
        self.help            = 0
        self.counter         = 0
        self.bmi             = 0
        self.name            = ""
        self.exercise        = ""
        self.difficulty      = ""
        self.category        = ""
        self.endless         = 0
        self.pushups         = 0
        self.situps          = 0
        self.planks          = 0
        self.burpees         = 0


    def on_chat_message(self, msg):
        
        content_type, chat_type, chat_id = telepot.glance(msg)
        response = bot.getUpdates()
        print(response)

        if ('/reset' in msg['text']):
            self.count = 1
            self.help = 0
            self.endless = 0
            self.level = 0
            self.bmi = 0
            self.weight = 0
            self.height = 0

        if (self.count) == 0:
            if ('/tap' in msg['text']):
                self.count += 1
            else:
                self.sender.sendMessage('/tap here to begin our Healthbot\uE404\n/reset everytime you want to change category!')

        if (self.count) == 1:
            self.count += 1
            self.sender.sendMessage('Welcome to our Healthbot!\U0001F917\n' +
                                    'You can use the custom keyboard to input the categories!\u2328', reply_markup=catKeyboard)
            
        elif (self.count) == 2:
            self.category=msg['text']
            if self.category not in keywords:
                self.count-=1

            else:
                self.count = 3
                self.start = 1
                self.sender.sendMessage("Category: " + self.category)
                self.sender.sendMessage('Type anything to continue')
                x = msg['text']

        elif (self.count == 3 and self.start == 1):
            if (self.category == "Diet"):
                self.sender.sendMessage('Hi', reply_markup=dietKeyboard)

            elif (self.category == "Exercises"):
                self.sender.sendMessage('Hi', reply_markup=exerciseKeyboard)
                self.difficulty = msg['text']

                if (self.difficulty == 'Beginner'):
                    self.sender.sendMessage('Change difficulty using the custom keyboard', reply_markup=beginnerWeeks)

                elif (self.difficulty == 'Intermediate'):
                    self.sender.sendMessage('Change difficulty using the custom keyboard', reply_markup=intermediateWeeks)

                elif (self.difficulty == 'Expert'):
                    self.sender.sendMessage('Change difficulty using the custom keyboard', reply_markup=expertWeeks)

            elif (self.category == "Stretches"):
                self.sender.sendMessage('HI', reply_markup=stretchKeyboard)

            elif (self.category == "Help"):
                self.count = 4
                self.help += 1
                self.sender.sendMessage('Which exercises do you need help in?', reply_markup=helpKeyboard)

            elif (self.category == "You"):
                self.sender.sendMessage('Oh you naughty naughty ;)', reply_markup=catKeyboard)

            elif (self.category == 'Endless'):
                self.count = 5
                self.endless += 1
                self.sender.sendMessage('Type a number in to indicate your level')

            elif (self.category == 'Bmi'):
                self.count = 6
                self.bmi += 1
                self.sender.sendMessage('Please enter your height(m) then weight(kg) in this format.\n' +
                                        'E.g, 1.75, 65.0\n' +
                                        'Please include the comma(,) and spacing.')


        elif (self.count == 4 and self.help == 1):
            if ('Push ups' in msg['text']):
                self.sender.sendMessage('Start with hands on the ground, shoulder width apart\n' +
                                        'Extend your legs straight with ball of feet on the ground\n' +
                                        'Keep your body straight, core tight and glutes squeezed, head in neutral position\n' +
                                        'Lower body until chest touches ground, Push back up to starting position', reply_markup=helpKeyboard)
            elif ('Sit ups' in msg['text']):
                self.sender.sendMessage('Lie down on your back, knees bent, feet flat on the ground\n' +
                                        'Hands cupped around your ears and tighten your core\n' +
                                        'Bring your body up till your elbow or chest touches the knees\n' +
                                        'Slowly lower your body back to starting position\n', reply_markup=helpKeyboard)

            elif ('Squats' in msg['text']):
                self.sender.sendMessage('Stand with feet shoulder width apart\n' +
                                        'Keep core tightened, Push your butt and hips out\n' +
                                        'Keep your back straight, weight on heels\n' +
                                        'Keep your knees behind your toes\n' +
                                        'Lower yourself down as if sitting on a chair until your thighs are parallel to the ground\n' +
                                        'Straighten your legs and squeeze your glutes while going up', reply_markup=helpKeyboard)

            elif ('Pull ups' in msg['text']):
                self.sender.sendMessage('Start with a dead hang, grip the bar slightly wider than shoulder width\n' +
                                        'Pull yourself up, chest up and pull shoulder blades back and downards\n' +
                                        'Lift till chin is above the bar\n' +
                                        'Slowly lower yourself down to starting position\n' +
                                        'If you are unable to do a proper pull up, start with a jumping pull up', reply_markup=helpKeyboard)

            elif ('Dips' in msg['text']):
                self.sender.sendMessage('Balance on the dip bars, hand under shoulders and elbows locked\n' +
                                        'Keep head in line with torso, lean your torso slightly forward\n' +
                                        'Bend your arms, lower till shoulders are below elbow\n' +
                                        'Rise to starting position and repeat\n'+
                                        'If your are unable to do a proper dip\n' +
                                        'You can lower yourself slightly instead of having your shoulders below the elbow', reply_markup=helpKeyboard)

        elif (self.count == 5 and self.endless == 1):
            x = msg['text']
            while self.endless != 2:
                try:
                    if int(x) <= 0:
                        self.sender.sendMessage('Please input a positive number')
                        return

                    elif 0 < int(x):
                        self.level = int(x)
                        self.endless = 2
                        self.sender.sendMessage('Sending workout')

                except ValueError:
                    break

                if (self.level > 0):
                    self.pushups = 30 + (self.level * 2)
                    self.situps = 40 + (self.level *(1.5))
                    self.plank = 20 + (self.level * 3)
                    self.burpees = 10 + (self.level *2.5)
                    self.endless = 3
                    self.count = 5

                    if (self.count == 5 and self.endless == 3):
                        self.count = 0
                        self.endless = 0
                        self.sender.sendMessage('Do this\n' +
                                                '1. ' + str(self.pushups) + ' push ups\n' +
                                                '2. ' + str(self.situps) + ' sit ups\n' +
                                                '3. ' + str(self.plank) + 'seconds planks\n' +
                                                '4. ' + str(self.burpees) + ' burpees\n')
                        self.sender.sendMessage('Here\'s a /reset button')
                        return

        elif (self.count == 6 and self.bmi == 1):
            h = msg['text']
            height = h[0:3]
            weight = h[6:9]
            while self.bmi != 2:
                try:
                    if float(height) < 0:
                        self.sender.sendMessage('Please input a positive number')
                        return
                    
                    elif 0 < float(height):
                        self.height = float(height)
                        self.weight = float(weight)
                        self.bmi = 2
                except ValueError:
                    break

            if self.bmi == 2:
                BMI = self.weight / (self.height ** 2)
                BMI = "{0:.2f}".format(BMI)
                if 18.5 <= float(BMI) <= 24.9:
                    sentence = ('Good Job! You are in the healthy range, keep up the good work!')
                elif float(BMI) < 18.5:
                    sentence = ('Your BMI is a bit too low, that isn\'t very healthy\n' +
                                'You need to get some gains, or have a healthier diet\n' +
                                'Visit our diet and exercise category to begin your fitness journey')
                elif 30.0 > float(BMI) > 24.9:
                    sentence = ('Your BMI is a bit too high, You need to improve your diet choices\n' +
                                'Get started, visit our diet and exercise category to shed some weight')
                elif float(BMI) >= 30.0:
                    sentence = ('Your BMI is very high! It is crucial to follow a healthy diet and exercise plan\n' +
                                'Visit our diet and exercise category to get started.')
    
                self.sender.sendMessage('Your BMI is ' + str(BMI) + '\n' +
                                        str(sentence))
                self.sender.sendMessage('Here\'s a /reset button')
                    



    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        
        response1 = bot.getUpdates()
        print(response1)


        if query_data == 'food':
            
            bot.answerCallbackQuery(query_id, text='Please hold while we fetch the relevant details')
            y = random.randint(0, len(urls)-1)
            bot.sendMessage(from_id, text=urls[y], reply_markup=dietKeyboard)
            
        elif query_data == 'tips':
            
            y = random.randint(0, len(tips)-1)
            bot.answerCallbackQuery(query_id, text=tips[y])

        elif query_data == 'beginnerweek1':
            bot.sendMessage(from_id, 'Do the following exercises:\n' +
                            'Push ups    10\n' +
                            'Squats      10\n' +
                            'Sit ups     10\n' +
                            'Do 3 sets, rest 1min between each set', reply_markup=None)
            
        elif query_data == 'beginnerweek2':
            bot.sendMessage(from_id, 'Do the following exercises:\n' +
                            'Push ups      15\n' +
                            'Squats        15\n' +
                            'Situps        15\n' +
                            'Jumping Jacks 20\n' +
                            'Do 4 sets, rest 1min between each set', reply_markup=None)
            
        elif query_data == 'beginnerweek3':
            bot.sendMessage(from_id, 'Do the following exercises:\n' +
                            'Push ups      15\n' +
                            'Squats        15\n' +
                            'Sit ups       15\n' +
                            'Jumping jacks 30\n' +
                            'Do 5 sets, rest 1min between each set', reply_markup=None)

        elif query_data == 'intermediateweek1-2':
            bot.sendMessage(from_id, 'Do the following exercises:\n' +
                            'Squats     30\n' +
                            'Sit ups    30\n' +
                            'Push ups   30\n' +
                            'Pull ups    5\n' +
                            'Dips        5\n' +
                            'Do 3 sets, rest 1min between each set', reply_markup=None)
            
        elif query_data == 'intermediateweek3-4':
            bot.sendMessage(from_id, 'Do the following exercises:\n' +
                            'Squats     30\n' +
                            'Sit ups    30\n' +
                            'Push ups   30\n' +
                            'Pull ups    5\n' +
                            'Dips        5\n' +
                            'Do 5 sets, rest 1min between each set', reply_markup=None)
            
        elif query_data == 'intermediateweek5-6':
            bot.sendMessage(from_id, 'Do the following exercises:\n' +
                            'Squats     35\n' +
                            'Sit ups    35\n' +
                            'Push ups   35\n' +
                            'Pull ups   10\n' +
                            'Dips       10\n' +
                            'Do 5 sets, rest 1min between each set', reply_markup=None)

        elif query_data == 'expertweek1-2':
            bot.sendMessage(from_id, 'Do the following exercises:\n' +
                            'Push ups   30\n' +
                            'Sit ups    35\n' +
                            'Pull ups   10\n' +
                            'Dips       10\n' +
                            'Burpees    10\n' +
                            'Do 5 sets, rest 1min between each set', reply_markup=None)

        elif query_data == 'expertweek3-4':
            bot.sendMessage(from_id, 'Do the following exercises:\n' +
                            'Push ups   40\n' +
                            'Sit ups    40\n' +
                            'Pull ups   10\n' +
                            'Dips       10\n' +
                            'Burpees    10\n' +
                            'Do 5 sets, rest 1min between each set', reply_markup=None)

        elif query_data == 'expertweek3-4':
            bot.sendMessage(from_id, 'Do the following exercises:\n' +
                            'Push ups   40\n' +
                            'Sit ups    40\n' +
                            'Pull ups   10\n' +
                            'Dips       10\n' +
                            'Burpees    10\n' +
                            'Do 7 sets, rest 1min between each set', reply_markup=None)

        elif query_data == 'expertweek5-6':
            bot.sendMessage(from_id, 'Do the following exercises:\n' +
                            'Push ups   50\n' +
                            'Sit ups    50\n' +
                            'Pull ups   12\n' +
                            'Dips       12\n' +
                            'Burpees    15\n' +
                            'Do 7 sets, rest 1min between each set', reply_markup=None)

        elif query_data == 'neck':
            y = random.randint(0, len(headStretch)-1)
            bot.sendMessage(from_id, text=headStretch[y], reply_markup=stretchKeyboard)
            bot.sendMessage(from_id, text='Here\'s a /reset button')

        elif query_data == 'torso':
            y = random.randint(0, len(torsoStretch)-1)
            bot.sendMessage(from_id, text=torsoStretch[y], reply_markup=stretchKeyboard)
            bot.sendMessage(from_id, text='Here\'s a /reset button')

        elif query_data == 'legs':
            y = random.randint(0, len(legStretch)-1)
            bot.sendMessage(from_id, text=legStretch[y], reply_markup=stretchKeyboard)
            bot.sendMessage(from_id, text='Here\'s a /reset button')



TOKEN = '444858592:AAGjqJtL9FwiUdXfvUWqd2WLcZeWajEqC7I'
##Keeps the bot running
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageCounter, timeout = 5000),
])
bot.message_loop(run_forever='Listening...')

affirmations = ['yes', 'si', 'yeah', 'yep', 'yup', 'sure', 'ok', 'okay', 'affirmative', 'aye aye', 'aye', 'roger', 'roger that', 'righto', 'right', 'indeed', 'yep', 'yup', 'yarp', 'yarp yarp', 'yarp yarp yarp']

# list of greetings
greetings = ['hello', 'good morning', 'good afternoon', 'good evening', 'hi!', 'hi', 'hallo', 'hola']

# list of questions
questions = ['what', 'where', 'how', 'when', 'who']

def response(input_message):
    message = input_message.lower()


    if message == 'nice':
        return 'Nice to meet you too!'
    elif message == 'bye':
        return 'Bye! Have a nice day!'
    elif message == 'hola!!':
        return 'Hola! Como estas?'
    elif message in affirmations:
        return 'Great!'
    elif message in greetings:
        return 'Hello! How are you?'
    elif message in questions:
        return 'I am a bot. I do not know the answer to that question.'
    else:
        return 'I am sorry, I do not understand you.'
    
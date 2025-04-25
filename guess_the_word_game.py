import random
import time

import speech_recognition as sr

def recognize_speech_from_mic(recognizer,microphone):
    """
        Transcribe speech from recorded from microphone.
        Returns a dictionary with three keys:
        "success": a boolean indicating whether or not API was sucessful.
        "error": 'None' if no error occured , otherwise a string containing a error message if the API could not be reached or speech was unrecognizable.
        "transcription" : 'None' if speech could not be transcribed, otherwise a string containing the transcribed text.
    """

    # check that recognizer and microphone arguments are appropriate type.

    if not isinstance(recognizer,sr.Recognizer):
        raise TypeError("'recognizer' must be 'Recognizer' Instance.")
    
    if not isinstance(microphone,sr.Microphone):
        raise TypeError("'microphone' must be 'Microphone' instance.")
    
    with microphone as source:
        print("Adjusting For Surrounding Noise....")
        recognizer.adjust_for_ambient_noise(source,5)
        print("World is listening...")
        audio = recognizer.listen(source)


    # Response
    response = {
        "success":True,
        "error":None,
        "transcription":None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)

    except sr.RequestError:
        response["success"] = False,
        response["error"] = "API Unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech.."

    return response


if __name__ == "__main__":
    fruits = ["apple","banana","grape","orange","mango","lemon"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    # create the recognizer and microphone Instances.
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()


    #  random word from the list...
    word = random.choice(fruits)

    #  format the instructions string
    instructions = (
        "I'm thinking of one of these words: \n"
        "{words}\n"
        "You have {n} tries to guess which one...\n"
    ).format(words=', '.join(fruits),n=NUM_GUESSES)


    # show instructions and wait for three seconds.
    print(instructions)
    time.sleep(3)

    for i in range(NUM_GUESSES):
        for j in range(PROMPT_LIMIT):
            print('Guess {}. Speak!'.format(i+1))
            guess = recognize_speech_from_mic(recognizer,microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")


        # if their was an error, stop the game
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        # Showing the Transcription
        print("You Said: {}".format(guess["error"]))


        # check the game logic and if user guess is correct.
        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        if guess_is_correct:
            print("Correct! User has won the Game...".format(word))
            break
        elif user_has_more_attempts:
            print("Incorrect Try Again!")
        else:
            print("Sorry, you lose!\nThe correct word was'{}'".format(word))
            break
from datetime import date, datetime
import pyttsx3
import speech_recognition as sp

ear = sp.Recognizer()
mouth = pyttsx3.init()

while True:
	with sp.Microphone() as mic:
		print("Robot: I'm Listening")
		ear.adjust_for_ambient_noise(mic, duration=0.1)
		audio = ear.listen(mic)

	print("...Processing audio...")

	try:
		you = ear.recognize_google(audio)
	except:
		you = ""

	print("You: " + you)

	if "hello" in you or "hi" in you:
		robot = "hello"
	elif "your" in you and "name" in you:
		robot = "My name is robot"
	elif "how" in you and "you" in you:
		robot = "I'm good. And you?"
	elif "date" in you and "today" in you:
		robot = date.today().strftime("%B %d, %Y")
	elif "time" in you:
		robot = datetime.now().strftime("%H hours %M minutes")
	elif "bye" in you or "goodbye" in you:
		print("Robot: Bye")
		mouth.say("Bye")
		mouth.runAndWait()
		break
	else:
		robot = "I don't understand. Please try again"

	print("Robot: " + robot)
	mouth.say(robot)
	mouth.runAndWait()
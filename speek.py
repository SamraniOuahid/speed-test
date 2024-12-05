import pyttsx3
import wikipedia

engine = pyttsx3.init()  # Initialize the engine


#name
name = input("whats your name: ")
engine.say(f"Hello {name}")
engine.runAndWait()
#age
age = input("enter your age: ")
engine.say(f"your age is {age}")
newAge = int(age)
engine.runAndWait()
#job
job = input("whats your job: ")
engine.say(f"your job is {job}")
engine.runAndWait()
newAge = newAge+1
engine.say(f"good by {name} your age in 2025 is {age} ")
engine.runAndWait()
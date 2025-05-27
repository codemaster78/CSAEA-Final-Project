import time
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

score = 0
finished = False

def question(question,correct,a,b,c):
    global score
    qs = [correct,a,b,c]
    print(question)
    
    q1 = random.choice(qs)
    qs.remove(q1)
    print(f'a: {q1}')
    
    q2 = random.choice(qs)
    qs.remove(q2)
    print(f'b: {q2}')
    
    q3 = random.choice(qs)
    qs.remove(q3)
    print(f'c: {q3}')
    
    q4 = random.choice(qs)
    qs.remove(q4)
    print(f'd: {q4}')
    
    ans = input("Enter your Answer: ")
    if ans == 'a' and q1 == correct:
        score += 1
        print("Correct!")
    elif ans == 'b' and q2 == correct:
        score += 1
        print("Correct!")
    elif ans == 'c' and q3 == correct:
        score += 1
        print("Correct!")
    elif ans =='d' and q4 == correct:
        score += 1
        print("Correct!")
    else:
        print("Incorrect")


question("If the gas pedal sticks, you should keep your eyes on the road and quickly: ","Shift to neutral and steer the vehicle off the roadway","None of the answers","Let the vehicle coast to a stop","Grip the wheel firmly and shift to a lower gear")
time.sleep(3)
cls()
question("After 2 to 4 drinks, alchahol begins to impair your:","All of the answers","Coordination and balance","Judgement","Reaction time")
time.sleep(3)
cls()
question("A driver's hand and arm pointing straight out indicates what directional signal:","Left turn","U-Turn","Stop","Right-Turn")
time.sleep(3)
cls()
question("In the event of a sudden stop or crash, the use of seat belts may:","Keep you from hitting the winsheild and being thrown from the car","Help you maintain control of the car","Keep you from driving safely","Keep you from adjusting the seat and shoulder strap")
time.sleep(3)
cls()
question("To avoid a spin while in a skid, you should:","Turn in the same direction the back of the vehicle is skidding","Tighten your grip on the steering wheel","Turn in the direction of the skid and lock your brakes","Turn in the opposite direction the back of the vehicle is skidding")
time.sleep(3)
cls()
question("The best way to reduce your chances of having a alcohol related accident is to:","Not to drive at all after drinking","Have a meal before you drink","Reduce your drinking","Know your limits")
time.sleep(3)
cls()
question("If your breaks suddenly give out, the thing you should try to do is: ","Shift to a lower gear and pump the breaks several times","Blow the horn and coast to a stop","Turn off the ignition","Drive onto the shoulder to reduce speed")
time.sleep(3)
cls()
question("Approaching an uncontrolled intersection you should:","Reduce speed and be ready to stop","Stop","Speed up","Slow down and look straight ahead")
time.sleep(3)
cls()
question("An acceleration lane is: ","An extra lane at the highway entrance","The passing lane","The left lane on a 2 lane highway","An extra lane at the highway entrance")
time.sleep(3)
cls()
question("High beam lights are used for: ","Open country driving with no traffic","Signaling emergencies","Foggy weather","City streets without lights")
time.sleep(3)
cls()
question("To avoid hydroplaning, you should: ","Slow down and drive on the highest point of the road","Increase your speed","Coast and slow down to a stop","Maintain 35 mph or above")
cls()
print(f'Congrats, you finished with a score of {score*10}%')

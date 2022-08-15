import random

list = """
    What do you think the best part of being a grown-up will be?
    Do you believe in magic?  Why or why not?
    What kinds of behaviors would be on exhibit in a people zoo?
    Find a photograph, and then write the story of what you think is really going on in the image.
    Would you rather be a famous movie star, a politician, or an athlete?  Why?
    Write a story about an adventurous field trip to the moon.
    If trees could talk, what sorts of things would they have to say?
    Do you believe in aliens?  Why or why not?
    Write a sequel to your favorite fairy tale.
    If today were opposite day, what things would you have done differently so far?
    Write a story about a character who stumbles on an important clue to an unsolved mystery.
    Imagine that you see a strange light in the sky.  What is it?
    What would you do if you suddenly found yourself able to communicate with animals?
    If you could rename our city and state, what would you call them?  Why?
    What color best represents your personality?  Why?
    What is the coolest gift someone could ever receive?  What makes it so amazing?
    Write a story about a mountain made of ice cream.
    Imagine your life is a video game.  How do you get bonus points?  What is your goal?
    If you were to set a world record, what would it be for? 
    Write a story about a big storm that no one saw coming.
    Go outside and watch the clouds.  Then, write about the shapes and things you saw.
    Write a fake news story about something real that happened this week.
    If you were President of the Universe for one day, what new rules would you make? 
    What technology would you most like to see invented in the future?  Why?
    Write a story about an unexpected visitor.
    Imaginative Journal Writing Ideas for Students
    Make a list of 10 crazy food combinations.  They can be as savory and sweet or as weird and gross as you’d like.  Then, write about one that you would be willing to try and what you think it would taste like.
    What would you wish for if you found a magic genie?
    What would you do if you woke up and could suddenly speak three new languages?
    If you got trapped in the mall overnight, what would you do there?  Describe all the fun hijinks you could have.
    Write a story about an apple tree that never stops growing.
    If you could be lost in a maze made of any item of your choosing, what would it be?  Why?
    Write a story about someone with a diabolical plan—that goes terribly, comically, awry.
"""

cut_list = list.split("\n")
print(cut_list[random.randint(1, len(cut_list))])
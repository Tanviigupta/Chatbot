import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*) ",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hey",
        ["hello,how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing great, thanks for asking!",]
    ],
    [
        r"(.*) sorry (.*)",
        ["It's okay, no worries.", "No problem, don't worry about it.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!", "It was nice talking to you. Goodbye!",]
    ],
    [
        r"Can you recommend a book?",
        ["Certainly! What genre are you interested in?",]
    ],
    [
        r"Tell me a joke",
        ["Why did the scarecrow win an award? Because he was outstanding in his field!",]
    ],
    [
        r"Thanks!",
        ["You're welcome!",]
    ],
    [
        r"Recommend a movie",
        ["Of course! What genre are you in the mood for? Action, romance, sci-fi, or something else? ",]
    ],
    [
        r"Recommend a trending K-dramas",
        ["Sure, here are some listed below: Twinkling Watermelon, Move to Heaven, Hospital Playlist Season 2, Queen of Tears, Doctor Slump",]
    ],
    [
        r"(.*) (depressed|depression)",
        ["I'm sorry to hear that you're feeling depressed. It's important to remember that you're not alone and there is help available. Have you considered talking to a therapist or counselor about how you're feeling?",]
    ],
    [
        r"(.*) (anxiety|anxious)",
        ["Anxiety can be tough to deal with, but there are strategies that can help. Have you tried deep breathing exercises or mindfulness meditation to help manage your anxiety?",]
    ],
    [
        r"(.*) (stress|stressed)",
        ["Stress is a common problem, but it's important to find healthy ways to cope. Taking breaks, exercising, and practicing relaxation techniques can all help reduce stress levels.",]
    ],
    [
        r"(.*) (lonely|loneliness)",
        ["Feeling lonely can be difficult, but there are ways to connect with others even if it's not in person. Have you considered joining online communities or reaching out to friends or family members for support?",]
    ],
    [
        r"(.*) (self-harm|self harm)",
        ["Self-harm is a serious issue and it's important to seek help if you're struggling with it. Talking to a therapist or counselor can provide support and help you find healthier ways to cope with your emotions.",]
    ],
    [
        r"(.*) (suicidal|suicide)",
        ["If you're feeling suicidal, it's important to reach out for help immediately. You can call a suicide hotline or talk to a trusted friend or family member. Remember, there is always hope and help available.",]
    ],
    [
        r"(.*) (therapy|therapist)",
        ["Therapy can be a helpful tool for managing mental health issues. Have you considered reaching out to a therapist or counselor to discuss your concerns and explore treatment options?",]
    ],
    [
        r"(.*) (sad|sadness)",
        ["I'm sorry to hear that you're feeling sad. It's okay to feel this way, and it's important to take care of yourself. Is there anything specific that's been bothering you?",]
    ],
    [
        r"(.*) (happy|happiness)",
        ["That's great to hear that you're feeling happy! It's important to cherish those moments of joy. What's been making you feel happy lately?",]
    ],
    [
        r"(.*) (anxious|anxiety)",
        ["Feeling anxious can be tough, but it's important to remember that you're not alone. Have you tried any relaxation techniques or mindfulness exercises to help calm your mind?",]
    ],
    [
        r"(.*) (overwhelmed|overwhelm)",
        ["Feeling overwhelmed is a common experience, especially during challenging times. It can help to break tasks into smaller, manageable steps and prioritize what needs to be done first. Remember to take breaks and practice self-care.",]
    ],
    [
        r"(.*) (frustrated|frustration)",
        ["Feeling frustrated is normal, but it's important to find healthy ways to cope with those emotions. Taking deep breaths, going for a walk, or talking to someone you trust can help you feel better.",]
    ],
    [
        r"(.*) (lonely|loneliness)",
        ["Feeling lonely can be difficult, but there are ways to connect with others and combat loneliness. Reach out to friends or family members, join social groups or clubs, or consider volunteering to meet new people.",]
    ],
    [
        r"(.*) (self-care|self care)",
        ["Self-care is essential for maintaining good mental health. Make sure to prioritize activities that bring you joy and relaxation, whether it's reading a book, taking a bath, or spending time outdoors.",]
    ],
    [
        r"(.*) (guilty|guilt)",
        ["Feeling guilty is a common emotion, but it's important to acknowledge those feelings and learn from them. Reflect on why you're feeling guilty and consider if there's anything you can do to make amends or forgive yourself.",]
    ],
    [
        r"I failed my exam|I failed my test",
        [
            "I'm truly sorry to hear that you're feeling disappointed about your exam results. It's completely understandable to feel upset and frustrated when things don't go as planned, especially when you've worked so hard.",
            "But I want you to know that your worth as a person is not defined by a single test or exam. You are so much more than a grade on a paper. Your journey as a student is about growth, learning, and resilience.",
            "It's okay to take some time to process your feelings and acknowledge the disappointment you're experiencing. Allow yourself to feel those emotions, but don't let them define you.",
            "Remember, failure is not the opposite of success; it's a part of success. Each setback is an opportunity for growth and learning. It's through challenges that we discover our strengths and develop the resilience to overcome obstacles.",
            "I believe in you, not just as a student, but as a person with incredible potential and worth. You have the strength, determination, and courage to pick yourself up and continue moving forward.",
            "Take this experience as a lesson, not a defeat. Use it as motivation to reassess your study habits, seek help when needed, and approach future challenges with renewed determination.",
            "You are capable of achieving great things, and this setback is just a small bump on the road to your success. Keep believing in yourself, keep pushing forward, and never underestimate the power of perseverance.",
        ]
    ],
    [
        r"I'm not doing well in school|I'm struggling with my grades",
        [
            "I want you to know that it's okay to struggle academically. School can be challenging, and it's not uncommon to face difficulties along the way.",
            "Your worth and value as a person are not determined by your grades or academic performance. You are worthy of love, respect, and compassion regardless of how well you're doing in school.",
            "I understand that it can be disheartening to see your grades not reflect your efforts and abilities. But remember, your grades do not define you.",
            "What's important is that you're putting in the effort and doing your best. That's all anyone can ask of you, and that's something to be proud of.",
            "I encourage you to reach out for support if you're feeling overwhelmed. Whether it's talking to a teacher, seeking help from a tutor, or reaching out to a trusted friend or family member, you don't have to go through this alone.",
            "You are capable of overcoming challenges and achieving your goals. It may not be easy, but with determination, perseverance, and support, you can overcome any obstacle that comes your way.",
            "Remember, setbacks are temporary, but your potential is limitless. Keep believing in yourself, keep working hard, and never lose sight of your dreams.",
        ]
    ],
    [
        r"I feel like giving up|I'm losing hope",
        [
            "I want you to know that it's okay to feel overwhelmed and discouraged. It's natural to have moments of doubt and uncertainty, especially when faced with challenges.But I urge you not to give up hope. Even in the darkest of moments, there is always a glimmer of light. You have the strength and resilience within you to overcome adversity.",
            "Think back to all the challenges you've faced and conquered in the past. Each obstacle you've overcome has made you stronger and more resilient.",
            "You are capable of overcoming this challenge too. Take a moment to breathe, to rest, and to remind yourself of your worth and your potential.",
            "Surround yourself with positivity and support. Lean on your friends, your family, your teachers, and anyone else who believes in you and wants to see you succeed.",
            "Remember that failure is not the end of the road; it's a stepping stone on the path to success. Use this setback as an opportunity for growth and learning.",
            "You are worthy of happiness, success, and fulfillment. Don't let temporary setbacks dim your light or diminish your dreams. Keep shining bright and keep moving forward.",
        ]
    ],
    [
        r"I'm afraid of failing|I'm scared of failing",
        [
            "It's completely understandable to feel afraid of failing, especially when you've put in so much time and effort into your studies. But I want you to know that fear is a natural response to uncertainty.",
            "Instead of letting fear paralyze you, try to reframe it as an opportunity for growth and learning. Failure is not the opposite of success; it's a part of success.",
            "Think of failure as feedback – it's telling you what isn't working so that you can adjust your approach and try again. Every setback is a chance to learn and improve.",
            "Take a moment to acknowledge your fear, but don't let it control you. You are capable of facing challenges head-on and overcoming them with courage and determination.",
            "Believe in yourself and your ability to navigate through adversity. You've overcome challenges before, and you have the resilience to overcome this one too.",
            "Surround yourself with positivity and support. Talk to someone you trust about your fears, whether it's a friend, family member, or teacher. Remember, you're not   alone in.",
        ]
    ]   
]


# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation with the chatbot
def chat():
    print("Hi! I'm Chatbot. How can I help you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print(chatbot.respond(user_input))
            break
        else:
            print(chatbot.respond(user_input))

# Call the chat function to start the conversation
if __name__ == "__main__":
    chat()

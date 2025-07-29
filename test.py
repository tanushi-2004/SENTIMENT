# test.py

# We are importing the function we just wrote in the other file
from nlp_processor import analyze_emotions

# Let's create a sample journal entry
sample_text = "I finished a huge project today and I feel so relieved and proud. It was stressful, but seeing it done is pure joy."

print(f"Analyzing text: '{sample_text}'")
print("-" * 30)

# Call the function and get the results
emotions = analyze_emotions(sample_text)

# Print the results neatly
if emotions:
    # Sort emotions by score in descending order
    sorted_emotions = sorted(emotions.items(), key=lambda item: item[1], reverse=True)
    print("Emotion Analysis Results:")
    for emotion, score in sorted_emotions[:7]: # Print the top 7
        print(f"- {emotion.capitalize()}: {score}")
else:
    print("No analysis performed.")
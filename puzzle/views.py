from django.shortcuts import render
from .form import PuzzleForm
import math, random

def puzzle_view(request):
    result = {}
    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            text = form.cleaned_data['text']

    
            if number % 2 == 0:
                result['number_result'] = f"The number {number} is even. Its square root is {math.sqrt(number):.2f}."
            else:
                result['number_result'] = f"The number {number} is odd. Its cube is {number ** 3}."

            
            binary = ' '.join(format(ord(char), '08b') for char in text)
            vowels = sum(char.lower() in 'aeiou' for char in text)
            result['binary'] = binary
            result['vowels'] = vowels

            
            secret = random.randint(1, 100)
            attempts = []
            for i in range(1, 6):
                guess = random.randint(1, 100)
                if guess == secret:
                    attempts.append(f"Attempt {i}: {guess} (Correct!)")
                    break
                elif guess < secret:
                    attempts.append(f"Attempt {i}: {guess} (Too low!)")
                else:
                    attempts.append(f"Attempt {i}: {guess} (Too high!)")
            else:
                attempts.append("You didn't find the treasure in 5 attempts.")

            result['treasure'] = f"The secret number is {secret}."
            result['attempts'] = attempts
            
            result['user_number']= number
            result['user_text'] = text
    else:
        form = PuzzleForm()
    return render(request, 'puzzle/index.html', {'form': form, 'result': result})

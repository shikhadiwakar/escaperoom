from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Level, Player

@login_required
def level_view(request, level_id):
    # Retrieve the level and player data from the database
    level = Level.objects.get(id=level_id)
    player = Player.objects.get(user=request.user)

    # Perform any necessary calculations or data manipulations

    # Create the context dictionary with the necessary data
    context = {
        'level': level,
        'player': player,
        # Other data to pass to the template
    }

    # Pass the context to the template for rendering
    return render(request, 'game/level.html', context)

@login_required
def puzzle_view(request, level_id, puzzle_id):
    # Retrieve the level and player data from the database
    level = Level.objects.get(id=level_id)
    player = Player.objects.get(user=request.user)

    # Retrieve the specific puzzle based on puzzle_id
    puzzle = level.puzzles.get(id=puzzle_id)

    # Perform any necessary calculations or data manipulations

    # Create the context dictionary with the necessary data
    context = {
        'level': level,
        'player': player,
        'puzzle': puzzle,
        # Other data to pass to the template
    }

    # Handle puzzle solving logic
    if request.method == 'POST':
        # Process the user's solution for the puzzle
        user_solution = request.POST.get('solution', '')
        if user_solution == puzzle.solution:
            # Puzzle solved successfully
            # Update player progress or other relevant data
            player.current_level = level.next_level
            player.save()
            return redirect('level_view', level_id=player.current_level.id)
        else:
            # Incorrect solution provided
            context['error'] = 'Incorrect solution. Try again.'

    # Pass the context to the template for rendering
    return render(request, 'game/puzzle.html', context)

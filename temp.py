import ui
import sound
import random

# Define the slot symbols
symbols = ['🍒', '🍋', '🍊', '🍉', '🍇', '🍓', '7️⃣']

def spin(sender, slot1, slot2, slot3, result_label):
    """Handle the spin button press."""
    # Randomly select a symbol for each slot
    slot1.text = random.choice(symbols)
    slot2.text = random.choice(symbols)
    slot3.text = random.choice(symbols)
    
    # Play a sound
    sound.play_effect('arcade:Coin_2')
    
    # Check for win
    if slot1.text == slot2.text == slot3.text:
        result_label.text = 'You win!'
        sound.play_effect('arcade:Powerup_2')
    else:
        result_label.text = 'Try again!'

def main():
    # Create a UI
    view = ui.View()
    view.name = 'Slot Machine'
    view.background_color = 'white'

    # Create slot labels
    slot1 = ui.Label(frame=(50, 100, 80, 80), font=('Helvetica', 50), alignment=ui.ALIGN_CENTER)
    slot2 = ui.Label(frame=(150, 100, 80, 80), font=('Helvetica', 50), alignment=ui.ALIGN_CENTER)
    slot3 = ui.Label(frame=(250, 100, 80, 80), font=('Helvetica', 50), alignment=ui.ALIGN_CENTER)

    # Create a spin button
    spin_button = ui.Button(title='Spin', frame=(130, 250, 120, 50))
    spin_button.background_color = 'lightblue'
    spin_button.tint_color = 'white'
    spin_button.corner_radius = 5
    # Partial function to pass additional arguments to the spin function
    spin_button.action = lambda sender: spin(sender, slot1, slot2, slot3, result_label)

    # Create a result label
    result_label = ui.Label(frame=(50, 350, 300, 40), font=('Helvetica', 24), alignment=ui.ALIGN_CENTER)

    # Add subviews to the main view
    view.add_subview(slot1)
    view.add_subview(slot2)
    view.add_subview(slot3)
    view.add_subview(spin_button)
    view.add_subview(result_label)

    # Present the view
    view.present('sheet')

if __name__ == '__main__':
    main()

import pandas as pd
import pygame
from pygame import mixer
import os

# Load the dataset
dataset_path = r"D:\3-2\Minor Project\Feel_Good_dataset.xlsx"
print("Dataset Path:", dataset_path)
if not os.path.exists(dataset_path):
    print("File not found!")
    exit()

data = pd.read_excel(dataset_path)

# Initialize pygame
pygame.init()
mixer.init()

# Function to play music
def play_music(song_path, start_pos=0.0):
    mixer.music.load(song_path)
    mixer.music.play(start=start_pos)

# Function to stop music
def stop_music():
    mixer.music.stop()

# Function to display song list
def display_song_list():
    print("Song List:")
    for index, row in data.iterrows():
        print(f"{index+1}. {row['Title of the song']} - {row['Movie/Album name']}")

# Function to play next song
def play_next_song(current_index):
    next_index = current_index + 1
    if next_index >= len(data):
        next_index = 0  # Loop back to the first song if reached the end of the list
    selected_song = data.iloc[next_index]
    song_path = selected_song['Link of song']
    play_music(song_path)
    print(f"Now playing next song: {selected_song['Title of the song']} - {selected_song['Movie/Album name']}")
    return next_index

# Function to play previous song
def play_previous_song(current_index):
    previous_index = current_index - 1
    if previous_index < 0:
        previous_index = len(data) - 1  # Loop back to the last song if reached the beginning of the list
    selected_song = data.iloc[previous_index]
    song_path = selected_song['Link of song']
    play_music(song_path)
    print(f"Now playing previous song: {selected_song['Title of the song']} - {selected_song['Movie/Album name']}")
    return previous_index

# Function to skip forward in the currently playing song
def skip_forward(song_path, skip_duration):
    # Get the current position of the music
    current_pos = mixer.music.get_pos() / 1000  # Convert milliseconds to seconds
    # Skip forward by the specified duration
    new_pos = current_pos + skip_duration
    mixer.music.stop()
    play_music(song_path, start_pos=new_pos)

# Function to skip backward in the currently playing song
def skip_backward(song_path, skip_duration):
    # Get the current position of the music
    current_pos = mixer.music.get_pos() / 1000  # Convert milliseconds to seconds
    # Skip backward by the specified duration
    new_pos = current_pos - skip_duration
    if new_pos < 0:
        new_pos = 0
    mixer.music.stop()
    play_music(song_path, start_pos=new_pos)

# Main function
def main():
    while True:
        display_song_list()
        choice = int(input("Enter the number of the song you want to play, or 0 to exit: "))

        if choice == 0:
            print("Exiting...")
            break

        if choice < 1 or choice > len(data):
            print("Invalid choice!")
            continue

        selected_song = data.iloc[choice - 1]
        song_path = selected_song['Link of song']

        if not os.path.exists(song_path):
            print("File not found!")
            continue

        print(f"Now playing: {selected_song['Title of the song']} - {selected_song['Movie/Album name']}")
        play_music(song_path)

        current_index = choice - 1

        while True:
            action_choice = input("Press 'n' for next song, 'p' for previous song, 'f' to choose a favorite song again, 's' to stop, "
                                  "'fwd' to skip forward, 'bwd' to skip backward: ")
            if action_choice.lower() == 'n':
                current_index = play_next_song(current_index)
            elif action_choice.lower() == 'p':
                current_index = play_previous_song(current_index)
            elif action_choice.lower() == 'f':
                break
            elif action_choice.lower() == 's':
                stop_music()
                print("Song stopped.")
                break
            elif action_choice.lower() == 'fwd':
                skip_duration = float(input("Enter the duration to skip forward (in seconds): "))
                skip_forward(song_path, skip_duration)
            elif action_choice.lower() == 'bwd':
                skip_duration = float(input("Enter the duration to skip backward (in seconds): "))
                skip_backward(song_path, skip_duration)

if __name__ == "__main__":
    main()

import pygame
import os


pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Музыкальный плеер")


MUSIC_FOLDER = "C:/Users/Daulet/Desktop/pp2/lab7/songplayer/songs"


music_files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
if not music_files:
    print("there is no files .mp3")
    exit()


current_track = 0

#for downloading and playing back a track
def play_music(track):
    track_path = os.path.join(MUSIC_FOLDER, music_files[track])
    print(f"Now playing: {music_files[track]}")
    pygame.mixer.music.load(track_path)
    pygame.mixer.music.play()

# Запускаем первый трек
play_music(current_track)

running = True
paused = False

print("\nуправление: SPACE - Play/Pause, S - Stop, N - Next, P - Previous")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play / Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                    print("music on pause")
                else:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("continue")

            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()
                print("music is stop")

            elif event.key == pygame.K_n:  # Next
                current_track = (current_track + 1) % len(music_files)
                play_music(current_track)

            elif event.key == pygame.K_p:  # Previous
                current_track = (current_track - 1) % len(music_files)
                play_music(current_track)

    pygame.display.flip()  

pygame.quit()

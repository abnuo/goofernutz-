import random
import cherrypy
import requests
from moviepy.editor import *
from pathlib import Path
import glob
import os
import string
from pypresence import Presence

pathy = os.getcwd()
penismaster = 'outputpath'
client_id = '758065753504088157'
RPC = Presence(client_id)
RPC.connect()
RPC.update(state="Idle")
def render(output,input,geedey,mirx,miry,reversie,sfxe,blinke,accel,sfxfun,clipspeed):
    def randomaudio():
        filename = glob.glob(input + "/*.mp3")
        sdofjsodfj = random.choice(filename)
        return sdofjsodfj
    aclips.append(AudioFileClip(randomaudio()))
    random.shuffle(aclips)
    def randomvideo():
        filename = glob.glob(input + "/*.mp4")
        return random.choice(filename)
    def randomtime():
        clipname = randomvideo()
        lend = random.uniform(.5, VideoFileClip(clipname).duration)
        mario = clipname
        return VideoFileClip(clipname).subclip(lend - .5, lend).fx(vfx.speedx, random.uniform(.54, 3)).resize(
            (250, 250))
    superpoop = randomtime()
    poopman = superpoop
    RPC.update(state="Rendering")
    for i in range(int(geedey)):
        print("Applying effect : PLAIN")
        superpoop = randomtime()
        geeder = random.uniform(0, superpoop.duration)
        poopman = superpoop.subclip(0, geeder)
        clips.append(poopman)
    for i in range(int(mirx)):
        superpoop = randomtime()
        print("Applying effect : MIRROR X")
        poopman = superpoop.fx(vfx.mirror_x, apply_to='mask')
        clips.append(poopman)
    for i in range(int(miry)):
        superpoop = randomtime()
        print("Applying effect : MIRROR Y")
        poopman = superpoop.fx(vfx.mirror_y, apply_to='mask')
        clips.append(poopman)
    for i in range(int(reversie)):
        superpoop = randomtime()
        print("Applying effect : REVERSI")
        poopman = superpoop.fx(vfx.time_mirror)
        clips.append(poopman)
    for i in range(int(sfxe)):
        superpoop = randomtime()
        print("Applying effect : SFX")
        poopman = superpoop.set_audio(AudioFileClip(randomaudio()).audio_loop(duration=superpoop.duration))
        clips.append(poopman)
    for i in range(int(blinke)):
        superpoop = randomtime()
        print("Applying effect : INVERT")
        poopman = superpoop.fx(vfx.invert_colors)
        clips.append(poopman)
    for i in range(int(blinke)):
        superpoop = randomtime()
        print("Applying effect : DE FART")
        defart = []
        poopman = superpoop.fx(vfx.time_mirror).fx(vfx.speedx, 2)
        superman = poopman.fx(vfx.time_mirror)
        for i in range(2):
            defart.append(poopman)
            defart.append(superman)
        duperman = concatenate_videoclips(defart, method='compose')
        clips.append(duperman)
    for i in range(2):
        clips.append(poopman)
    for i in range(int(sfxfun)):
        superpoop = randomtime()
        lolsoft = []
        cocksoft = superpoop.fx(vfx.time_mirror).fx(vfx.speedx, 4)
        for i in range(random.randint(1, 4)):
            lolsoft.append(cocksoft)
            lolsoft.append(cocksoft)
        pooperlol = concatenate_videoclips(lolsoft, method='compose')
        appendtime = pooperlol.set_audio(random.choice(aclips).audio_loop(duration=superpoop.duration))
        clips.append(appendtime)
    for i in range(len(clips)):
        print("Shuffling! ")
        random.shuffle(clips)
    bitch = concatenate_videoclips(clips, method='compose').fx(vfx.speedx, int(clipspeed))
    print(bitch.duration)
    # Replace this directory with where you want the rendered video to go + the temp mp3
    bitch.write_videofile(output + '/zzeph.mp4',
                          temp_audiofile=output + '/tempaudio.aac', remove_temp=True,
                          codec="libx264", audio_codec="aac")
    RPC.update(state="Idle")
while True:
    clips = []
    aclips = []
    render(pathy,penismaster,random.randint(1,3),random.randint(1,7),random.randint(1,3),random.randint(1,3),random.randint(1,3),random.randint(1,3),random.randint(1,3),random.randint(1,3),random.randint(2,4))
    username = "FartBot"
    superfilez = {
    'file1': ('file' + Path(pathy + "/zzeph.mp4").suffix, open(pathy + "/zzeph.mp4", 'rb')),
    }
    r = requests.post("https://canary.discordapp.com/api/webhooks/713004331246288948/65OZwJ7sho-LBHu5nTMB1dHkGjBfdAawQIjNOcBjoWKVdwQYW7rYOqtkO52flCIPJTA1", data={'username': username,'content': "watch video pls :pleading:",'tts': "false"},files=superfilez)
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
    memerdoge = get_random_string(6)
    os.rename(pathy + "/zzeph.mp4"+ memerdoge + ".mp4")





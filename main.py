from moviepy.editor import *
import random
import os
import PySimpleGUIWx as sg
import glob
clips = []
aclips = []
def render(output,input,geedey,mirx,miry,reversie,sfxe,blinke,accel,sfxfun):
    inputlog = open(os.getcwd() + "/log1.txt",'w').close()
    inputlog = open(os.getcwd() + "/log1.txt", 'a')
    outputlog = open(os.getcwd() + "/log2.txt", 'w').close()
    outputlog = open(os.getcwd() + "/log2.txt",'a')
    inputlog.write(input)
    outputlog.write(output)
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
    for i in range(int(geedey)):
        print("Applying effect : GEEDER")
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


    bitch = concatenate_videoclips(clips, method='compose')
    print(bitch.duration)
    # Replace this directory with where you want the rendered video to go + the temp mp3
    bitch.write_videofile(output + '/result.mp4',
                          temp_audiofile=output + '/tempaudio.aac', remove_temp=True,
                          codec="libx264", audio_codec="aac")

if os.path.exists(os.getcwd() + "/log1.txt"):
    mariol = open(os.getcwd() + "/log1.txt")
    bonerly = mariol.read()
else:
    bonerly = ''
if os.path.exists(os.getcwd() + "/log2.txt"):
    superpoope2 = open(os.getcwd() + "/log2.txt")
    bonerlye = superpoope2.read()
else:
    bonerlye = ''

sg.theme('DarkBrown3')
layout = [
    [
        sg.Text("goofernutz+", font = 'Courier 34')
    ],
    [
            sg.Text('Output Folder', font='Courier 24'),
            sg.Multiline(size=(8, 3),default_text=bonerly,key='output'),
            sg.FolderBrowse(),
            sg.Text('Input folder\n', font='Courier 24'),
            sg.Multiline(size=(8, 3),default_text=bonerlye, key='input'),
            sg.FolderBrowse()

],
    [
            sg.Spin([str(i) for i in range(0,11)],size=(3, 1), initial_value=0,key='geeder'), sg.Text('GEEDER'),
            sg.Spin([str(i) for i in range(0,11)],size=(3, 1), initial_value=0,key='mirx'), sg.Text('MIRROR X'),
            sg.Spin([str(i) for i in range(0,11)],size=(3, 1), initial_value=0,key='miry'), sg.Text('MIRROR Y'),
            sg.Spin([str(i) for i in range(0,11)],size=(3, 1), initial_value=0,key='reversi'), sg.Text('REVERSI'),
            sg.Spin([str(i) for i in range(0,11)],size=(3, 1), initial_value=0,key='sfx'), sg.Text('SFX'),
            sg.Spin([str(i) for i in range(0,11)],size=(3, 1), initial_value=0,key='blink'), sg.Text('INVERT')
    ],
[
            sg.Spin([str(i) for i in range(0,11)],size=(3, 1), initial_value=0,key='accel'), sg.Text('DE FART'),
            sg.Spin([str(i) for i in range(0,11)],size=(3, 1), initial_value=0,key='sfxfun'), sg.Text('FUNNYSFX'),


            ],
[
sg.Button('Render')
],
[
sg.Output(size=(40,10), key='-OUTPUT-')
]
    ]

window = sg.Window('Goofernutz+', layout)
while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
        break
    if event == "Render":
        render(values['output'],values['input'],values['geeder'],values['mirx'],values['miry'],values['reversi'],values['sfx'],values['blink'],values['accel'],values['sfxfun'])



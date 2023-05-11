def konversi_audio():
    inputPath = easygui.fileopenbox(title='Select video file')
    outputPath = easygui.filesavebox(title='Save file to..')
    video = mp3.VideoFileClip(inputPath)
    audio = video.audio
    audio.write_audiofile(outputPath)
from lightning_whisper_mlx import LightningWhisperMLX

whisper = LightningWhisperMLX(model="tiny", batch_size=12, quant=None)

text = whisper.transcribe(audio_path="./cut.mp3")['text']

print(text)
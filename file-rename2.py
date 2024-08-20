import os
import shutil
import pandas as pd

excel_path = r"C:\Users\..."
clips_dir = r"C:\Users\..."
new_clips_dir = r"C:\Users\..."
os.makedirs(new_clips_dir, exist_ok=True)

df = pd.read_excel(excel_path, sheet_name='Sheet1')

print(df.columns)

clip_names = df['Clip Name'].tolist()
emotion_codes = df['Emotion Code'].tolist()

emotion_code_mapping = {
    1: 'angry',
    2: 'bored',
    3: 'bothered',
    4: 'concentrated',
    5: 'contempted',
    6: 'disgust',
    7: 'fearful',
    8: 'happy',
    9: 'neutral',
    10: 'sad',
    11: 'surprised',
    12: 'thoughtful',
    13: 'unsure'
}

for clip_name, emotion_code in zip(clip_names, emotion_codes):
    if not clip_name.lower().endswith('.wav'):
        clip_name = clip_name + '.wav'

    old_clip_path = os.path.join(clips_dir, clip_name)

    if os.path.exists(old_clip_path):
        if emotion_code in emotion_code_mapping:
            emo_name = emotion_code_mapping[emotion_code]
            new_clip_name = f"{os.path.splitext(clip_name)[0]}_{emo_name}{os.path.splitext(clip_name)[1]}"
            new_clip_path = os.path.join(new_clips_dir, new_clip_name)
            shutil.copyfile(old_clip_path, new_clip_path)
            print(f"'{clip_name}' dosyası '{new_clip_name}' olarak kopyalandı.")
        else:
            print(f"'{emotion_code}' kodu için EMO adı bulunamadı.")
    else:
        print(f"'{old_clip_path}' yolu ile dosya bulunamadı.")

print("Klipler başarıyla yeniden adlandırıldı ve yeni dizine kopyalandı.")

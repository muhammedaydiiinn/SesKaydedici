import sounddevice as sd
from scipy.io.wavfile import write


def ses_kaydet(time, doc_name):
    # Ses kaydı yapmak için gerekli ayarlar
    example_speed = 44100  # Örnek hızı (örneğin, 44.1 kHz)
    channel_num = 2  # Kanal sayısı (1 mono, 2 stereo)

    # Ses kaydını başlatma
    kayit = sd.rec(int(time * example_speed), samplerate=example_speed, channels=channel_num)

    print("Ses kaydediliyor...")
    sd.wait()  # Ses kaydının tamamlanmasını bekleyin

    # Ses kaydını WAV dosyası olarak kaydetme
    write(doc_name, example_speed, kayit)

    print(f"Ses kaydedildi: {doc_name}")


# Kullanıcıdan kayıt süresini ve dosya adını alın
kayit_suresi = float(input("Kayıt süresini saniye cinsinden girin: "))
dosya_adi = input("Dosya adını girin (örneğin: kayit.wav): ")

# Ses kaydetme işlemini gerçekleştirin
ses_kaydet(kayit_suresi, dosya_adi)

#gite ekledim

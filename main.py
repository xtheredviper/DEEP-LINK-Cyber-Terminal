import whisper
from gtts import gTTS
import os
import random
import platform

def get_local_audio():
    print("\n--- [SYSTEM]: Local Audio Sync Activated ---")
    filename = input("Enter the path to your audio file (or drag it here): ").strip().replace("'", "").replace('"', "")
    return filename

def generate_cyber_response(user_text):
    responses = [
        "Mainframe status: UNSTABLE. Corporate ICE is scanning our position, Choomba. Get out now!",
        "System check complete. 40% of your chrome is glitching, but the Eddies are safe. For now.",
        "You're asking about the mainframe? I'm busy rerouting power to the black market servers. Try later, Netrunner.",
        "Signal decrypted. Status is: FUBAR. Someone leaked your IP to Arasaka. Good luck, Choomba.",
        "Mainframe is humming, but your brain-deck is overheating. Maybe lay off the cyberware for a bit?"
    ]
    return random.choice(responses)

def run_cyber_system():
    print("\n--- [STATUS]: Initializing Whisper Protocol ---")
    model = whisper.load_model("base")
    
    audio_path = get_local_audio()
    
    if not os.path.exists(audio_path):
        print("--- [ERROR]: File not found in the mainframe! ---")
        return

    print("--- [STATUS]: Decrypting audio signal ---")
    result = model.transcribe(audio_path)
    user_text = result["text"]
    print(f"USER SAYS: {user_text}")
    
    print("--- [STATUS]: Accessing encrypted database ---")
    ai_response = generate_cyber_response(user_text)
    print(f"DEEP-LINK: {ai_response}")
    
    tts = gTTS(text=ai_response, lang='en')
    tts.save("response.mp3")
    
    print("\n--- [STATUS]: Audio output ready: response.mp3 ---")
    
    if platform.system() == "Windows":
        os.startfile("response.mp3")

if __name__ == "__main__":
    run_cyber_system()
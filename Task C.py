import asyncio

async def filler_tts():
    print("TTS → Let me look that up for you...")
    await asyncio.sleep(0.1)


def voice_post_process(text):

    replacements = {
        "PWR_CONN_1": "power connector one",
        "planar board": "main board"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    chunks = text.replace(".", ".\n").split("\n")

    return chunks

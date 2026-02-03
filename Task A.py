import asyncio

async def streaming_asr(audio_stream):
    partials = [
        "my dell server shows error",
        "my dell server shows error e121",
        "my dell server shows error e121 and what about the second one"
    ]

    for p in partials:
        await asyncio.sleep(0.2)
        yield p


async def rewrite_query(partial, history):
    if "second one" in partial.lower():
        return "Explain Dell PowerEdge R740 error E122"
    return partial

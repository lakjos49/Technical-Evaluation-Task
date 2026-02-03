import asyncio

from asr_and_rewrite import streaming_asr, rewrite_query
from retrieval import hybrid_retrieve, cross_encoder_rerank
from voice_layer import filler_tts, voice_post_process


async def voice_rag_pipeline(audio):

    history = []

    retrieval_task = None

    async for partial in streaming_asr(audio):

        rewritten = await rewrite_query(partial, history)

        retrieval_task = asyncio.create_task(
            hybrid_retrieve(rewritten)
        )

    docs = await retrieval_task

    asyncio.create_task(filler_tts())

    reranked = await cross_encoder_rerank(docs)

    llm_answer = """
    Disconnect PWR_CONN_1 from the planar board.
    Then reboot the system.
    """

    spoken_chunks = voice_post_process(llm_answer)

    for c in spoken_chunks:
        print("TTS →", c.strip())


asyncio.run(voice_rag_pipeline("fake_audio"))

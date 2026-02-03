import asyncio

async def vector_search(q):
    await asyncio.sleep(0.05)
    return ["vec_doc1", "vec_doc2"]


async def bm25_search(q):
    await asyncio.sleep(0.05)
    return ["bm25_doc1", "vec_doc2"]


async def hybrid_retrieve(q):
    vec_task = asyncio.create_task(vector_search(q))
    bm25_task = asyncio.create_task(bm25_search(q))

    vec, bm25 = await asyncio.gather(vec_task, bm25_task)

    return list(set(vec + bm25))


async def cross_encoder_rerank(docs):
    await asyncio.sleep(0.2)
    return docs[:2]

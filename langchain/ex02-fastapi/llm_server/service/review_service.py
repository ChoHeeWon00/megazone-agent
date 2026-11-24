from planner.review_planner import review_chain

async def review( req:str ):
    return await review_chain.ainvoke( {"text":req} )

from agents.summary_agent import summary_chain
async def summary_stream( req : str):
    async for chunk in summary_chain.astream({"text":req}):
        yield chunk
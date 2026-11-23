#planner - review_planner.py

from langchain_core.runnables import RunnableParallel
from agents.sentiment_agent import sentiment_chain

review_chain = RunnableParallel(
    sentiment = sentiment_chain,
)
#review_chain.invoke()
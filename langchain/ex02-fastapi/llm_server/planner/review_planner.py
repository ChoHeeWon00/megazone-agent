#planner - review_planner.py

from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from agents.sentiment_agent import sentiment_chain
from agents.summary_agent import summary_chain
from agents.keyword_agent import keyword_chain

from operator import itemgetter


review_chain = RunnableParallel(
    sentiment = sentiment_chain ,
    summary = summary_chain,
    keyword = keyword_chain,
    original = itemgetter("text") #RunnablePassthrough(),
)

#review_chain.invoke()
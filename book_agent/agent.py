from .qdrant import bestseller_vdb_client
from google.adk.agents import Agent

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import FieldCondition
from qdrant_client.models import Filter
from qdrant_client.models import MatchValue

def get_best_sellers(query: str, must: dict, must_not: dict):
    """
    추천 도서 목록을 반환합니다.
    
    Args:
        query (str): 검색 쿼리 문자열.
        must (dict): 반드시 포함되어야 하는 조건들. (키-값 쌍)
                     키에는 다음과 같은 것들을 사용할 수 있다.
                        - "author": 저자 이름
                        - "category": 도서 카테고리 예: "자기계발", "시, 에세이", "경제/경영", "소설", "인문", "외국어"
        must_not (dict): 포함되지 않아야 하는 조건들. (키-값 쌍)
                     키에는 다음과 같은 것들을 사용할 수 있다.
                        - "author": 저자 이름
                        - "category": 도서 카테고리 예: "자기계발", "시, 에세이", "경제/경영", "소설", "인문", "외국어"
    """
    qdrant_must = [FieldCondition(key=key, match=MatchValue(value=value)) for key, value in (must or {}).items()]
    qdrant_must_not = [FieldCondition(key=key, match=MatchValue(value=value)) for key, value in (must_not or {}).items()]
    query_filter = Filter(must=qdrant_must, must_not=qdrant_must_not)
    query_vector = model.encode(query).tolist()
    
    search_result = bestseller_vdb_client.query_points(
        collection_name="best_sellers",
        query=query_vector,
        query_filter=query_filter,
        limit=5,
    )
    return [found_book.payload for found_book in search_result.points]

root_agent = Agent(
    name="book_agent",
    model="gemini-2.5-flash",
    instruction="사용자의 베스트셀러에 관한 질문에 답하세요. 'get_best_sellers' 도구를 사용하여 관련 책을 검색할 수 있습니다. 이때 사용자가 특정 조건을 걸었다면 'must' 및 'must_not' 매개변수를 dict 형태로 전달하여 검색결과를 필터링할 수 있습니다.",
    tools=[get_best_sellers],
)

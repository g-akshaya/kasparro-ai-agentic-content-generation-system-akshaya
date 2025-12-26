from typing import TypedDict, Dict, List, Any

class ContentState(TypedDict, total=False):
    raw_input: str
    product_data: Dict[str, Any]
    questions: Dict[str, List[str]]
    faq_page: Dict[str, Any]
    product_page: Dict[str, Any]
    comparison_page: Dict[str, Any]

from pydantic import BaseModel
from typing import List, Dict

class FAQItem(BaseModel):
    question: str
    answer: str
    category: str

class FAQPage(BaseModel):
    product_name: str
    faqs: List[FAQItem]

class ProductPage(BaseModel):
    name: str
    concentration: str
    skin_type: List[str]
    ingredients: List[str]
    benefits: List[str]
    usage: str
    side_effects: str
    price: str

class ComparisonPage(BaseModel):
    product_a: Dict
    product_b: Dict
    summary: str

from blocks.usage_block import extract_usage
from blocks.comparison_block import compare_ingredients, price_comparison
from models import FAQPage, FAQItem, ProductPage, ComparisonPage

def content_agent(state):
    product = state["product_data"]

    faq_items = []
    for category, qs in state["questions"].items():
        for q in qs[:1]:
            faq_items.append(
                FAQItem(
                    question=q,
                    answer="Based on provided product data.",
                    category=category
                )
            )

    state["faq_page"] = FAQPage(
        product_name=product["name"],
        faqs=faq_items
    ).dict()

    state["product_page"] = ProductPage(
        name=product["name"],
        concentration=product["concentration"],
        skin_type=product["skin_type"],
        ingredients=product["ingredients"],
        benefits=product["benefits"],
        usage=extract_usage(product),
        side_effects=product["side_effects"],
        price="₹699"
    ).dict()

    product_b = {
        "name": "RadiantSkin Serum",
        "ingredients": ["Niacinamide"],
        "benefits": ["Oil control"],
        "price": 899
    }

    summary = (
        compare_ingredients(product, product_b)
        + " "
        + price_comparison(product["price"], product_b["price"])
    )

    state["comparison_page"] = ComparisonPage(
        product_a=product,
        product_b=product_b,
        summary=summary
    ).dict()

    return state

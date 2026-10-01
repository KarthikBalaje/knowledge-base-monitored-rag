from app.knowledge_base.document_processor import clean_text
def test_clean(): assert clean_text("hello   world")=="hello world"

import json
from sentence_transformers import SentenceTransformer, util

# 載入模型
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 載入資料
with open('patents.json') as f:
    patents = json.load(f)

with open('company_products.json') as f:
    companies = json.load(f)

def check_infringement(patent_id, company_name, threshold=0.7):
    # 查找專利和公司資料
    patent = next((p for p in patents if p["publication_number"] == patent_id), None)
    if not patent:
        raise ValueError("Patent not found")
    
    company = next((c for c in companies["companies"] if c["name"].lower() == company_name.lower()), None)
    if not company:
        raise ValueError("Company not found")
    
    infringement_results = []
    patent_claims = json.loads(patent["claims"])
    
    # 計算產品描述和專利聲明的相似性
    for product in company["products"]:
        product_embedding = model.encode(product["description"], convert_to_tensor=True)
        relevant_claims = []
        explanation = ""

        for claim in patent_claims:
            claim_embedding = model.encode(claim["text"], convert_to_tensor=True)
            similarity = util.pytorch_cos_sim(product_embedding, claim_embedding).item()
            
            if similarity >= threshold:
                relevant_claims.append(claim["num"])
                explanation += f"Claim {claim['num']} has a similarity score of {similarity:.2f}. "

        if relevant_claims:
            infringement_likelihood = "High" if len(relevant_claims) > 3 else "Moderate"
            infringement_results.append({
                "product_name": product["name"],
                "infringement_likelihood": infringement_likelihood,
                "relevant_claims": relevant_claims,
                "explanation": explanation
            })

    if not infringement_results:
        raise ValueError("No infringement detected")

    return {
        "analysis_id": "1",
        "patent_id": patent_id,
        "company_name": company_name,
        "analysis_date": "2024-10-31",
        "top_infringing_products": infringement_results
    }

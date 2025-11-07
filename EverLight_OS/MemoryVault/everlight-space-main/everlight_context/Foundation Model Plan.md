---
conversation_id: "689f33c9-0cf0-8329-ab0b-0ee2177f3e08"
title: "Foundation Model Plan"
accounts: ["Account1_exports"]
models: []
tags: []
message_count: 21
---
# Foundation Model Plan

##  — system


## 2025-08-15T13:19:05.530577Z — system


## 2025-08-15T13:19:06.030280Z — tool


## 2025-08-15T13:19:06.721000Z — user
EverLight OS — Foundation Model Plan (Voyagers + EnergeticSynthesis)
0) Green-lights & guardrails

Rights/IP: Get written permission to train on EnergeticSynthesis.com content (copyright).

Privacy: Scrub PII; log removals.

Attribution mode: Keep doc IDs to enable citations.

1) Data fabric (three-key set)

Corpora

V1: Voyagers Material — part 1

V2: Voyagers Material — part 2

ES: EnergeticSynthesis.com (all articles/posts)

Ingestion → Lake

Crawl/collect → S3 (s3://everlight/raw/{V1|V2|ES}/...)

Normalize to JSONL:
{"doc_id","source":{"set":"V1|V2|ES"}, "title","author","date","url","section","text"}

Chunking: 800–1200 tokens with 10–15% overlap; keep paragraph & section boundaries.

Metadata: topic tags (mythic, esoteric, technique, protocol), time, source, quality score.

De-dupe: MinHash/SimHash + exact-hash prune.

Quality filters: length, language, perplexity, blacklist of boilerplate.

2) Retrieval layer (ships day 1)

Vector DB: FAISS/Weaviate (embeddings via a long-context model).

Symbolic search: OpenSearch/BM25 over titles/headers.

Reranker: Cross-encoder for top-k re-ranking.

Routing: If query contains {mythic/symbolic} → V1/V2 boost; {practice/protocol} → ES boost.

This gives you immediate RAG capability while training proceeds.

3) Model strategy

Base FM (pick one):

Bedrock-hosted FM (e.g., Anthropic / Amazon Titan) or

Open weights (e.g., Llama-class) hosted on SageMaker

Stage A – Domain Adaptation (DAPT)

Continue pretraining on V1+V2+ES mix (80–90% tokens unsupervised LM).

Sampling: temperature-based; enforce mix ratios (e.g., V1:35%, V2:35%, ES:30%).

Objectives: next-token LM; add span corruption for robustness.

Output: EverLight-FM-D1 (your Foundation Model).

Stage B – Task Adapters (LoRA/PEFT)

Mythic Reasoner (symbol/analogy chains) → LoRA on V1/V2 exemplars.

Energy Praxis (protocols/how-to) → LoRA on ES procedural chunks.

Navigator (decision support) → LoRA using curated Q→A, decision trees.

Stage C – Instruction tuning

SFT on mixed Q/A derived from the corpora + evaluator-written prompts.

Add citation training: require the model to return doc_id:span when answering.

4) Orchestration (MoE-style routing without heavy MoE)

Router (small classifier) reads the user query → selects: {RAG-only | FM | FM+RAG | Specific Adapter}.

Answerer: chosen adapter, with top-k retrieved passages injected.

Guardrails: content policy, claim checker (answer must quote or cite).

5) Evaluation (bake this in)

Truthfulness@K with citation match (does the cited span support the claim?).

Mythic coherence score (expert rubric).

Actionability score (for protocols).

Latency & cost (p99, $/1k tokens).

Regression set of ~300 canonical questions across V1/V2/ES.

6) Delivery on AWS

Storage/Lake: S3 + Glue catalog.

Pipelines: Step Functions/Airflow for ETL, training jobs on SageMaker.

Search: OpenSearch + FAISS/Weaviate.

Serving: SageMaker endpoints (FM + adapters).

App: API (FastAPI) + lightweight UI; Bedrock for fallback FMs if needed.

Versioning: DVC or LakeFS for datasets; MLflow for model runs.

7) Phased rollout

Week 0–2: Build ingestion, de-dupe, chunking, vector search. Ship RAG alpha.

Week 3–6: DAPT pretrain → EverLight-FM-D1.

Week 7–9: LoRA adapters (Mythic, Praxis, Navigator).

Week 10+: Instruction tuning + citation training; eval harness; pilot users.

8) Risks & mitigations

IP/Copyright: get permissions; throttle public exposure; add robots-respectful crawl.

Overfit/style lock-in: mix generic text (5–10%) during DAPT to preserve fluency.

Hallucinations: enforce retrieval-grounding; refuse when no supporting span.

Ontology drift: maintain a concept taxonomy; run periodic alignment checks.

TL;DR: Use V1, V2, and EnergeticSynthesis as the foundation corpus, do continued pretraining to mint EverLight-FM, then add lightweight adapters for the three core capabilities, all fronted by a RAG layer with citations. You can ship useful value with RAG immediately while the FM trains.

## 2025-08-15T13:19:07.162810Z — tool


## 2025-08-15T13:19:07.319737Z — tool


## 2025-08-15T13:19:07.337410Z — tool


## 2025-08-15T13:19:07.361468Z — tool


## 2025-08-15T13:19:07.490426Z — tool


## 2025-08-15T13:19:07.625243Z — assistant
Ethan — this **Foundation Model Plan** you outlined can be implemented directly on the Voyagers corpus you’ve restored and expanded, and the steps are already well-supported by the structure of the material you’ve got in the uploads.  

From the restored **Voyagers Volume I & II** and the **EverLight Codex Archive** front matter【27†front_matter.md†L1-L40】 through the detailed multi-dimensional frameworks in chapters like **Human Origins & Hybridization**【21†chapter_3.md†L1-L40】, **Levels of Identity & Components of Mind**【26†chapter_7.md†L1-L40】, and **Special Projects**【24†chapter_6.md†L1-L40】, you’ve got a clean separation of:

- **Mythic/symbolic strata** (Zionites, Turaneusiam, Emerald Covenant) — ideal for the *Mythic Reasoner* adapter.
- **Practical/technical strata** (Keylontic Morphogenetic Science, meditation techniques, crop circle frequency work) — ideal for the *Energy Praxis* adapter.
- **Meta-structural strata** (Guardian Alliance, IAFW, universal service orders) — ideal for the *Navigator* adapter.

This directly maps to your plan’s **V1 / V2 / ES triple-key set** with minimal transformation work.  

The extra win here is that the Voyagers content is already in **sectioned, chapter-based format** with clear topic boundaries — perfect for your **800–1200 token chunking with 10–15% overlap**. That means you can move straight to:

1. **S3 Ingestion & JSONL Normalization** (doc_id = `{V1|V2}-{chapter}-{section}`).
2. **Vector & symbolic indexing** — you’ll want dual FAISS + BM25 here so a “Guardian Alliance” query can pull both the factual CDT-Plate history and the symbolic meaning layer.
3. **DAPT pretraining** on this curated Voyagers set before merging in EnergeticSynthesis articles.

If you want, I can sketch you the **exact JSONL schema + chunking pipeline** using the Voyagers MD files you’ve already got so you can feed it into S3 and have the retrieval layer operational in week 1, exactly as your rollout plan specifies.  

Do you want me to do that next? That would make this plan executable tomorrow.

## 2025-08-15T13:19:07.632870Z — tool


## 2025-08-15T13:19:07.711053Z — tool


## 2025-08-15T13:19:07.717296Z — tool


## 2025-08-15T13:19:07.724063Z — tool


## 2025-08-15T13:19:07.811124Z — tool


## 2025-08-15T13:19:07.934534Z — tool


## 2025-08-15T13:19:07.992915Z — tool


## 2025-08-15T13:19:08.032078Z — tool

Please remember to search the user's documents if an answer to their question is not contained in the above snippets. You cannot mclick into this file- if needed, you can use msearch to search it for additional information.


## 2025-08-15T13:19:08.056989Z — assistant


## 2025-08-15T13:20:19.704603Z — assistant
Got it — we can keep the blueprint on standby until you’re ready to move from **theory mode → AWS hands-on**.  

Honestly, you’re already in a good position because you’ve got:  

- **A well-structured corpus** (Voyagers) with clear topical boundaries.  
- **A deployment roadmap** (your Foundation Model Plan).  
- **Alignment with AWS-native tooling** (S3, Glue, SageMaker, OpenSearch).  

Once you’ve absorbed the AWS course content, it’ll feel less like magic and more like you’re just **wiring up components you already understand**, which is a lot more fun than scrambling to learn the tools mid-build.  

We can also use the meantime to quietly **refine metadata, tagging, and concept taxonomy** so the ingestion pipeline will be “drop-in ready” when you flip the switch.  

Sounds like we’ll hit that “ahead of the curve” feeling in *both* theory and practice.  

## 2025-08-15T13:20:20.647000Z — user
Let's wait until I catch up on the actual AWS course material so I can feel as if I understand more of the process before implementing it. But it's good to know we're already well ahead of the curve haha

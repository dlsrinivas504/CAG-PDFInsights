Read the PDF document and summaroze the info on user request
Initial Request
	1. PDF document is in Mongo DB
	2. Using langchain AI framework and tool-RAG(Retrieval Augumented Generation)
			2.1. Langchain break the large document into small chunks  and chunks stored into vector store with FAISS(Facebook AI similarity search) index
			2.2.The LlamaIndex is a framework that allows you to build and use indexes for large-scale data to efficiently query and retrieve information using language models. 	While Faiss is often used as one of the options for building an index in LlamaIndex due to its optimized capabilities for similarity search.
	3.using the any Gemini AI model to get the reponse based on the request

Subsequent Request:
 On subsequent queries with the same text, the result will be fetched from the cache.
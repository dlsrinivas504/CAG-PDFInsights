from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI

class PerformConversationalChain:

    def get_conversational_chain():
        print("inside get_conversational_chain")
        prompt_template = """
        Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
        provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
        Context:\n {context}?\n
        Question: \n{question}\n

        Answer:
        """
        model=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
        prompt = PromptTemplate(template=prompt_template,input_variables=["context","question"])
        chain = load_qa_chain(model,chain_type="stuff",prompt=prompt)
        return chain
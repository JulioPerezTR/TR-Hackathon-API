
from chat.indexing import DocumentMilvus


#import ast  # for converting embeddings saved as strings back to arrays
import openai  # for calling the OpenAI API
import pandas as pd  # for storing text and embeddings data
#import tiktoken  # for counting tokens

class Chat():    
    def ask(self, question):
        milvus = DocumentMilvus()
        #document={"text":text,"id":1,"name":"software_engineer","documentTypeId":"10","pageCount":10,}
        #milvus.index_document(document)
        docs = milvus.ask_question(question)
        print(docs)
        documents_from_milvus = []

        for doc in docs:
            documents_from_milvus.append(doc[0].page_content)

        return documents_from_milvus
    
    def ask_and_analyze(self, question):
        milvus = DocumentMilvus()
        #document={"text":text,"id":1,"name":"software_engineer","documentTypeId":"10","pageCount":10,}
        #milvus.index_document(document)
        docs = milvus.ask_question(question)
        print(docs)
        documents_from_milvus = ""

        count = 0
        for doc in docs:
            if count > 2:
                break
            documents_from_milvus += doc[0].page_content
            count +=1

        GPT_MODEL = "gpt-3.5-turbo"

        query = f"""Use the below article above Thomson Reuters Employess reviews, answer the subsequent question. If the answer cannot be found, write "I don't know."

        Article:
        \"\"\"
        {documents_from_milvus}
        \"\"\"

        Question: Is there any bias in the reviews about Thomson Reuters?"""
        openai.api_key = "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"
        response = openai.ChatCompletion.create(
            messages=[
                {'role': 'system', 'content': 'Your Answer about Bias in TR employees review.'},
                {'role': 'user', 'content': query},
            ],
            model=GPT_MODEL,
            temperature=0,
        )

        return response['choices'][0]['message']['content']
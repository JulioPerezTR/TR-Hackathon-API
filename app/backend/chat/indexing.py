from typing import Any, Dict
from abc import ABC, abstractmethod
from collections import defaultdict

from langchain.schema.document import Document
from langchain.text_splitter import SpacyTextSplitter
import json
from tqdm import tqdm
import urllib.error
import urllib.request
from typing import Any, Dict, List
from langchain.vectorstores.milvus import Milvus
from langchain.embeddings.base import Embeddings
import requests

from typing import (
    Any,
    List,
)

class DocumentProcessor(ABC):
    "Document Processor"
    @abstractmethod
    def process_document(self, document: Any) -> Any:
        pass

class EmbeddingGenerator(Embeddings):
    "Embedding Generator Class"

    def __init__(self):
        #self._api_url="https://api-inference.huggingface.co/models/intfloat/e5-large-v2"
        self._api_url="http://40.124.47.43:80/api/v1/service/e5-large-v2/score"
        self._batch_size=32
        #self._api_key="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"
        self._api_key="v3nKcecuel8NRZyahm8qy0sB909vh3XU"


    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed search docs."""

        embeddings = []
        print(len(texts))
        print(self._batch_size)
        for i in range(0, len(texts), self._batch_size):
            embeddings.extend(self._generate_embeddings(texts[i: i + self._batch_size]))

        #text_batches = [texts[i: i + self._batch_size] for i in range(0, len(texts), self._batch_size)]
        
        #embeddings = []
        #for text_batch in tqdm(text_batches):
            #embeddings.extend(self._generate_embeddings(text_batch))
        return embeddings
    
    def _generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings using the Embaas API."""
        payload = str.encode(json.dumps(texts), "utf-8")
        #payload = {"sentences":{"source_sentence":texts}}
        try:
            headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + self._api_key)}
            #response = requests.post(self._api_url, headers=headers, json=payload)
            #embeddings= response.json()
            req = urllib.request.Request(self._api_url, payload, headers)
            response = urllib.request.urlopen(req, timeout=200)
            embeddings = json.loads(response.read())
            return embeddings['embeddings']
        except urllib.error.HTTPError as error:
            error = "Http Error when calling request during embeddings."
            raise Exception(error)
        except Exception:
            error = "Unexpected Error when getting embeddings."
            raise Exception(error)
    
    def embed_query(self, text: str) -> List[float]:
        """Embed query text."""
        return self._generate_embeddings(text)

class DocumentMilvus(DocumentProcessor,SpacyTextSplitter):

    def __init__(self):

        try:
            self._vector_store = Milvus(
                collection_name="software_developer_1",
                embedding_function=EmbeddingGenerator(),
                connection_args={"uri":"https://in03-bfba916462319ba.api.gcp-us-west1.zillizcloud.com","token":"c52727333ba431c498f54ff058405d3b66a0bf7a029c7b8e37996e92be7d75d35a247744eebf53a2684a6782b8c3377eb68f34e6"},
                #search_params=dict(**self._config["search_params"])
            )

            self._config = {"chunk_size": 1024,"chunk_overlap": 0}
            super().__init__(**self._config)
        except Exception as exc:
            err="Error When Connecting with Milvus"
            return err

    def _get_document_wrapper(self,document: Any) -> Document:
        try:

            doc = Document(
                page_content=document['text'],
                metadata={
                    "doc_id": str(document['id']),
                    'name': str(document['name']),
                    'doc_type_id': str(document['documentTypeId']),
                    'doc_page_count': int(document['pageCount'])
                }
            )
        except Exception:
            error = "Error when creating the Document Wrapper."
            raise Exception(error)

        return doc
    
    def process_document(self, document: Any) -> Any:

        try:
            doc = self._get_document_wrapper(document)
            # Split the documents into smaller chunks
            chunks = self.split_documents([doc])
            # Add unique (combined) ID and chunk ID to each chunk
            self.add_chunk_ids_to_chunks(chunks)

            return chunks
        except Exception as exc:
            error = "Error when processing input document."
            raise Exception(error)
        
    def add_chunk_ids_to_chunks(self,chunks):
        # Initialize a dictionary to store the chunk ID for each document
        doc_chunk_ids = {}

        # Iterate through the chunks
        for chunk in chunks:
            doc_id = chunk.metadata["doc_id"]

            # Get the current chunk ID for the document or initialize it to 0
            chunk_id = doc_chunk_ids.get(doc_id, 0)

            # Update chunk metadata with chunk ID and combined ID
            chunk.metadata["chunk_id"] = chunk_id
            chunk.metadata["id"] = f"{doc_id}-{chunk_id}"

            # Increment the chunk ID for the current document
            doc_chunk_ids[doc_id] = chunk_id + 1
        
    def save_embeddings(self, text_chunks: List[Document]) -> Any:
        """Save embeddings."""
        doc_chunks = self._group_chunks_by_doc_id(text_chunks)
        for doc_id, doc_text_chunks in doc_chunks.items():
            #self._delete_embeddings_for_document(doc_id)
            texts = [d.page_content for d in doc_text_chunks]
            metadatas = [d.metadata for d in doc_text_chunks]
            self._vector_store.add_texts(texts=texts, metadatas=metadatas)

    @staticmethod
    def _group_chunks_by_doc_id(text_chunks: List[Document]) -> Dict[str, List[Document]]:
        grouped_chunks = defaultdict(list)
        for chunk in text_chunks:
            doc_id = chunk.metadata["doc_id"]
            grouped_chunks[doc_id].append(chunk)
        return grouped_chunks

    def index_document(self,document:Any):
        doc=self.process_document(document)
        self.save_embeddings(doc)

    def ask_question(self,query):
        #query = "What is milvus?"

        params= {"k": 30,"param": {"params":{"ef": 30}}}
        generator=EmbeddingGenerator()
        embedding_query=generator.embed_query(query)
        docs = self._vector_store.similarity_search_with_score_by_vector(embedding=embedding_query,param=params)
        return docs


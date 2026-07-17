from rag_helper import RAGBase
from exporter import SQLiteSpanExporter

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)

# Configure tracing
provider = TracerProvider()
# provider.add_span_processor(
#     SimpleSpanProcessor(ConsoleSpanExporter())
# )
provider.add_span_processor(
    SimpleSpanProcessor(SQLiteSpanExporter("traces.db"))
)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)


class RAGTraced(RAGBase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def search(self, query, num_results=5):
        with tracer.start_as_current_span("search") as span_search:
            return super().search(query, num_results)

    def build_prompt(self, query, search_results):
        return super().build_prompt(query, search_results)

    def llm(self, prompt):
        with tracer.start_as_current_span("llm") as span:
            input_messages = [
                {'role': 'developer', 'content': self.instructions},
                {'role': 'user', 'content': prompt}
            ]

            response = self.llm_client.responses.create(
                model=self.model,
                input=input_messages
            )

            span.set_attribute("input_tokens", response.usage.input_tokens)
            span.set_attribute("output_tokens", response.usage.output_tokens)

            return response
        
    def ragWithTrace(self, query):
        with tracer.start_as_current_span("rag") as span_rag:
            return self.rag(query)
        
    def rag(self, query):
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        response = self.llm(prompt)
        return response.output_text
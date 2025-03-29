import os
from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Set up OpenTelemetry tracing
trace.set_tracer_provider(TracerProvider())
tracer_provider = trace.get_tracer_provider()

# Configure OTLP exporter (adjust endpoint if needed)
otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317")
otlp_exporter = OTLPSpanExporter(endpoint=otlp_endpoint, insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)

app = FastAPI()

# Instrument FastAPI with OpenTelemetrys
FastAPIInstrumentor.instrument_app(app)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
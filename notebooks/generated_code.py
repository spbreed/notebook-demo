from diagrams import Cluster, Diagram
from diagrams.aws.general import InternetAlt1
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.analytics import Glue, DataPipeline
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.aws.ml import SagemakerNotebook, SagemakerModel, Sagemaker
from diagrams.aws.ml import AugmentedAi
from diagrams.azure.ml import CognitiveServices
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.azure.web import AppServices
from diagrams.generic.compute import Rack

with Diagram("AI Lifecycle Architecture", show=False):
    internet = InternetAlt1("Internet & 3rd Party")

    with Cluster("Stage 1: Data Sources"):
        structured_data = RDS("Structured Data")
        semi_structured_data = Dynamodb("Semi-Structured Data")
        unstructured_data = SimpleStorageServiceS3Bucket("Unstructured Data")

    with Cluster("Stage 2: Data Pipelines"):
        glue = Glue("AWS Glue")
        data_pipeline = DataPipeline("AWS Data Pipeline")

    with Cluster("Stage 3: Data Sets"):
        training_data = SimpleStorageServiceS3("Training Data")
        rag_data = SimpleStorageServiceS3("RAG Data")

    with Cluster("Stage 4: AI Inventory"):
        model_registry = SagemakerModel("Model Registry")
        mlflow = Sagemaker("MLflow")
        kubeflow = Sagemaker("Kubeflow")

    with Cluster("Stage 5: Training and Development"):
        sagemaker_notebook = SagemakerNotebook("Sagemaker Notebook")

    with Cluster("Stage 6: Serving and Inference"):
        sagemaker_endpoint = Sagemaker("Sagemaker Endpoint")

    with Cluster("Stage 7: Multi-Agent Systems"):
        azure_openai = CognitiveServices("Azure OpenAI")

    with Cluster("Stage 8: AI Use Cases"):
        retail_agent = AppServices("Retail Agent")
        recommendation_agent = AppServices("Recommendation Agent")

    # Connections
    internet >> structured_data
    internet >> semi_structured_data
    internet >> unstructured_data
    structured_data >> glue
    semi_structured_data >> glue
    unstructured_data >> glue
    glue >> data_pipeline
    data_pipeline >> training_data
    data_pipeline >> rag_data
    training_data >> model_registry
    rag_data >> model_registry
    model_registry >> sagemaker_notebook
    sagemaker_notebook >> sagemaker_endpoint
    sagemaker_endpoint >> azure_openai
    azure_openai >> retail_agent
    azure_openai >> recommendation_agent

    # Overarching layer
    with Cluster("Model Guardrails & Monitoring", direction="TB"):
        guardrails = Rack("Guardrails & Monitoring")
        guardrails >> internet
        guardrails >> structured_data
        guardrails >> semi_structured_data
        guardrails >> unstructured_data
        guardrails >> glue
        guardrails >> data_pipeline
        guardrails >> training_data
        guardrails >> rag_data
        guardrails >> model_registry
        guardrails >> sagemaker_notebook
        guardrails >> sagemaker_endpoint
        guardrails >> azure_openai
        guardrails >> retail_agent
        guardrails >> recommendation_agent

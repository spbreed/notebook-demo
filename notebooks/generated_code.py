from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import InternetAlt1
from diagrams.aws.database import RDS, DatabaseMigrationService
from diagrams.aws.analytics import Glue, DataPipeline
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.aws.ml import SagemakerNotebook, SagemakerModel, Sagemaker
from diagrams.azure.ml import CognitiveServices

# Define the diagram
with Diagram("AI Lifecycle Architecture", show=False, direction="LR"):

    # Stage 0: Internet & 3rd Party
    with Cluster("Stage 0: Internet & 3rd Party"):
        internet = InternetAlt1("External Inputs")

    # Stage 1: Data Sources
    with Cluster("Stage 1: Data Sources"):
        legacy_db = DatabaseMigrationService("On-prem DB\n& Warehouses")
        structured_data = RDS("Structured Data")
        semi_unstructured_data = RDS("Semi-Structured\n& Unstructured Data")

    # Stage 2: Data Pipelines
    with Cluster("Stage 2: Data Pipelines"):
        data_pipeline = DataPipeline("Data Pipeline")
        data_glue = Glue("Transform & Validate")

    # Stage 3: Data Sets
    with Cluster("Stage 3: Data Sets"):
        s3_datasets = SimpleStorageServiceS3("S3 Datasets")
        training_data = SimpleStorageServiceS3("Training Data")
        rag_data = SimpleStorageServiceS3("RAG Datasets")

    # Stage 4: AI Inventory
    with Cluster("Stage 4: AI Inventory"):
        model_registry = SagemakerModel("Model Registry")
        mlflow = Sagemaker("MLflow")
        kubeflow = Sagemaker("Kubeflow")

    # Stage 5: Training and Development
    with Cluster("Stage 5: Training and Development"):
        sagemaker_notebook = SagemakerNotebook("Sagemaker Notebook")
        external_models = Sagemaker("External Models")

    # Stage 6: Serving and Inference
    with Cluster("Stage 6: Serving and Inference"):
        serving_endpoint = SagemakerModel("Sagemaker Endpoint")

    # Stage 7: Multi-Agent Systems
    with Cluster("Stage 7: Multi-Agent Systems"):
        azure_openai = CognitiveServices("Azure OpenAI")

    # Stage 8: AI Use Cases
    with Cluster("Stage 8: AI Use Cases"):
        retail_agent = Sagemaker("Retail Agent")
        recommendation_agent = Sagemaker("Recommendation Agent")

    # Model Guardrails and Monitoring Layer
    model_guardrails = Edge(color="darkgray", style="dashed")

    # Diagram Connections
    internet >> legacy_db
    internet >> structured_data
    internet >> semi_unstructured_data
    legacy_db >> data_pipeline
    structured_data >> data_pipeline
    semi_unstructured_data >> data_pipeline
    data_pipeline >> data_glue
    data_glue >> s3_datasets
    s3_datasets >> training_data
    s3_datasets >> rag_data
    training_data >> sagemaker_notebook
    rag_data >> sagemaker_notebook
    sagemaker_notebook >> model_registry
    model_registry >> serving_endpoint
    serving_endpoint >> azure_openai
    azure_openai >> retail_agent
    azure_openai >> recommendation_agent

    # Overarching Layer for Guardrails and Monitoring
    for stage in [legacy_db, structured_data, semi_unstructured_data, data_pipeline, 
                  data_glue, s3_datasets, training_data, rag_data, 
                  model_registry, sagemaker_notebook, serving_endpoint, azure_openai]:
        stage >> model_guardrails

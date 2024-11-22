from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import InternetGateway
from diagrams.aws.database import RDSInstance
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.aws.analytics import Glue, DataPipeline
from diagrams.aws.ml import Sagemaker, SagemakerNotebook, SagemakerModel
from diagrams.aws.management import Cloudwatch
from diagrams.azure.ml import CognitiveServices
from diagrams.azure.identity import ActiveDirectory

with Diagram("AI Lifecycle Architecture", show=False, direction="TB"):

    with Cluster("Stage 0: Internet & 3rd Party"):
        internet = InternetGateway("Internet & 3rd Party")

    with Cluster("Stage 1: Data Sources"):
        structured_data = RDSInstance("Legacy SQL DB")
        unstructured_data = RDSInstance("Data Warehouses")
        data_scanner = CognitiveServices("Data & License Scanner")

    with Cluster("Stage 2: Data Pipelines"):
        data_pipeline = DataPipeline("AWS Data Pipeline")
        glue_service = Glue("AWS Glue")

    with Cluster("Stage 3: Data Sets"):
        training_data = SimpleStorageServiceS3("Training Data")
        rag_data = SimpleStorageServiceS3("RAG Data")

    with Cluster("Stage 4: AI Inventory"):
        model_registry = SagemakerModel("Model Registry")

    with Cluster("Stage 5: Training and Development"):
        sagemaker_notebook = SagemakerNotebook("Sagemaker Notebook")

    with Cluster("Stage 6: Serving and Inference"):
        sagemaker_endpoint = Sagemaker("Sagemaker Endpoint")
        monitoring = Cloudwatch("Monitoring")

    with Cluster("Stage 7: Multi-Agent Systems"):
        azure_openai = ActiveDirectory("Azure OpenAI")

    with Cluster("Stage 8: AI Use Cases"):
        retail_agent = CognitiveServices("Retail Agent")
        recommendation_agent = CognitiveServices("Recommendation Agent")

    internet >> structured_data
    internet >> unstructured_data
    structured_data >> data_scanner
    unstructured_data >> data_scanner
    data_scanner >> data_pipeline
    data_pipeline >> glue_service
    glue_service >> training_data
    glue_service >> rag_data
    training_data >> model_registry
    rag_data >> model_registry
    model_registry >> sagemaker_notebook
    sagemaker_notebook >> sagemaker_endpoint
    sagemaker_endpoint >> monitoring
    azure_openai >> sagemaker_endpoint
    sagemaker_endpoint >> retail_agent
    sagemaker_endpoint >> recommendation_agent

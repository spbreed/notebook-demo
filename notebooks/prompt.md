Generate a `diagrams.mingrammer.com` code snippet to create the following architecture diagram:

## General Layout

---
Design a detailed architecture diagram showcasing the entire AI lifecycle, with interconnected modules representing key stages and processes deployed in {target_cloud_provider}. The diagram should include the following elements:



The archiecture flow begins with Stage 0 (Internet & 3rd Party), which provides external inputs and connects to Stage 1 (Data Sources), where different types of data are collected and prepared for processing. The data flows into Stage 2 (Data Pipelines), where it is transformed and validated before being separated into Stage 3 (Data Sets) for training or retrieval purposes. These datasets support Stage 5 (Training and Development), where models are trained and developed, and outputs are sent to Stage 6 (Serving and Inference) for deployment and monitoring.

Supporting these processes, Stage 4 (AI Inventory) manages metadata, model, and feature information, while Stage 7 (Multi-Agent Systems) handles routing, integration, and optimization thats connected to Stage 8. Finally, all processes contribute to Stage 8 (AI Use Cases), where the outcomes are applied across user, developer, and business domains. The stages are interconnected to ensure seamless workflow across the AI lifecycle.

## Diagram Requirements
- **Visual Features**:
  - Clear labels for each stage.
  - Directional arrows to show workflows
  - Dont use any imports thats not listed in reference library section below
  - Color-coded modules to distinguish stages
  - donot import diagrams.generic.blank 
  - strictly donot use from diagrams.aws.database import GenericDatabase
  - Each node should be inside a cluster
  - {ai_security_controls} is overarching across all the stages and foundational layer and represennt as a horizontal and foundational layer thats spans across the stages
- **Layout**:
  - Sequential yet interconnected representation of the AI lifecycle.

Represent {data_sources} in stage 1 datasoruces structured, semi-structured, and unstructured data. Show connections to external internet sources for models, software, and datasets, with tools like scanners (model, data, and license) assessing quality and compliance.

{data_pipelines} in stage 2 are data pipelines Highlight transformations, validations, embeddings, and flow into the dataset stage. Include access control and anonymization mechanisms.

{data_sets} in stage 3 are datasets Separate training data and Retrieval-Augmented Generation (RAG) datasets, showing PII detection and redundancy mechanisms.

{ai_inventory}: in stage 4 are AI inventory Illustrate components like data catalogs, model registries, and feature stores, supported by model governance and validation rules.

{ai_training_environment}: in stage 5 training and development Cover supervised, unsupervised, reinforcement learning, LLM training, and adversarial models. Include external models and environment provisioning and model validation.

{ai_deployment_platform} in stage 6 are servinga nd inference platforms that Depict model deployments of {model_type}, gateways, and monitoring systems.

{ai_agents}: in stage 7 are multi agent systems Show output grounding, agent routing, and prompt engineering. Include permissions, segregation of duties, and user feedback loops.

{ai_usecases}: in stage 8 are AI usecases Separate areas into user productivity, developer productivity, and business use cases (e.g., chatbots, code generators, security tools, adaptive UX).

Use clear labels, directional arrows for workflows, and color-coding to distinguish stages, processes, and security layers. The layout should reflect the sequential yet interconnected nature of the AI lifecycle

---

# reference Libraries
Use the following libraries for the diagram:
# AWS Analytics
from diagrams.aws.analytics import AmazonOpensearchService, Analytics, Athena, CloudsearchSearchDocuments, Cloudsearch, DataLakeResource, DataPipeline, ElasticsearchService, EMRCluster, EMREngineMaprM3, EMREngineMaprM5, EMREngineMaprM7, EMREngine, EMRHdfsCluster, EMR, GlueCrawlers, GlueDataCatalog, Glue, KinesisDataAnalytics, KinesisDataFirehose, KinesisDataStreams, KinesisVideoStreams, Kinesis, LakeFormation, ManagedStreamingForKafka, Quicksight, RedshiftDenseComputeNode, RedshiftDenseStorageNode, Redshift

# AWS AR
from diagrams.aws.ar import ArVr, Sumerian

# AWS Blockchain
from diagrams.aws.blockchain import BlockchainResource, Blockchain, ManagedBlockchain, QuantumLedgerDatabaseQldb

# AWS Business
from diagrams.aws.business import AlexaForBusiness, BusinessApplications, Chime, Workmail

# AWS Compute
from diagrams.aws.compute import AppRunner, ApplicationAutoScaling, Batch, ComputeOptimizer, Compute, EC2Ami, EC2AutoScaling, EC2ContainerRegistryImage, EC2ContainerRegistryRegistry, EC2ContainerRegistry, EC2ElasticIpAddress, EC2ImageBuilder, EC2Instance, EC2Instances, EC2Rescue, EC2SpotInstance, EC2, ElasticBeanstalkApplication, ElasticBeanstalkDeployment, ElasticBeanstalk, ElasticContainerServiceContainer, ElasticContainerServiceService, ElasticContainerService, ElasticKubernetesService, Fargate, LambdaFunction, Lambda, Lightsail, LocalZones, Outposts, ServerlessApplicationRepository, ThinkboxDeadline, ThinkboxDraft, ThinkboxFrost, ThinkboxKrakatoa, ThinkboxSequoia, ThinkboxStoke, ThinkboxXmesh, VmwareCloudOnAWS, Wavelength

# AWS Cost Management
from diagrams.aws.cost import Budgets, CostAndUsageReport, CostExplorer, CostManagement, ReservedInstanceReporting, SavingsPlans

# AWS Database
from diagrams.aws.database import AuroraInstance, Aurora, DatabaseMigrationServiceDatabaseMigrationWorkflow, DatabaseMigrationService, Database, DocumentdbMongodbCompatibility, DynamodbAttribute, DynamodbAttributes, DynamodbDax, DynamodbGlobalSecondaryIndex, DynamodbItem, DynamodbItems, DynamodbTable, Dynamodb, ElasticacheCacheNode, ElasticacheForMemcached, ElasticacheForRedis, Elasticache, KeyspacesManagedApacheCassandraService, Neptune, QuantumLedgerDatabaseQldb, RDSInstance, RDSMariadbInstance, RDSMysqlInstance, RDSOnVmware, RDSOracleInstance, RDSPostgresqlInstance, RDSSqlServerInstance, RDS, RedshiftDenseComputeNode, RedshiftDenseStorageNode, Redshift, Timestream

# AWS Developer Tools
from diagrams.aws.devtools import CloudDevelopmentKit, Cloud9Resource, Cloud9, Codeartifact, Codebuild, Codecommit, Codedeploy, Codepipeline, Codestar, CommandLineInterface, DeveloperTools, ToolsAndSdks, XRay

# AWS Enablement
from diagrams.aws.enablement import CustomerEnablement, Iq, ManagedServices, ProfessionalServices, Support

# AWS End User Computing
from diagrams.aws.enduser import Appstream20, DesktopAndAppStreaming, Workdocs, Worklink, Workspaces

# AWS Customer Engagement
from diagrams.aws.engagement import Connect, CustomerEngagement, Pinpoint, SimpleEmailServiceSesEmail, SimpleEmailServiceSes

# AWS Game Tech
from diagrams.aws.game import GameTech, Gamelift

# AWS General
from diagrams.aws.general import Client, Disk, Forums, General, GenericDatabase, GenericFirewall, GenericOfficeBuilding, GenericSamlToken, GenericSDK, InternetAlt1, InternetAlt2, InternetGateway, Marketplace, MobileClient, Multimedia, OfficeBuilding, SamlToken, SDK, SslPadlock, TapeStorage, Toolkit, TraditionalServer, User, Users

# AWS Integration
from diagrams.aws.integration import ApplicationIntegration, Appsync, ConsoleMobileApplication, EventResource, EventbridgeCustomEventBusResource, EventbridgeDefaultEventBusResource, EventbridgeSaasPartnerEventBusResource, Eventbridge, ExpressWorkflows, MQ, SimpleNotificationServiceSnsEmailNotification, SimpleNotificationServiceSnsHttpNotification, SimpleNotificationServiceSnsTopic, SimpleNotificationServiceSns, SimpleQueueServiceSqsMessage, SimpleQueueServiceSqsQueue, SimpleQueueServiceSqs, StepFunctions

# AWS IoT
from diagrams.aws.iot import Freertos, InternetOfThings, Iot1Click, IotAction, IotActuator, IotAlexaEcho, IotAlexaEnabledDevice, IotAlexaSkill, IotAlexaVoiceService, IotAnalyticsChannel, IotAnalyticsDataSet, IotAnalyticsDataStore, IotAnalyticsNotebook, IotAnalyticsPipeline, IotAnalytics, IotBank, IotBicycle, IotButton, IotCamera, IotCar, IotCart, IotCertificate, IotCoffeePot, IotCore, IotDesiredState, IotDeviceDefender, IotDeviceGateway, IotDeviceManagement, IotDoorLock, IotEvents, IotFactory, IotFireTvStick, IotFireTv, IotGeneric, IotGreengrassConnector, IotGreengrass, IotHardwareBoard, IotHouse, IotHttp, IotHttp2, IotJobs, IotLambda, IotLightbulb, IotMedicalEmergency, IotMqtt, IotOverTheAirUpdate, IotPolicyEmergency, IotPolicy, IotReportedState, IotRule, IotSensor, IotService, IotShadow, IotSimulator, IotSitewise, IotThermostat, IotThingsGraph, IotTopic, IotTravel, IotUtility, IotWindfarm

# AWS Management and Governance
from diagrams.aws.management import AmazonDevopsGuru, AmazonManagedGrafana, AmazonManagedPrometheus, AmazonManagedWorkflowsApacheAirflow, AutoScaling, Chatbot, CloudformationChangeSet, CloudformationStack, CloudformationTemplate, Cloudformation, Cloudtrail, CloudwatchAlarm, CloudwatchEventEventBased, CloudwatchEventTimeBased, CloudwatchRule, Cloudwatch, Codeguru, CommandLineInterface, Config, ControlTower, LicenseManager, ManagedServices, ManagementAndGovernance, ManagementConsole, OpsworksApps, OpsworksDeployments, OpsworksInstances, OpsworksLayers, OpsworksMonitoring, OpsworksPermissions, OpsworksResources, OpsworksStack, Opsworks, OrganizationsAccount, OrganizationsOrganizationalUnit, Organizations, PersonalHealthDashboard, Proton, ServiceCatalog, SystemsManagerAppConfig, SystemsManagerAutomation, SystemsManagerDocuments, SystemsManagerInventory, SystemsManagerMaintenanceWindows, SystemsManagerOpscenter, SystemsManagerParameterStore, SystemsManagerPatchManager, SystemsManagerRunCommand, SystemsManagerStateManager, SystemsManager, TrustedAdvisorChecklistCost, TrustedAdvisorChecklistFaultTolerant, TrustedAdvisorChecklistPerformance, TrustedAdvisorChecklistSecurity, TrustedAdvisorChecklist, TrustedAdvisor, WellArchitectedTool

# AWS Media Services
from diagrams.aws.media import ElasticTranscoder, ElementalConductor, ElementalDelta, ElementalLive, ElementalMediaconnect, ElementalMediaconvert, ElementalMedialive, ElementalMediapackage, ElementalMediastore, ElementalMediatailor, ElementalServer, KinesisVideoStreams, MediaServices

# AWS Migration and Transfer
from diagrams.aws.migration import ApplicationDiscoveryService, CloudendureMigration, DatabaseMigrationService, DatasyncAgent, Datasync, MigrationAndTransfer, MigrationHub, ServerMigrationService, SnowballEdge, Snowball, Snowmobile, TransferForSftp

# AWS Machine Learning
from diagrams.aws.ml import ApacheMxnetOnAWS, AugmentedAi, Comprehend, DeepLearningAmis, DeepLearningContainers, Deepcomposer, Deeplens, Deepracer, ElasticInference, Forecast, FraudDetector, Kendra, Lex, MachineLearning, Personalize, Polly, RekognitionImage, RekognitionVideo, Rekognition, SagemakerGroundTruth, SagemakerModel, SagemakerNotebook, SagemakerTrainingJob, Sagemaker, TensorflowOnAWS, Textract, Transcribe, Translate

# AWS Mobile
from diagrams.aws.mobile import Amplify, APIGatewayEndpoint, APIGateway, Appsync, DeviceFarm, Mobile, Pinpoint

# AWS Networking and Content Delivery
from diagrams.aws.network import APIGatewayEndpoint, APIGateway, AppMesh, ClientVpn, CloudMap, CloudFrontDownloadDistribution, CloudFrontEdgeLocation, CloudFrontStreamingDistribution, CloudFront, DirectConnect, ElasticLoadBalancing, ElbApplicationLoadBalancer, ElbClassicLoadBalancer, ElbNetworkLoadBalancer, Endpoint, GlobalAccelerator, InternetGateway, Nacl, NATGateway, NetworkFirewall, NetworkingAndContentDelivery, PrivateSubnet, Privatelink, PublicSubnet, Route53HostedZone, Route53, RouteTable, SiteToSiteVpn, TransitGateway, VPCCustomerGateway, VPCElasticNetworkAdapter, VPCElasticNetworkInterface, VPCFlowLogs, VPCPeering, VPCRouter, VPCTrafficMirroring, VPC, VpnConnection, VpnGateway

# AWS Quantum Technologies
from diagrams.aws.quantum import Braket, QuantumTechnologies

# AWS Robotics
from diagrams.aws.robotics import RobomakerCloudExtensionRos, RobomakerDevelopmentEnvironment, RobomakerFleetManagement, RobomakerSimulator, Robomaker, Robotics

# AWS Satellite
from diagrams.aws.satellite import GroundStation, Satellite

# AWS Security, Identity, and Compliance
from diagrams.aws.security import AdConnector, Artifact, CertificateAuthority, CertificateManager, CloudDirectory, Cloudhsm, Cognito, Detective, DirectoryService, FirewallManager, Guardduty, IdentityAndAccessManagementIamAccessAnalyzer, IdentityAndAccessManagementIamAddOn, IdentityAndAccessManagementIamAWSStsAlternate, IdentityAndAccessManagementIamAWSSts, IdentityAndAccessManagementIamDataEncryptionKey, IdentityAndAccessManagementIamEncryptedData, IdentityAndAccessManagementIamLongTermSecurityCredential, IdentityAndAccessManagementIamMfaToken, IdentityAndAccessManagementIamPermissions, IdentityAndAccessManagementIamRole, IdentityAndAccessManagementIamTemporarySecurityCredential, IdentityAndAccessManagementIam, InspectorAgent, Inspector, KeyManagementService, Macie, ManagedMicrosoftAd, ResourceAccessManager, SecretsManager, SecurityHubFinding, SecurityHub, SecurityIdentityAndCompliance, ShieldAdvanced, Shield, SimpleAd, SingleSignOn, WAFFilteringRule, WAF

# AWS Storage
from diagrams.aws.storage import Backup, CloudendureDisasterRecovery, EFSInfrequentaccessPrimaryBg, EFSStandardPrimaryBg, ElasticBlockStoreEBSSnapshot, ElasticBlockStoreEBSVolume, ElasticBlockStoreEBS, ElasticFileSystemEFSFileSystem, ElasticFileSystemEFS, FsxForLustre, FsxForWindowsFileServer, Fsx, MultipleVolumesResource, S3GlacierArchive, S3GlacierVault, S3Glacier, SimpleStorageServiceS3BucketWithObjects, SimpleStorageServiceS3Bucket, SimpleStorageServiceS3Object, SimpleStorageServiceS3, SnowFamilySnowballImportExport, SnowballEdge, Snowball, Snowmobile, StorageGatewayCachedVolume, StorageGatewayNonCachedVolume, StorageGatewayVirtualTapeLibrary, StorageGateway, Storage

# Azure Analytics
from diagrams.azure.analytics import AnalysisServices, DataExplorerClusters, DataFactories, DataLakeAnalytics, DataLakeStoreGen1, Databricks, EventHubClusters, EventHubs, Hdinsightclusters, LogAnalyticsWorkspaces, StreamAnalyticsJobs, SynapseAnalytics

# Azure Compute
from diagrams.azure.compute import AppServices, AutomanagedVM, AvailabilitySets, BatchAccounts, CitrixVirtualDesktopsEssentials, CloudServicesClassic, CloudServices, CloudsimpleVirtualMachines, ContainerApps, ContainerInstances, ContainerRegistries, DiskEncryptionSets, DiskSnapshots, Disks, FunctionApps, ImageDefinitions, ImageVersions, KubernetesServices, MeshApplications, OsImages, SAPHANAOnAzure, ServiceFabricClusters, SharedImageGalleries, SpringCloud, VMClassic, VMImages, VMLinux, VMScaleSet, VMWindows, VM, Workspaces

# Azure Database
from diagrams.azure.database import BlobStorage, CacheForRedis, CosmosDb, DataExplorerClusters, DataFactory, DataLake, DatabaseForMariadbServers, DatabaseForMysqlServers, DatabaseForPostgresqlServers, ElasticDatabasePools, ElasticJobAgents, InstancePools, ManagedDatabases, SQLDatabases, SQLDatawarehouse, SQLManagedInstances, SQLServerStretchDatabases, SQLServers, SQLVM, SQL, SsisLiftAndShiftIr, SynapseAnalytics, VirtualClusters, VirtualDatacenter

# Azure DevOps
from diagrams.azure.devops import ApplicationInsights, Artifacts, Boards, Devops, DevtestLabs, LabServices, Pipelines, Repos, TestPlans

# Azure General
from diagrams.azure.general import Allresources, Azurehome, Developertools, Helpsupport, Information, Managementgroups, Marketplace, Quickstartcenter, Recent, Reservations, Resource, Resourcegroups, Servicehealth, Shareddashboard, Subscriptions, Support, Supportrequests, Tag, Tags, Templates, Twousericon, Userhealthicon, Usericon, Userprivacy, Userresource, Whatsnew

# Azure Identity
from diagrams.azure.identity import AccessReview, ActiveDirectoryConnectHealth, ActiveDirectory, ADB2C, ADDomainServices, ADIdentityProtection, ADPrivilegedIdentityManagement, AppRegistrations, ConditionalAccess, EnterpriseApplications, Groups, IdentityGovernance, InformationProtection, ManagedIdentities, Users

# Azure Integration
from diagrams.azure.integration import APIForFhir, APIManagement, AppConfiguration, DataCatalog, EventGridDomains, EventGridSubscriptions, EventGridTopics, IntegrationAccounts, IntegrationServiceEnvironments, LogicAppsCustomConnector, LogicApps, PartnerTopic, SendgridAccounts, ServiceBusRelays, ServiceBus, ServiceCatalogManagedApplicationDefinitions, SoftwareAsAService, StorsimpleDeviceManagers, SystemTopic

# Azure IoT
from diagrams.azure.iot import DeviceProvisioningServices, DigitalTwins, IotCentralApplications, IotHubSecurity, IotHub, Maps, Sphere, TimeSeriesInsightsEnvironments, TimeSeriesInsightsEventsSources, Windows10IotCoreServices

# Azure Migration
from diagrams.azure.migration import DataBoxEdge, DataBox, DatabaseMigrationServices, MigrationProjects, RecoveryServicesVaults

# Azure Machine Learning
from diagrams.azure.ml import BatchAI, BotServices, CognitiveServices, GenomicsAccounts, MachineLearningServiceWorkspaces, MachineLearningStudioWebServicePlans, MachineLearningStudioWebServices, MachineLearningStudioWorkspaces

# Azure Mobile
from diagrams.azure.mobile import AppServiceMobile, MobileEngagement, NotificationHubs

# Azure Monitor
from diagrams.azure.monitor import ChangeAnalysis, Logs, Metrics, Monitor

# Azure Networking
from diagrams.azure.network import ApplicationGateway, ApplicationSecurityGroups, CDNProfiles, Connections, DDOSProtectionPlans, DNSPrivateZones, DNSZones, ExpressrouteCircuits, Firewall, FrontDoors, LoadBalancers, LocalNetworkGateways, NetworkInterfaces, NetworkSecurityGroupsClassic, NetworkWatcher, OnPremisesDataGateways, PrivateEndpoint, PublicIpAddresses, ReservedIpAddressesClassic, RouteFilters, RouteTables, ServiceEndpointPolicies, Subnets, TrafficManagerProfiles, VirtualNetworkClassic, VirtualNetworkGateways, VirtualNetworks, VirtualWans

# Azure Security
from diagrams.azure.security import ApplicationSecurityGroups, ConditionalAccess, Defender, ExtendedSecurityUpdates, KeyVaults, SecurityCenter, Sentinel

# Azure Storage
from diagrams.azure.storage import ArchiveStorage, Azurefxtedgefiler, BlobStorage, DataBoxEdgeDataBoxGateway, DataBox, DataLakeStorage, GeneralStorage, NetappFiles, QueuesStorage, StorageAccountsClassic, StorageAccounts, StorageExplorer, StorageSyncServices, StorsimpleDataManagers, StorsimpleDeviceManagers, TableStorage

# Azure Web
from diagrams.azure.web import APIConnections, AppServiceCertificates, AppServiceDomains, AppServiceEnvironments, AppServicePlans, AppServices, MediaServices, NotificationHubNamespaces, Search, Signalr

Sure! Here's the consolidated import statements for the providers you listed:

# GCP Analytics
from diagrams.gcp.analytics import Bigquery, Composer, DataCatalog, DataFusion, Dataflow, Datalab, Dataprep, Dataproc, Genomics, Pubsub

# GCP API
from diagrams.gcp.api import APIGateway, Apigee, Endpoints

# GCP Compute
from diagrams.gcp.compute import AppEngine, ComputeEngine, ContainerOptimizedOS, Functions, GKEOnPrem, GPU, KubernetesEngine, Run

# GCP Database
from diagrams.gcp.database import Bigtable, Datastore, Firestore, Memorystore, Spanner, SQL

# GCP DevTools
from diagrams.gcp.devtools import Build, CodeForIntellij, Code, ContainerRegistry, GradleAppEnginePlugin, IdePlugins, MavenAppEnginePlugin, Scheduler, SDK, SourceRepositories, Tasks, TestLab, ToolsForEclipse, ToolsForPowershell, ToolsForVisualStudio

# GCP IoT
from diagrams.gcp.iot import IotCore

# GCP Migration
from diagrams.gcp.migration import TransferAppliance

# GCP Machine Learning
from diagrams.gcp.ml import AdvancedSolutionsLab, AIHub, AIPlatformDataLabelingService, AIPlatform, AutomlNaturalLanguage, AutomlTables, AutomlTranslation, AutomlVideoIntelligence, AutomlVision, Automl, DialogFlowEnterpriseEdition, InferenceAPI, JobsAPI, NaturalLanguageAPI, RecommendationsAI, SpeechToText, TextToSpeech, TPU, TranslationAPI, VideoIntelligenceAPI, VisionAPI

# GCP Networking
from diagrams.gcp.network import Armor, CDN, DedicatedInterconnect, DNS, ExternalIpAddresses, FirewallRules, LoadBalancing, NAT, Network, PartnerInterconnect, PremiumNetworkTier, Router, Routes, StandardNetworkTier, TrafficDirector, VirtualPrivateCloud, VPN

# GCP Operations
from diagrams.gcp.operations import Logging, Monitoring

# GCP Security
from diagrams.gcp.security import Iam, IAP, KeyManagementService, ResourceManager, SecurityCommandCenter, SecurityScanner

# GCP Storage
from diagrams.gcp.storage import Filestore, PersistentDisk, Storage

# IBM Analytics
from diagrams.ibm.analytics import Analytics, DataIntegration, DataRepositories, DeviceAnalytics, StreamingComputing

# IBM Applications
from diagrams.ibm.applications import ActionableInsight, Annotate, ApiDeveloperPortal, ApiPolyglotRuntimes, AppServer, ApplicationLogic, EnterpriseApplications, Index, IotApplication, Microservice, MobileApp, Ontology, OpenSourceTools, RuntimeServices, SaasApplications, ServiceBroker, SpeechToText, VisualRecognition, Visualization

# IBM Blockchain
from diagrams.ibm.blockchain import BlockchainDeveloper, Blockchain, CertificateAuthority, ClientApplication, Communication, Consensus, EventListener, Event, ExistingEnterpriseSystems, HyperledgerFabric, KeyManagement, Ledger, MembershipServicesProviderApi, Membership, MessageBus, Node, Services, SmartContract, TransactionManager, Wallet

# IBM Compute
from diagrams.ibm.compute import BareMetalServer, ImageService, Instance, Key, PowerInstance

# IBM Data
from diagrams.ibm.data import Caches, Cloud, ConversationTrainedDeployed, DataServices, DataSources, DeviceIdentityService, DeviceRegistry, EnterpriseData, EnterpriseUserDirectory, FileRepository, GroundTruth, Model, TmsDataInterface

# IBM DevOps
from diagrams.ibm.devops import ArtifactManagement, BuildTest, CodeEditor, CollaborativeDevelopment, ConfigurationManagement, ContinuousDeploy, ContinuousTesting, Devops, Provision, ReleaseManagement

# IBM General
from diagrams.ibm.general import CloudMessaging, CloudServices, Cloudant, CognitiveServices, DataSecurity, Enterprise, GovernanceRiskCompliance, IBMContainers, IBMPublicCloud, IdentityAccessManagement, IdentityProvider, InfrastructureSecurity, Internet, IotCloud, MicroservicesApplication, MicroservicesMesh, MonitoringLogging, Monitoring, ObjectStorage, OfflineCapabilities, Openwhisk, PeerCloud, RetrieveRank, Scalable, ServiceDiscoveryConfiguration, TextToSpeech, TransformationConnectivity

# IBM Infrastructure
from diagrams.ibm.infrastructure import Channels, CloudMessaging, Dashboard, Diagnostics, EdgeServices, EnterpriseMessaging, EventFeed, InfrastructureServices, InterserviceCommunication, LoadBalancingRouting, MicroservicesMesh, MobileBackend, MobileProviderNetwork, MonitoringLogging, Monitoring, PeerServices, ServiceDiscoveryConfiguration, TransformationConnectivity

# IBM Management
from diagrams.ibm.management import AlertNotification, ApiManagement, CloudManagement, ClusterManagement, ContentManagement, DataServices, DeviceManagement, InformationGovernance, ItServiceManagement, Management, MonitoringMetrics, ProcessManagement, ProviderCloudPortalService, PushNotifications, ServiceManagementTools

# IBM Network
from diagrams.ibm.network import Bridge, DirectLink, Enterprise, Firewall, FloatingIp, Gateway, InternetServices, LoadBalancerListener, LoadBalancerPool, LoadBalancer, LoadBalancingRouting, PublicGateway, Region, Router, Rules, Subnet, TransitGateway, Vpc, VpnConnection, VpnGateway, VpnPolicy

# IBM Security
from diagrams.ibm.security import ApiSecurity, BlockchainSecurityService, DataSecurity, Firewall, Gateway, GovernanceRiskCompliance, IdentityAccessManagement, IdentityProvider, InfrastructureSecurity, PhysicalSecurity, SecurityMonitoringIntelligence, SecurityServices, TrustendComputing, Vpn

# IBM Social
from diagrams.ibm.social import Communities, FileSync, LiveCollaboration, Messaging, Networking

# IBM Storage
from diagrams.ibm.storage import BlockStorage, ObjectStorage

# IBM User
from diagrams.ibm.user import Browser, Device, IntegratedDigitalExperiences, PhysicalEntity, Sensor, User

# K8S Chaos
from diagrams.k8s.chaos import ChaosMesh, LitmusChaos

# K8S Cluster Config
from diagrams.k8s.clusterconfig import HPA, Limits, Quota

# K8S Compute
from diagrams.k8s.compute import Cronjob, Deploy, DS, Job, Pod, RS, STS

# K8S Control Plane
from diagrams.k8s.controlplane import API, CCM, CM, KProxy, Kubelet, Sched

# K8S Ecosystem
from diagrams.k8s.ecosystem import ExternalDns, Helm, Krew, Kustomize

# K8S Group
from diagrams.k8s.group import NS

# K8S Infra
from diagrams.k8s.infra import ETCD, Master, Node

# K8S Network
from diagrams.k8s.network import Ep, Ing, Netpol, SVC

# K8S Others
from diagrams.k8s.others import CRD, PSP

# K8S Pod Config
from diagrams.k8s.podconfig import CM, Secret

# K8S RBAC
from diagrams.k8s.rbac import CRole, CRB, Group, RB, Role, SA, User

# K8S Storage
from diagrams.k8s.storage import PV, PVC, SC, Vol

# OCI Compute
from diagrams.oci.compute import AutoscaleWhite, Autoscale, BMWhite, BM, ContainerWhite, Container, FunctionsWhite, Functions, InstancePoolsWhite, InstancePools, OCIRWhite, OCIR, OKEWhite, OKE, VMWhite, VM

# OCI Connectivity
from diagrams.oci.connectivity import BackboneWhite, Backbone, CDNWhite, CDN, CustomerDatacenter, CustomerDatacntrWhite, CustomerPremisesWhite, CustomerPremises, DisconnectedRegionsWhite, DisconnectedRegions, DNSWhite, DNS, FastConnectWhite, FastConnect, NATGatewayWhite, NATGateway, VPNWhite, VPN

# OCI Database
from diagrams.oci.database import AutonomousWhite, Autonomous, BigdataServiceWhite, BigdataService, DatabaseServiceWhite, DatabaseService, DataflowApacheWhite, DataflowApache, DcatWhite, Dcat, DisWhite, Dis, DMSWhite, DMS, ScienceWhite, Science, StreamWhite, Stream

# OCI DevOps
from diagrams.oci.devops import APIGatewayWhite, APIGateway, APIServiceWhite, APIService, ResourceMgmtWhite, ResourceMgmt

# OCI Governance
from diagrams.oci.governance import AuditWhite, Audit, CompartmentsWhite, Compartments, GroupsWhite, Groups, LoggingWhite, Logging, OCIDWhite, OCID, PoliciesWhite, Policies, TaggingWhite, Tagging

# OCI Monitoring
from diagrams.oci.monitoring import AlarmWhite, Alarm, EmailWhite, Email, EventsWhite, Events, HealthCheckWhite, HealthCheck, NotificationsWhite, Notifications, QueueWhite, Queue, SearchWhite, Search, TelemetryWhite, Telemetry, WorkflowWhite, Workflow

# OCI Network
from diagrams.oci.network import DrgWhite, Drg, FirewallWhite, Firewall, InternetGatewayWhite, InternetGateway, LoadBalancerWhite, LoadBalancer, RouteTableWhite, RouteTable, SecurityListsWhite, SecurityLists, ServiceGatewayWhite, ServiceGateway, VcnWhite, Vcn

# OCI Security
from diagrams.oci.security import CloudGuardWhite, CloudGuard, DDOSWhite, DDOS, EncryptionWhite, Encryption, IDAccessWhite, IDAccess, KeyManagementWhite, KeyManagement, MaxSecurityZoneWhite, MaxSecurityZone, VaultWhite, Vault, WAFWhite, WAF

# OCI Storage
from diagrams.oci.storage import BackupRestoreWhite, BackupRestore, BlockStorageCloneWhite, BlockStorageClone, BlockStorageWhite, BlockStorage, BucketsWhite, Buckets, DataTransferWhite, DataTransfer, ElasticPerformanceWhite, ElasticPerformance, FileStorageWhite, FileStorage, ObjectStorageWhite, ObjectStorage, StorageGatewayWhite, StorageGateway

# Elastic Agent
from diagrams.elastic.agent import Agent, Endpoint, Fleet, Integrations

# Elastic Beats
from diagrams.elastic.beats import APM, Auditbeat, Filebeat, Functionbeat, Heartbeat, Metricbeat, Packetbeat, Winlogbeat

# Elastic Elasticsearch
from diagrams.elastic.elasticsearch import Alerting, Beats, Elasticsearch, Kibana, LogstashPipeline, Logstash, MachineLearning, MapServices, Maps, Monitoring, SearchableSnapshots, SecuritySettings, SQL, Stack

# Elastic Enterprise Search
from diagrams.elastic.enterprisesearch import AppSearch, Crawler, EnterpriseSearch, SiteSearch, WorkplaceSearch

# Elastic Observability
from diagrams.elastic.observability import APM, Logs, Metrics, Observability, Uptime

# Elastic Orchestration
from diagrams.elastic.orchestration import ECE, ECK

# Elastic SaaS
from diagrams.elastic.saas import Cloud, Elastic

# Elastic Security
from diagrams.elastic.security import Endpoint, Security, SIEM, Xdr

# Generic Blank
from diagrams.generic.blank import Blank

# Generic Compute
from diagrams.generic.compute import Rack

# Generic Database
from diagrams.generic.database import SQL

# Generic Device
from diagrams.generic.device import Mobile, Tablet

# Generic Network
from diagrams.generic.network import Firewall, Router, Subnet, Switch, VPN

# Generic OS
from diagrams.generic.os import Android, Centos, Debian, IOS, LinuxGeneral, Raspbian, RedHat, Suse, Ubuntu, Windows

# Generic Place
from diagrams.generic.place import Datacenter

# Generic Storage
from diagrams.generic.storage import Storage

# Generic Virtualization
from diagrams.generic.virtualization import Qemu, Virtualbox, Vmware, XEN

# Programming Flowchart
from diagrams.programming.flowchart import Action, Collate, Database, Decision, Delay, Display, Document, InputOutput, Inspection, InternalStorage, LoopLimit, ManualInput, ManualLoop, Merge, MultipleDocuments, OffPageConnectorLeft, OffPageConnectorRight, Or, PredefinedProcess, Preparation, Sort, StartEnd, StoredData, SummingJunction

# Programming Framework
from diagrams.programming.framework import Angular, Backbone, Camel, Django, Dotnet, Ember, Fastapi, Flask, Flutter, Graphql, Hibernate, Jhipster, Laravel, Micronaut, Nextjs, Quarkus, Rails, React, Spring, Starlette, Svelte, Vercel, Vue

# Programming Language
from diagrams.programming.language import Bash, C, Cpp, Csharp, Dart, Elixir, Erlang, Go, Java, Javascript, Kotlin, Latex, Matlab, Nodejs, Php, Python, R, Ruby, Rust, Scala, Swift, Typescript

# Programming Runtime
from diagrams.programming.runtime import Dapr

# SaaS Alerting
from diagrams.saas.alerting import Newrelic, Opsgenie, Pagerduty, Pushover, Xmatters

# SaaS Analytics
from diagrams.saas.analytics import Dataform, Snowflake, Stitch

# SaaS CDN
from diagrams.saas.cdn import Akamai, Cloudflare, Fastly

# SaaS Chat
from diagrams.saas.chat import Discord, Line, Mattermost, Messenger, RocketChat, Slack, Teams, Telegram

# SaaS Communication
from diagrams.saas.communication import Twilio

# SaaS File Sharing
from diagrams.saas.filesharing import Nextcloud

# SaaS Identity
from diagrams.saas.identity import Auth0, Okta

# SaaS Logging
from diagrams.saas.logging import Datadog, Newrelic, Papertrail

# SaaS Media
from diagrams.saas.media import Cloudinary

# SaaS Recommendation
from diagrams.saas.recommendation import Recombee

# SaaS Social
from diagrams.saas.social import Facebook, Twitte







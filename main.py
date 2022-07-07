

import boto3
import datetime
import json
import time

client = boto3.client(
    'cloudtrail',
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name="eu-west-2"
)


OUTPUT_PATH = ""

START_TIME = datetime.datetime(2020, 1, 1)
END_TIME = datetime.datetime(2021, 12, 24)

EventSources = [
    "signin.amazonaws.com",
    "backup.amazonaws.com",
    "events.amazonaws.com",
    "iam.amazonaws.com",
    "rds.amazonaws.com",
    "s3-outposts.amazonaws.com",
    "s3.amazonaws.com",
    "a4b.amazonaws.com",
    "acm-pca.amazonaws.com",
    "acm.amazonaws.com",
    "activate.amazonaws.com",
    "airflow.amazonaws.com",
    "amazonmq.amazonaws.com",
    "apigateway.amazonaws.com",
    "appconfig.amazonaws.com",
    "application-insights.amazonaws.com",
    "appmesh.amazonaws.com",
    "appsync.amazonaws.com",
    "assessment.amazonaws.com",
    "athena.amazonaws.com",
    "autoscaling.amazonaws.com",
    "backup.amazonaws.com",
    "batch.amazonaws.com",
    "billingconsole.amazonaws.com",
    "braket.amazonaws.com",
    "cassandra.amazonaws.com",
    "ce.amazonaws.com",
    "chime.amazonaws.com",
    "cloud9.amazonaws.com",
    "clouddirectory.amazonaws.com",
    "cloudformation.amazonaws.com",
    "cloudfront.amazonaws.com",
    "cloudhsm.amazonaws.com",
    "cloudsearch.amazonaws.com",
    "cloudshell.amazonaws.com",
    "cloudtrail.amazonaws.com",
    "codebuild.amazonaws.com",
    "codecommit.amazonaws.com",
    "codedeploy.amazonaws.com",
    "codeguru-profiler.amazonaws.com",
    "codeguru-reviewer.amazonaws.com",
    "codepipeline.amazonaws.com",
    "codestar-connections.amazonaws.com",
    "codestar.amazonaws.com",
    "cognito-identity.amazonaws.com",
    "cognito-idp.amazonaws.com",
    "cognito-sync.amazonaws.com",
    "comprehend.amazonaws.com",
    "compute-optimizer.amazonaws.com",
    "config.amazonaws.com",
    "connect.amazonaws.com",
    "dataexchange.amazonaws.com",
    "datapipeline.amazonaws.com",
    "dax.amazonaws.com",
    "diode.amazonaws.com",
    "directconnect.amazonaws.com",
    "discovery.amazonaws.com",
    "dlm.amazonaws.com",
    "dms.amazonaws.com",
    "ds.amazonaws.com",
    "dynamodb.amazonaws.com",
    "ebs.amazonaws.com",
    "ec2-instance-connect.amazonaws.com",
    "ec2.amazonaws.com",
    "ecr.amazonaws.com",
    "ecs.amazonaws.com",
    "eks.amazonaws.com",
    "elasticache.amazonaws.com",
    "elasticbeanstalk.amazonaws.com",
    "elasticfilesystem.amazonaws.com",
    "elasticloadbalancing.amazonaws.com",
    "elasticmapreduce.amazonaws.com",
    "elastictranscoder.amazonaws.com",
    "emr-containers.amazonaws.com",
    "es.amazonaws.com",
    "finspace-api.amazonaws.com",
    "finspace.amazonaws.com",
    "firehose.amazonaws.com",
    "fms.amazonaws.com",
    "freertos.amazonaws.com",
    "fsx.amazonaws.com",
    "gamelift.amazonaws.com",
    "glacier.amazonaws.com",
    "glue.amazonaws.com",
    "grafana.amazonaws.com",
    "greengrass.amazonaws.com",
    "guardduty.amazonaws.com",
    "health.amazonaws.com",
    "honeycode.amazonaws.com",
    "imagebuilder.amazonaws.com",
    "importexport.amazonaws.com",
    "inspector.amazonaws.com",
    "iot.amazonaws.com",
    "iotanalytics.amazonaws.com",
    "iotsitewise.amazonaws.com",
    "iotthingsgraph.amazonaws.com",
    "iotwireless.amazonaws.com",
    "kafka-cluster.amazonaws.com",
    "kinesis.amazonaws.com",
    "kinesisanalytics.amazonaws.com",
    "kms.amazonaws.com",
    "lakeformation.amazonaws.com",
    "lambda.amazonaws.com",
    "launchwizard.amazonaws.com",
    "lex.amazonaws.com",
    "lightsail.amazonaws.com",
    "logs.amazonaws.com",
    "lookoutmetrics.amazonaws.com",
    "machinelearning.amazonaws.com",
    "managedservices.amazonaws.com",
    "mediaconnect.amazonaws.com",
    "mediaconvert.amazonaws.com",
    "mediapackage.amazonaws.com",
    "mediastore.amazonaws.com",
    "mediatailor.amazonaws.com",
    "memorydb.amazonaws.com",
    "metering-marketplace.amazonaws.com",
    "mgn.amazonaws.com",
    "migrationhub.amazonaws.com",
    "mobilehub.amazonaws.com",
    "monitoring.amazonaws.com",
    "network-firewall.amazonaws.com",
    "opsworks-cm.amazonaws.com",
    "opsworks.amazonaws.com",
    "organizations.amazonaws.com",
    "outposts.amazonaws.com",
    "participant-connect.amazonaws.com",
    "pinpoint.amazonaws.com",
    "polly.amazonaws.com",
    "pricelist.amazonaws.com",
    "proton.amazonaws.com",
    "qldb.amazonaws.com",
    "quicksight.amazonaws.com",
    "ram.amazonaws.com",
    "redshift.amazonaws.com",
    "rekognition.amazonaws.com",
    "resource-groups.amazonaws.com",
    "robomaker.amazonaws.com",
    "route53.amazonaws.com",
    "route53domains.amazonaws.com",
    "route53resolver.amazonaws.com",
    "sagemaker.amazonaws.com",
    "schemas.amazonaws.com",
    "secretsmanager.amazonaws.com",
    "securityhub.amazonaws.com",
    "serverlessrepo.amazonaws.com",
    "servicecatalog.amazonaws.com",
    "servicediscovery.amazonaws.com",
    "servicequotas.amazonaws.com",
    "ses.amazonaws.com",
    "shield.amazonaws.com",
    "signer.amazonaws.com",
    "sms.amazonaws.com",
    "sns.amazonaws.com",
    "sqs.amazonaws.com",
    "ssm.amazonaws.com",
    "sso.amazonaws.com",
    "states.amazonaws.com",
    "storagegateway.amazonaws.com",
    "support.amazonaws.com",
    "swf.amazonaws.com",
    "synthetics.amazonaws.com",
    "tagging.amazonaws.com",
    "timestream.amazonaws.com",
    "transcribe.amazonaws.com",
    "transcribestreaming.amazonaws.com",
    "transfer.amazonaws.com",
    "translate.amazonaws.com",
    "trustedadvisor.amazonaws.com",
    "tts.amazonaws.com",
    "voiceid.amazonaws.com",
    "waf-regional.amazonaws.com",
    "waf.amazonaws.com",
    "wafv2.amazonaws.com",
    "wellarchitected.amazonaws.com",
    "workdocs.amazonaws.com",
    "worklink.amazonaws.com",
    "workmail.amazonaws.com",
    "workspaces.amazonaws.com",
    "xray.amazonaws.com",
    "sts.amazonaws.com"
]


for source in EventSources:

    print("Searching: " + source)


    NextToken = ""
    BreakMe = False

    while(True):

        # Throttled to 1 request per second
        time.sleep(1)

        if NextToken == "": # First time

            response = client.lookup_events(
                LookupAttributes=[
                    {
                        'AttributeKey': 'EventSource',
                        'AttributeValue': source
                    },
                ],
                StartTime=START_TIME,
                EndTime=END_TIME,
                MaxResults=50
            )

        else: # second time
            
            response = client.lookup_events(
                LookupAttributes=[
                    {
                        'AttributeKey': 'EventSource',
                        'AttributeValue': source
                    },
                ],
                StartTime=START_TIME,
                EndTime=END_TIME,
                NextToken=NextToken,
                MaxResults=50
            )

        try:
            NextToken = response["NextToken"]
        except KeyError:
            BreakMe = True
        finally:

            print("Returned " + str(len(response['Events'])) + " events.")

            if len(response["Events"]) > 0:
                # Iterate through events
                with open(OUTPUT_PATH, 'a') as f:
                    for event in response['Events']:
                        jsonEvent = json.loads(event['CloudTrailEvent'])
                        sourceIP = jsonEvent['sourceIPAddress']

                        json.dump(jsonEvent, f)
                        f.write('\n')


            if NextToken == "" or BreakMe == True:
                BreakMe = False
                break

print("Finished collection")
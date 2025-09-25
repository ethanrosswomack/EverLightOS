import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as iam from 'aws-cdk-lib/aws-iam';

export class ApmStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const sessionTable = new dynamodb.Table(this, 'SessionTable', {
      partitionKey: { name: 'session_id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const itemsTable = new dynamodb.Table(this, 'ItemsTable', {
      partitionKey: { name: 'session_id', type: dynamodb.AttributeType.STRING },
      sortKey: { name: 'item_id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const artifactBucket = new s3.Bucket(this, 'ArtifactBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    const lambdaFn = new lambda.Function(this, 'ApmHandler', {
      runtime: lambda.Runtime.PYTHON_3_11,
      handler: 'handler.lambda_handler',
      code: lambda.Code.fromAsset('lambda/'),
      environment: {
        SESSION_TABLE: sessionTable.tableName,
        ITEMS_TABLE: itemsTable.tableName,
        ARTIFACT_BUCKET: artifactBucket.bucketName,
      }
    });

    sessionTable.grantReadWriteData(lambdaFn);
    itemsTable.grantReadWriteData(lambdaFn);
    artifactBucket.grantReadWrite(lambdaFn);

    const api = new apigateway.RestApi(this, 'ApmApi', {
      restApiName: 'APM Service',
    });

    const session = api.root.addResource('session');
    const sessionId = session.addResource('{id}');
    sessionId.addResource('item').addMethod('POST', 
      new apigateway.LambdaIntegration(lambdaFn)
    );
    sessionId.addResource('render').addMethod('GET',
      new apigateway.LambdaIntegration(lambdaFn)
    );
  }
}
# aws-cicd-infrastructure-as-code

This project creates **CI/CD Pipeline** through AWS CloudFormation. This pipeline is then responsible for deployment of other **Infrastructure Stacks**, thus bringing the entire *AWS Infrastructure starting from the Application and its Deployment to code*. This can be deployed anywhere with absolutely no prerequisite resources to be configured. All you need is an AWS environment, and account to let GitHub and CFN carry out operations on your behalf.

> **Article on Mediumn** : https://medium.com/@pratyayp1999/manage-ci-cd-infrastructure-as-code-f6b504eb87e5

## Architecture
![Image](Architecture/createinfra.drawio.png?raw=true)
>The above architecture diagram shows the workflow of how the CI/CD Infrastructure is deployed.

![Image](Architecture/architecture.drawio.png?raw=true)
>The above architecture diagram shows the workflow of how the Application CFN is deployed into CloudFormation Stacks using the Code Pipeline created above.


### Resources

The following AWS resources are created:

|Name                |Type                          |Purpose                         |
|----------------|-------------------------------|-----------------------------|
|aws-cicd-artifacts-store|S3 Bucket|Artifact store for Codepipeline. Codepipeline will generate artifacts for the subsequent stages which are stored here.|
|aws-cfn-infra-store|S3 Bucket|Bucket where Source Artifact for Codepipeline is stored. This is where the CFN for your stack will go to. Github actions will auomatically place the ZIP here.|
|AWS-CFN-Infra-Role|IAM Role|Role that Cloudformation assumes when creating resources on AWS.|
|AWS-Lambda-S3-Role|IAM Role|Role that Lambda uses to connect to S3.|
|Eventbridge-pipeline-Role|IAM Role|Role that EventBridge uses to trigger Code Pipeline.|
|cicd-pipeline-infra-deployment|Code Pipeline|The CICD Pipeline which does stack deployment.|
|EB-Execute-Pipeline-From-S3-Put|Eventbridge Rule|The Event bridge Rule which triggers CICD Pipeline on S3 PUT.|
|lambda-to-delete-S3-files|Lambda|Lambda which deletes files in S3 before bucket deletion.|
|infrastructure-stack|CFN Stack|Name of stack of the Infrastructure (Not the CI/CD one).|
|S3-Put-Event-Logging|CloudTrail|Cloudtrail which listens to S3 Put Object API|

> **Note:** Do **NOT** delete the **CI/CD Pipeline stack** before deleting the **infrastructure-stack**. If AWS-CFN-Infra-Role gets deleted CFN will not be able to delete the **infrastructure-stack**.
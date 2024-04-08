import json
import boto3
import cfnresponse

s3 = boto3.client('s3')
response_data = {}
def lambda_handler(event, context):
    print("Event : "+str(event))
    bucket_name=event['ResourceProperties']['bucket_name']
    try:
        if event['RequestType'] == 'Delete':                
            allObjs = s3.list_object_versions(Bucket=bucket_name)
            for objVer in allObjs.get('Versions', []):
                s3.delete_object(
                    Bucket=bucket_name,
                    Key=objVer['Key'],
                    VersionId=objVer['VersionId']
                )                  
            for objDelMrkr in allObjs.get('DeleteMarkers', []):
                s3.delete_object(
                    Bucket=bucket_name,
                    Key=objDelMrkr['Key'],
                    VersionId=objDelMrkr['VersionId']
                )
        print("Execution succesfull!")
        cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
    except Exception as e:
        print("Execution failed...")
        print(str(e))
        response_data['Data'] = str(e)
        cfnresponse.send(event, context, cfnresponse.FAILED, response_data)
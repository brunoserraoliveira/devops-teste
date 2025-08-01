import json

def handler(event, context):
    print(f"Event received: {json.dumps(event)}")
    
    # API Gateway v1.0 (REST API) format
    if 'requestContext' in event:
        path = event.get('path', '/')
        method = event.get('httpMethod', 'GET')
        
        print(f"HTTP {method} request to {path}")
        
        # Roteamento baseado no path (remove /dev prefix)
        clean_path = path.replace('/dev', '') or '/'
        print(f"Clean path for routing: {clean_path}")
        
        if clean_path.endswith('/hello'):
            response_body = {"message": "Hello World!"}
        elif clean_path.endswith('/echo'):
            query_params = event.get('queryStringParameters', {}) or {}
            msg = query_params.get('msg', 'No message provided')
            response_body = {"echo": msg}
        elif clean_path.endswith('/health'):
            response_body = {"status": "healthy", "service": "devops-test-api"}
        elif clean_path == '/':
            response_body = {"message": "Hello World from Lambda!"}
        else:
            response_body = {"message": "Hello World from Lambda!", "path": clean_path}
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response_body)
        }
    
    # Fallback para outros tipos de evento
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({"message": "Hello from Lambda!", "event_type": str(type(event))})
    }
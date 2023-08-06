Logging Module for Azure Log Analytics


#### Install
- add to your requirements.txt: `git+ssh://walmart@vs-ssh.visualstudio.com:22/Post%20Payment%20Audit%20Email%20Classification/_ssh/aiohttp_azure_logging`
- Build your container with valid ssh credentials

#### Implement
```
from aiohttp_azure_logging import send_to_azure

app = web.application()
settings = {
	'workspace_id': '<YOUR WORKSPACE ID>',
	'workspace_secret' '<YOUR WORKSPACE PRIMARY OR SECONDARY KEY>'
}
send_to_azure(app, settings)
```

To send custom events:
```
async def my_view(request):
	await request.app['oms'].create_event(
		log_type='new_event_category'
		name='specific_event_name',
		request=request,
		event_data={
			'retry_attempts': 0,
			'success': True,
			'response_message': "Success",
			'nested_object': {
				'value_one': 'test'
			}
		})
```
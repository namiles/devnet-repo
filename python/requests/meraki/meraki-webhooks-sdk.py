import meraki
import json

X_CISCO_MERAKI_API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0" #read-only sandbox key

# Create new client connection
dashboard = meraki.DashboardAPI(X_CISCO_MERAKI_API_KEY)

#Returns dict of alert settings
alertSettings = dashboard.networks.getNetworkAlertsSettings('L_646829496481105433')
cleanAlertSettings = json.dumps(alertSettings, indent=4)

#print alert settings in readable string format
print(cleanAlertSettings)

print()

#Get http servers
httpsServers = dashboard.networks.getNetworkWebhooksHttpServers('L_646829496481105433')
cleanHttpServers = json.dumps(httpsServers, indent=4)
print(cleanHttpServers)

print()

#Updating Alert settings/HTTP servers using PUT
updateAlerts = dashboard.networks.updateNetworkAlertsSettings(
    'L_646829496481105433',
    defaultDestination = {
        'emails': ['testupdate@example.com']
    },
    alerts = [{
        'type':'gatewayDown',
        'enable': True
    }]
)

network_id = 'L_646829496481104079'
name = 'My HTTP server'
url = 'https://www.example.com/webhooks'

response = dashboard.http_servers.createNetworkHttpServer(
    network_id, name, url, 
    sharedSecret='foobar'
)
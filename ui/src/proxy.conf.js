const PROXY_CONFIG = {
    "/api/*": {
        "target": "https://glassdoranalyticsapi.azurewebsites.net",
        "secure": false,
        "logLevel": "debug"
    }
}

module.exports = PROXY_CONFIG;
const PROXY_CONFIG = {
    "/api": {
        "target": "http://127.0.0.1:5000",
        "secure": false
    }
}

module.exports = PROXY_CONFIG;
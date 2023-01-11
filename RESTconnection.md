## Values for setting up connection in Azure Data factory ingest.

### REST linked service connection
 - Source Type: REST
 - Connection:
    - BaseURL: https://api.spotify.com/v1
    - Authentication Type: OAuth2
    - Token Endpoint: https://accounts.spotify.com/api/token
    - scope: user-read-recently-played
 - Auth headers:
    - response_type (required): code
    - redirect_uri (required): see application settings in development dashboard
    - state (optional, provides protection against attacks)
### Other
 - Relative URL: https://api.spotify.com/v1/me/player/recently-played
 - Request method: GET
 - headers:
    - grant_type:
    - redirect_uri:
 
